"""Knowledge base: ingest public UAE regulation texts into ChromaDB and search them.

Each document belongs to one partition (FEDERAL, DHA, DOH). Each regulator agent
searches ONLY its own partition - that is what keeps the agents' mandates separate.

    python -m sovereignguard.kb ingest      # build / rebuild the vector store
    python -m sovereignguard.kb search DHA "patient consent for sharing records"
"""
import hashlib
import json
import re
import sys
import threading
from pathlib import Path

import chromadb

ROOT = Path(__file__).resolve().parent.parent
KB_TEXT = ROOT / "kb" / "text"
MANIFEST = ROOT / "kb" / "manifest.json"
DB_PATH = ROOT / ".chroma"
COLLECTION = "sovereignguard_kb"


def load_manifest():
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def kb_fingerprint() -> str:
    """Hash of manifest + all text files, recorded in every run trace."""
    h = hashlib.sha256(MANIFEST.read_bytes())
    for p in sorted(KB_TEXT.glob("*.txt")):
        h.update(p.name.encode())
        h.update(p.read_bytes())
    return h.hexdigest()[:16]


def chunk_text(text: str, max_chars: int = 1400, overlap: int = 200):
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks, cur = [], ""
    for p in paras:
        if len(cur) + len(p) + 1 <= max_chars:
            cur = (cur + "\n" + p).strip()
            continue
        if cur:
            chunks.append(cur)
        if len(p) > max_chars:
            step = max_chars - overlap
            for i in range(0, len(p), step):
                chunks.append(p[i:i + max_chars])
            cur = ""
        else:
            cur = p
    if cur:
        chunks.append(cur)
    return chunks


_lock = threading.Lock()
_client = None
_col = None


def _collection(create=False):
    """One shared ChromaDB client per process (agents query it from parallel threads)."""
    global _client, _col
    with _lock:
        if _client is None:
            _client = chromadb.PersistentClient(path=str(DB_PATH))
        if create:
            try:
                _client.delete_collection(COLLECTION)
            except Exception:
                pass
            _col = _client.create_collection(COLLECTION)
        elif _col is None:
            _col = _client.get_collection(COLLECTION)
        return _col


def ingest():
    col = _collection(create=True)
    total = 0
    for doc in load_manifest():
        path = KB_TEXT / f"{doc['doc_id']}.txt"
        text = path.read_text(encoding="utf-8")
        chunks = chunk_text(text)
        ids = [f"{doc['doc_id']}::{i:04d}" for i in range(len(chunks))]
        metas = [{
            "doc_id": doc["doc_id"], "title": doc["title"], "partition": doc["partition"],
            "source_url": doc["source_url"], "chunk": i,
        } for i in range(len(chunks))]
        for s in range(0, len(chunks), 200):
            col.add(ids=ids[s:s + 200], documents=chunks[s:s + 200], metadatas=metas[s:s + 200])
        total += len(chunks)
        print(f"  {doc['partition']:8} {doc['doc_id']:40} {len(chunks):4} chunks")
    print(f"Ingested {total} chunks. KB fingerprint {kb_fingerprint()}")


def search(partition: str, query: str, k: int = 6):
    col = _collection()
    res = col.query(query_texts=[query], n_results=k, where={"partition": partition})
    out = []
    for cid, doc, meta, dist in zip(res["ids"][0], res["documents"][0], res["metadatas"][0], res["distances"][0]):
        out.append({
            "excerpt_id": cid, "doc_id": meta["doc_id"], "title": meta["title"],
            "partition": meta["partition"], "source_url": meta["source_url"],
            "distance": round(float(dist), 4), "text": doc,
        })
    return out


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "ingest":
        ingest()
    elif len(sys.argv) >= 4 and sys.argv[1] == "search":
        for r in search(sys.argv[2], " ".join(sys.argv[3:])):
            print(f"[{r['excerpt_id']}] d={r['distance']} {r['title']}\n  {r['text'][:300]!r}\n")
    else:
        print(__doc__)
