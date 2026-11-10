#!/bin/sh
# Starts the SovereignGuard dashboard on this computer only (127.0.0.1). No login, so never widen the address.
cd "$(dirname "$0")" && exec .venv/bin/streamlit run dashboard.py --server.address 127.0.0.1 --server.port 8501 --browser.gatherUsageStats false --client.toolbarMode minimal
