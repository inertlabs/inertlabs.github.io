"""Generates the Inert Labs logo as self-contained SVG: an element tile whose border is a closed electron shell, with
"Il" as the nucleus and two electrons on the shell. No fonts: every shape is drawn geometry."""

import sys
from pathlib import Path

FRAME = 1024
CHARCOAL_TOP = "#262C33"
CHARCOAL_BOTTOM = "#14181C"
PEACH = "#FFB38A"
PAPER = "#F4EFE6"
INK = "#1E2328"

# Per size class: the tile's inset, corner radius and border width, the symbol's height, and the electrons' radius.
# The favicon is bolder so it survives 16-32 px.
LAYOUTS = {
    "icon": {"inset": 176, "corner": 84, "border": 30, "symbol": 300, "electron": 48},
    "favicon": {"inset": 112, "corner": 120, "border": 60, "symbol": 440, "electron": 72},
}


def symbol(cx, cy, height, color):
    """"Il" as filled shapes: a slab-serif capital I and a lowercase l with a hooked foot, so the pair never reads as
    "II" or "ll". Centered on (cx, cy)."""
    top = cy - height / 2
    stem = height * 0.19
    serif = height * 0.46
    slab = height * 0.15
    gap = height * 0.36
    hook = height * 0.3
    round_corner = stem * 0.12
    i_left = cx - gap / 2 - serif
    i_stem = i_left + (serif - stem) / 2
    l_left = cx + gap / 2
    return (
        f'<g fill="{color}">'
        f'<rect x="{i_stem:.1f}" y="{top:.1f}" width="{stem:.1f}" height="{height}" rx="{round_corner:.1f}"/>'
        f'<rect x="{i_left:.1f}" y="{top:.1f}" width="{serif:.1f}" height="{slab:.1f}" rx="{round_corner:.1f}"/>'
        f'<rect x="{i_left:.1f}" y="{top + height - slab:.1f}" width="{serif:.1f}" height="{slab:.1f}" '
        f'rx="{round_corner:.1f}"/>'
        f'<path d="M{l_left:.1f},{top:.1f} h{stem:.1f} V{top + height - hook:.1f} '
        f'a{hook / 2:.1f},{hook / 2:.1f} 0 0 0 {hook / 2:.1f},{hook / 2:.1f} h{hook * 0.42:.1f} v{hook / 2:.1f} '
        f'h{-hook * 0.42:.1f} a{hook / 2 + stem:.1f},{hook / 2 + stem:.1f} 0 0 1 {-hook / 2 - stem:.1f},'
        f'{-hook / 2 - stem:.1f} Z"/>'
        f'</g>'
    )


def electrons(layout, color):
    """The shell's two electrons: on the top edge right of center and the bottom edge left of center, point-symmetric
    so they read as orbiting the tile."""
    inset, radius = layout["inset"], layout["electron"]
    far = FRAME - inset
    offset = (far - inset) * 0.22
    points = [(FRAME / 2 + offset, inset), (FRAME / 2 - offset, far)]
    return f'<g fill="{color}">' + "".join(
        f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{radius:.1f}"/>' for x, y in points) + "</g>"


def tile(variant, detail):
    dark = variant == "dark"
    accent = PEACH if dark else INK
    glyph = PAPER if dark else INK
    layout = LAYOUTS[detail]
    inset, corner, border = layout["inset"], layout["corner"], layout["border"]
    if dark:
        background = (
            f'<defs><radialGradient id="bg" cx="50%" cy="40%" r="75%"><stop offset="0" stop-color="{CHARCOAL_TOP}"/>'
            f'<stop offset="1" stop-color="{CHARCOAL_BOTTOM}"/></radialGradient>'
            f'<radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="{PEACH}" '
            f'stop-opacity="0.28"/><stop offset="1" stop-color="{PEACH}" stop-opacity="0"/></radialGradient></defs>'
            f'<rect width="{FRAME}" height="{FRAME}" fill="url(#bg)"/>'
            f'<circle cx="512" cy="512" r="400" fill="url(#glow)"/>'
        )
    else:
        background = f'<rect width="{FRAME}" height="{FRAME}" fill="{PAPER}"/>'
    size = FRAME - 2 * inset
    shell = (f'<rect x="{inset}" y="{inset}" width="{size}" height="{size}" rx="{corner}" fill="none" '
             f'stroke="{accent}" stroke-width="{border}"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{FRAME}" height="{FRAME}" viewBox="0 0 {FRAME} {FRAME}" '
            f'data-muppets="no strings attached">'
            f'{background}{shell}{electrons(layout, accent)}{symbol(512, 512, layout["symbol"], glyph)}'
            f'</svg>\n')


def main(out_dir):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for variant in ("dark", "light"):
        for detail in LAYOUTS:
            (out / f"inertlabs-{detail}-{variant}.svg").write_text(tile(variant, detail))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "svg")
