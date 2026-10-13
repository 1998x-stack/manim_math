#!/usr/bin/env bash
# Transitional entry point. The repository runtime is ManimGX on this branch.
set -euo pipefail
exec "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/install_manimgx.sh" "$@"
