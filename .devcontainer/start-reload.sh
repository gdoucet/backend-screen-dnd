#!/usr/bin/env bash

cd /workspace/.devcontainer
parallel --line-buffer --tag ::: "./backend.sh" "./frontend.sh"
exit 0