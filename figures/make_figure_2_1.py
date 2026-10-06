"""Figure 2.1 - Input-Process-Output conceptual framework of EasyLens.

Reproducible build:  python3 figures/make_figure_2_1.py
Output:              figures/figure_2_1.png  (300 dpi, 6.0 in = 1800 px wide)

All layout is done in inches on a 6.0 in wide canvas, so font sizes in
points are the true printed sizes (body 11 pt, stage titles 12 pt bold).
Text is word-wrapped by measuring rendered widths; shapes grow to fit.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle

OUT = Path(__file__).resolve().parent / "figure_2_1.png"

DPI = 300
FIG_W = 6.0            # inches (1800 px)
MAX_H = 8.0            # inches
BODY_PT = 11
TITLE_PT = 12
LINE_GAP = 1.2         # line height as a multiple of font size
BULLET_GAP = 0.04      # extra space between bullets (in)
TITLE_GAP = 0.16       # space between stage title and first bullet (in)

MARGIN_X = 0.08        # canvas edge to widest shape point (in)
MARGIN_Y = 0.06        # canvas top/bottom to shape (in)
SLANT = 0.25           # parallelogram skew and hexagon point depth (in)
PAD_X = 0.12           # min gap between text and slanted/vertical border (in)
PAD_Y = 0.13           # gap between text and top/bottom border (in)
ARROW_GAP = 0.32       # vertical space between stages (in)
LINE_W = 1.4           # outline width (pt)
ARROW_W = 1.8          # arrow shaft width (pt)
CORNER = 0.08          # rectangle corner radius (in)
BODY_FILL = "#F3F3F3"  # light gray stage background (prints in grayscale)
BAND_FILL = "#D6D6D6"  # darker gray title band


def pick_serif():
    names = {f.name for f in font_manager.fontManager.ttflist}
    for name in ("Times New Roman", "Liberation Serif"):
        if name in names:
            return name
    raise SystemExit("Neither Times New Roman nor Liberation Serif is installed.")


STAGES = [
    ("parallelogram", "INPUT", [
        "Live video (30 fps) from the smart glasses or the phone camera",
        "User's GPS location",
        "Voice prompts through the phone's microphone",
        "Stored data: settings, contacts, registered faces, journals",
    ]),
    ("rectangle", "PROCESS (Buddy Application on the Smartphone)", [
        "Hazard detection: ML Kit with left/center/right steering (Navigation "
        "mode); SSD\u00a0MobileNet (Object Detection mode)",
        "Text reading (OCR) and face recognition",
        "Buddy assistant: Gemma 2B (Local AI) or Gemini (online), with TF-IDF "
        "search of the knowledge base and journals",
        "GPS navigation with online route planning",
    ]),
    ("parallelogram", "OUTPUT", [
        "Spoken alerts and guidance in English and Filipino",
        "Vibration alerts and on-screen bounding boxes",
        "SOS text messages to emergency contacts",
        "Daily journals on the phone; profile data in Firebase",
    ]),
    ("hexagon", "EVALUATION (Three Measured Variables)", [
        "AI performance: Top-1 to Top-3 accuracy and inference time of the "
        "24-class\u00a0MobileNetV2 model (offline evaluation)",
        "Usability outcome: end-user checklist (n = 15)",
        "System quality: IT/AI expert checklist (n = 5)",
    ]),
]


class Measurer:
    def __init__(self, fig, family):
        self.r = fig.canvas.get_renderer()
        self.family = family

    def width_in(self, s, size, bold=False):
        prop = font_manager.FontProperties(
            family=self.family, size=size, weight="bold" if bold else "normal")
        w, _, _ = self.r.get_text_width_height_descent(s, prop, ismath=False)
        return w / DPI

    def wrap(self, text, size, max_w):
        lines, cur = [], ""
        # Split on plain spaces only so non-breaking spaces keep names together.
        for word in text.split(" "):
            trial = f"{cur} {word}".strip()
            if cur and self.width_in(trial, size) > max_w:
                lines.append(cur)
                cur = word
            else:
                cur = trial
        lines.append(cur)
        return lines


def shape_points(kind, left, right, y0, y1):
    s = SLANT
    if kind == "parallelogram":
        return [(left, y0), (right - s, y0), (right, y1), (left + s, y1)]
    if kind == "hexagon":
        ym = (y0 + y1) / 2
        return [(left + s, y0), (right - s, y0), (right, ym),
                (right - s, y1), (left + s, y1), (left, ym)]
    return [(left, y0), (right, y0), (right, y1), (left, y1)]


def shape_patch(kind, left, right, y0, y1, **kw):
    if kind == "rectangle":
        return FancyBboxPatch((left, y0), right - left, y1 - y0,
                              boxstyle=f"round,pad=0,rounding_size={CORNER}",
                              **kw)
    return Polygon(shape_points(kind, left, right, y0, y1), closed=True,
                   joinstyle="miter", **kw)


def main():
    family = pick_serif()
    plt.rcParams["font.family"] = family

    left, right = MARGIN_X, FIG_W - MARGIN_X
    # Text must clear the slanted edges at their innermost point.
    text_left = left + SLANT + PAD_X
    text_right = right - SLANT - PAD_X
    text_w = text_right - text_left

    probe = plt.figure(figsize=(FIG_W, 1), dpi=DPI)
    m = Measurer(probe, family)
    bullet = "•"
    indent = m.width_in(bullet + "  ", BODY_PT)

    body_lh = BODY_PT * LINE_GAP / 72
    title_lh = TITLE_PT * LINE_GAP / 72

    # Lay out each stage: wrapped lines and the resulting box height.
    blocks = []
    for kind, title, bullets in STAGES:
        assert m.width_in(title, TITLE_PT, bold=True) <= text_w, title
        wrapped = [m.wrap(b, BODY_PT, text_w - indent) for b in bullets]
        n_lines = sum(len(w) for w in wrapped)
        text_h = (title_lh + TITLE_GAP + n_lines * body_lh
                  + BULLET_GAP * (len(bullets) - 1))
        blocks.append((kind, title, wrapped, text_h + 2 * PAD_Y))
    plt.close(probe)

    total_h = (2 * MARGIN_Y + sum(b[3] for b in blocks)
               + ARROW_GAP * (len(blocks) - 1))
    fig_h = round(total_h * DPI) / DPI
    if fig_h > MAX_H:
        raise SystemExit(f"Figure would be {fig_h:.2f} in tall (> {MAX_H} in).")

    fig = plt.figure(figsize=(FIG_W, fig_h), dpi=DPI, facecolor="white")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, FIG_W)
    ax.set_ylim(0, fig_h)
    ax.axis("off")

    cx = FIG_W / 2
    y_top = fig_h - MARGIN_Y
    edges = []
    for kind, title, wrapped, box_h in blocks:
        y1, y0 = y_top, y_top - box_h
        # Fill, then a title band clipped to the shape, then the outline on top.
        body = shape_patch(kind, left, right, y0, y1, facecolor=BODY_FILL,
                           edgecolor="none")
        ax.add_patch(body)
        band_bottom = y1 - PAD_Y - title_lh - TITLE_GAP / 2
        band = Rectangle((left, band_bottom), right - left, y1 - band_bottom,
                         facecolor=BAND_FILL, edgecolor="none")
        ax.add_patch(band)
        band.set_clip_path(body)
        rule, = ax.plot([left, right], [band_bottom] * 2, color="black",
                        linewidth=0.6)
        rule.set_clip_path(body)
        ax.add_patch(shape_patch(kind, left, right, y0, y1, fill=False,
                                 edgecolor="black", linewidth=LINE_W))

        # Baselines: offset each line by roughly its ascent (0.8 of line).
        y = y1 - PAD_Y - title_lh * 0.8
        ax.text(cx, y, title, ha="center", va="baseline",
                fontsize=TITLE_PT, fontweight="bold")
        y -= title_lh * 0.2 + TITLE_GAP + body_lh * 0.8
        for i, lines in enumerate(wrapped):
            ax.text(text_left, y, bullet, ha="left", va="baseline",
                    fontsize=BODY_PT)
            for line in lines:
                ax.text(text_left + indent, y, line, ha="left",
                        va="baseline", fontsize=BODY_PT)
                y -= body_lh
            if i < len(wrapped) - 1:
                y -= BULLET_GAP
        edges.append((y0, y1))
        y_top = y0 - ARROW_GAP

    for (bottom, _), (_, next_top) in zip(edges, edges[1:]):
        ax.add_patch(FancyArrowPatch(
            (cx, bottom), (cx, next_top), arrowstyle="-|>",
            mutation_scale=18, color="black", linewidth=ARROW_W,
            shrinkA=0, shrinkB=0))

    fig.savefig(OUT, dpi=DPI, facecolor="white")
    plt.close(fig)
    try:  # flatten to RGB for print workflows; keep the 300 dpi tag
        from PIL import Image
        Image.open(OUT).convert("RGB").save(OUT, dpi=(DPI, DPI))
    except ImportError:
        pass
    print(f"Saved {OUT} ({FIG_W:.2f} x {fig_h:.2f} in, "
          f"{round(FIG_W * DPI)} x {round(fig_h * DPI)} px, font: {family})")


if __name__ == "__main__":
    main()
