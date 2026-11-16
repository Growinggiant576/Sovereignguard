"""Check the knowledge base against its recorded fingerprints.
1. Every text file in kb/text matches the SHA-256 recorded in kb/sha256.json.
2. The knowledge-base fingerprint (same method as sovereignguard/kb.py: kb/manifest.json + all kb/text/*.txt)
   matches the fingerprint recorded in every saved run in runs/.
usage (from the repo root): python3 kb/verify_manifest.py"""
import hashlib
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
bad = 0
entries = json.loads((root / "kb" / "sha256.json").read_text(encoding="utf-8"))
for d in entries:
    ok = hashlib.sha256((root / d["text_file"]).read_bytes()).hexdigest() == d["sha256"]
    bad += not ok
    print(f"{'OK  ' if ok else 'FAIL'} {d['text_file']}")
print(f"{len(entries) - bad} of {len(entries)} text files match kb/sha256.json")

h = hashlib.sha256((root / "kb" / "manifest.json").read_bytes())
for p in sorted((root / "kb" / "text").glob("*.txt")):
    h.update(p.name.encode()); h.update(p.read_bytes())
fp = h.hexdigest()[:16]
runs = sorted((root / "runs").glob("*.json"))
recorded = {json.loads(r.read_text(encoding="utf-8")).get("kb_fingerprint") for r in runs}
match = recorded == {fp}
bad += not match
print(f"knowledge-base fingerprint {fp}: {'matches' if match else 'DOES NOT match'} all {len(runs)} saved runs (recorded: {', '.join(sorted(map(str, recorded)))})")
sys.exit(1 if bad else 0)
