#!/usr/bin/env bash
# sync-brand-core.sh
# Mirrors brand-core tokens + fonts into site/ so the live deploy uses the same source.
# Run this any time you edit brand-core/tokens.css or brand-core/fonts/.
# CI runs it automatically before publishing to GitHub Pages.

set -euo pipefail
repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Syncing brand-core -> site ..."

cp "$repo/brand-core/tokens.css" "$repo/site/colors_and_type.css"
echo "  tokens.css -> site/colors_and_type.css"

mkdir -p "$repo/site/fonts"
cp -f "$repo/brand-core/fonts/"* "$repo/site/fonts/"
echo "  brand-core/fonts/* -> site/fonts/"

echo "Done."
