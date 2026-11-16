"""Test retrieval on the ITU-format KB with the reference code's own embedding + KnowledgeBase.search.
usage: python -I test_itu_kb.py <ITUAIReadiness/simulation> <chromadb_dir>"""
import os, re, sys
from pathlib import Path
sim, out = Path(sys.argv[1]), Path(sys.argv[2])
os.environ["AIREADY_CHROMADB_DIR"] = str(out); os.environ["AIREADY_OLLAMA_BASE_URL"] = "http://127.0.0.1:11434"
sys.path.insert(0, str(sim))
from server.knowledge.kb import KnowledgeBase
from server.knowledge.ingest import embed_texts
kb = KnowledgeBase(persist_dir=str(out))
tests = [  # (partition, question, text that must appear in a top-5 passage, what it is)
 ("FEDERAL", "store or transfer health data outside the country", "outside the country", "Federal Law 2/2019 Art. 13"),
 ("FEDERAL", "patient written consent exceptions scientific research identity not disclosed", "identity is not disclosed", "Federal Law 2/2019 Art. 16"),
 ("DHA", "transfer of medical record to another entity for continuing care", "separate Patient consent is required", "DHA PP-13 4.6.4"),
 ("DHA", "anonymised information definition cannot identify individual", "cannot be practically used to determine their identity", "DHA PP-13 definition"),
 ("DHA", "protected health information transferred outside the UAE exemptions", "outside the UAE", "DHA PP-11 4.15.1"),
 ("DOH", "healthcare facilities obtain patient consent for sharing via the health information exchange", "obtain patient consent for the sharing", "DoH ADHIE 4.2.1.2"),
 ("DOH", "store develop or transfer PHI outside the United Arab Emirates", "outside the United Arab Emirates", "DoH Privacy Std 4.1.4"),
 ("DOH", "research purposes de-identified data only", "de-identified data only", "Malaffi notice"),
]
norm = lambda s: re.sub(r"\s+", " ", s).lower()
ok = 0
for part, q, must, label in tests:
    r = kb.search(embed_texts([q])[0], n_results=5, where={"$and": [{"partition": part}, {"country": "United Arab Emirates"}]})
    docs, metas = r["documents"][0], r["metadatas"][0]
    hit = next((i for i, d in enumerate(docs) if norm(must) in norm(d)), None)
    ok += hit is not None
    print(f"{'PASS' if hit is not None else 'MISS'}  {label:26} rank={hit+1 if hit is not None else '-'}  top doc: {metas[0]['doc_id']}")
print(f"{ok}/{len(tests)} clauses found in the top 5")
fw = kb.search(embed_texts(["AI and policies dimension"])[0], n_results=1, collection_name="kb_framework")
print("framework collection sample:", fw["documents"][0][0][:90])
