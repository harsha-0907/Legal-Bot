#!/bin/sh
source .venv/bin/activate
uvicorn server:app --reload