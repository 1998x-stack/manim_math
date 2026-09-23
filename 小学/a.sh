#!/usr/bin/env bash
set -e
here="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
exec bash "$here/../tools/legacy/primary-pending-prompts.sh" "$@"
