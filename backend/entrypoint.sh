#!/bin/sh
./.venv/bin/aerich upgrade
.venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000
