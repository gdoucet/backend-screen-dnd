#!/usr/bin/env bash

cd /workspace/.devcontainer
parallel --line-buffer --tag ::: "./backend" "./frontend"
exit 0