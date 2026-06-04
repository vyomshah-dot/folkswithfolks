# sync-brand-core.ps1
# Mirrors brand-core tokens + fonts into site/ so the live deploy uses the same source.
# Run this any time you edit brand-core/tokens.css or brand-core/fonts/.
# CI runs it automatically before publishing to GitHub Pages.

$ErrorActionPreference = 'Stop'
$repo = Split-Path -Parent $PSScriptRoot

Write-Host "Syncing brand-core -> site ..." -ForegroundColor Cyan

# Tokens: brand-core/tokens.css -> site/colors_and_type.css
Copy-Item "$repo\brand-core\tokens.css" "$repo\site\colors_and_type.css" -Force
Write-Host "  tokens.css -> site/colors_and_type.css"

# Fonts: brand-core/fonts/* -> site/fonts/
$siteFonts = "$repo\site\fonts"
if (-not (Test-Path $siteFonts)) { New-Item -ItemType Directory -Path $siteFonts | Out-Null }
Copy-Item "$repo\brand-core\fonts\*" $siteFonts -Force
Write-Host "  brand-core/fonts/* -> site/fonts/"

Write-Host "Done." -ForegroundColor Green
