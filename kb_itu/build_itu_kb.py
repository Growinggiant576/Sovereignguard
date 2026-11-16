"""Build SovereignGuard's 12-document UAE knowledge base with the ITU reference code
(github.com/CrashingGuru/ITUAIReadiness, unmodified), using its own parsing, chunking,
nomic-embed-text embeddings (Ollama) and KnowledgeBase class.
usage: python -I build_itu_kb.py <ITUAIReadiness/simulation> <Sovereignguard> <output_chromadb_dir>"""
import json, os, sys
from pathlib import Path
sim, sg, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
os.environ["AIREADY_CHROMADB_DIR"] = str(out)
os.environ["AIREADY_OLLAMA_BASE_URL"] = "http://127.0.0.1:11434"
sys.path.insert(0, str(sim))
from server.knowledge.kb import KnowledgeBase
from server.knowledge.ingest import ingest_file, ingest_framework_definitions
out.mkdir(parents=True, exist_ok=True)
kb = KnowledgeBase(persist_dir=str(out))
kb.reset()
print("framework definitions:", ingest_framework_definitions(kb))
total = 0
for d in json.loads((sg / "kb" / "manifest.json").read_text(encoding="utf-8")):
    n = ingest_file(sg / "kb" / "text" / f"{d['doc_id']}.txt", kb, extra_metadata={
        "country": "United Arab Emirates", "document_category": d["partition"], "partition": d["partition"],
        "doc_id": d["doc_id"], "title": d["title"], "issuer": d.get("issuer", ""), "source_url": d["source_url"]})
    print(f"  {d['partition']:8} {d['doc_id']:38} {n:4} chunks"); total += n
print("total chunks:", total, "| KB stats:", kb.stats())
