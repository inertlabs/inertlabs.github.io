#!/usr/bin/env bash
# Renders the Inert Labs logo from gen_logo.py: the SVG sources, then PNGs at each size.
# Needs macOS (Quick Look renders the SVG) and ImageMagick.
set -euo pipefail
cd "$(dirname "$0")"
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT

rm -rf svg png
python3 gen_logo.py svg
mkdir -p png
for svg in svg/*.svg; do
  qlmanage -t -s 1024 -o "$work" "$svg" >/dev/null 2>&1
  cp "$work/$(basename "$svg").png" "png/$(basename "$svg" .svg)-1024.png"
done
for size in 512 180; do
  magick png/inertlabs-icon-dark-1024.png -resize "${size}x${size}" "png/inertlabs-icon-dark-${size}.png"
done
for size in 16 32 48; do
  magick png/inertlabs-favicon-dark-1024.png -resize "${size}x${size}" "png/inertlabs-favicon-dark-${size}.png"
done
