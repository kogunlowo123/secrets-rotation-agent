#!/bin/bash
set -euo pipefail
echo "Setting up Secrets Rotation Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
