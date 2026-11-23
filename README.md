<p align="center"><img alt="Inert Labs" src="https://raw.githubusercontent.com/inertlabs/brand/main/logo/png/github-avatar-512.png" width="200" /></p>

# brand

`brand` holds the Inert Labs logo: an element tile whose border is a closed electron shell, with "Il" at its center
and two electrons on the shell. Everything is generated from one script, so the mark can be tweaked and re-rendered
instead of redrawn.

## Rendering

[`logo/gen_logo.py`](https://github.com/inertlabs/brand/blob/main/logo/gen_logo.py) is the one source. Every shape is
drawn geometry, so it renders the same anywhere and needs no fonts. Colors and proportions are the constants at its
top. Render everything with:

```sh
make render
```

That writes:

- `logo/svg/`: the icon and the favicon cut (bolder, for 16–32 px), each in dark and light
- `logo/png/`: 1024 px renders of each, plus `github-avatar-512.png`, `play-developer-icon-512.png`,
  `apple-touch-icon-180.png`, and `favicon-16/32/48.png`

Rendering needs macOS (Quick Look rasterizes the SVG) and ImageMagick.

## Colors

|                     | Dark                  | Light     |
|---------------------|-----------------------|-----------|
| Background          | `#262C33` → `#14181C` | `#F4EFE6` |
| Shell and electrons | `#FFB38A`             | `#1E2328` |
| Symbol              | `#F4EFE6`             | `#1E2328` |
