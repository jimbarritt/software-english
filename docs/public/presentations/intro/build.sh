#!/usr/bin/env bash
# Build the deck: HTML with Marp, then PDF with Playwright's Chromium.
# Marp's own PDF export needs a browser with open network access, which
# a sandboxed session does not have, so the PDF step prints the Marp
# HTML through Playwright instead.
#
# Usage: ./build.sh            builds build/intro-to-software-english.{html,pdf}
#        ./build.sh --png      also writes one PNG per slide into build/slides/
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
deck="$here/intro-to-software-english.md"
out="$here/build"
name="intro-to-software-english"
marp_version="4.1.2"

mkdir -p "$out"

# The deck path goes first: --theme-set takes a list and would otherwise
# read the deck as a second theme file.
npx --yes --prefer-offline "@marp-team/marp-cli@${marp_version}" "$deck" \
  --html \
  --theme-set "$here/theme.css" \
  -o "$out/$name.html"

node -e '
const { chromium } = require("playwright");
(async () => {
  const [html, pdf] = process.argv.slice(1);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto("file://" + html);
  await page.pdf({ path: pdf, width: "1280px", height: "720px", printBackground: true });
  await browser.close();
})();
' "$out/$name.html" "$out/$name.pdf"

echo "built $out/$name.html and $out/$name.pdf"

if [[ "${1:-}" == "--png" ]]; then
  mkdir -p "$out/slides"
  rm -f "$out/slides"/*.png
  pdftoppm -png -r 72 "$out/$name.pdf" "$out/slides/slide"
  echo "wrote $(ls "$out/slides" | wc -l) slide images to $out/slides/"
fi
