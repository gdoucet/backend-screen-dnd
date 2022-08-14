#!/usr/bin/env bash

export PORT=8888
export PYTHONPATH=/workspace/backend/app
export MODULE_NAME=main
exec /bin/bash /workspace/backend/docker-images/start-reload.sh
