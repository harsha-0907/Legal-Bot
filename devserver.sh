#!/bin/sh
source .venv/bin/activate
streammlit run FrontEnd/HOME.py
uvicorn backend_server:app --reload