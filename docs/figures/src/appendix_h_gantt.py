import datetime as dt
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import os
OUT = os.path.join(os.path.dirname(__file__), "..", "assets") + os.sep
plt.rcParams.update({"font.family": "DejaVu Sans"})
D = lambda s: dt.date.fromisoformat(s)
COL = ["#4C72B0", "#8172B3", "#DD8452", "#55A868", "#64B5CD", "#C44E52", "#937860", "#8C8C8C"]

PHASES = [
 ("1. Research and Sourcing",          "2025-12-01", "2026-01-31"),
 ("2. Hardware Prototyping",           "2026-01-15", "2026-03-31"),
 ("3. AI Model Training (offline)",    "2026-03-15", "2026-05-15"),
 ("4. Mobile App Development",         "2026-05-01", "2026-07-15"),
 ("5. Cloud Services and Deployment",  "2026-06-20", "2026-08-23"),
 ("6. User Testing and Evaluation",    "2026-07-01", "2026-08-18"),
 ("7. Documentation and Defense",      "2026-08-01", "2026-09-23"),
 ("8. Post-Defense Revisions",         "2026-09-24", "2026-09-30"),
]

TASKS = [
 (0, "System modeling and architecture",                 "2025-12-01", "2026-01-15"),
 (0, "Hardware sourcing (ESP32-CAM, lens, power bank)",  "2025-12-15", "2026-01-31"),
 (1, "3D-printed PLA clip design and printing",             "2026-01-15", "2026-02-28"),
 (1, "Eyewear fitting and heat management",              "2026-02-15", "2026-03-15"),
 (1, "ESP32 Wi-Fi camera stream testing",                "2026-03-01", "2026-03-31"),
 (2, "Dataset audit and cleaning (30 to 24 classes)",    "2026-03-15", "2026-04-15"),
 (2, "Data augmentation setup",                          "2026-04-01", "2026-04-20"),
 (2, "Phase 1: train new classifier head",               "2026-04-15", "2026-04-25"),
 (2, "Phase 2: unfreeze top 30 layers",                  "2026-04-25", "2026-05-05"),
 (2, "Phases 3–4: fine-tuning and test evaluation",      "2026-05-01", "2026-05-15"),
 (3, "Flutter setup and state management (Provider)",    "2026-05-01", "2026-05-25"),
 (3, "Object detection (SSD MobileNet, bounding boxes)", "2026-05-20", "2026-06-20"),
 (3, "ML Kit text reading, labeling, face recognition",  "2026-06-01", "2026-06-30"),
 (3, "Buddy assistant (Gemma 2B, Gemini, TF-IDF)",       "2026-06-10", "2026-07-15"),
 (3, "Voice (English/Filipino) and vibration feedback",   "2026-06-20", "2026-07-10"),
 (3, "GPS navigation and SOS alerts",                    "2026-06-25", "2026-07-15"),
 (4, "Cloudflare R2 profile photo storage",              "2026-06-20", "2026-07-20"),
 (4, "Firebase Authentication and Firestore",            "2026-06-25", "2026-07-25"),
 (4, "CI/CD pipeline and Docker landing page",           "2026-07-16", "2026-07-25"),
 (4, "App releases v21–v25 (APK/IPA)",                   "2026-08-04", "2026-08-23"),
 (5, "Participant onboarding and informed consent",      "2026-07-01", "2026-07-10"),
 (5, "Walking trials with end-users (N = 15)",           "2026-07-20", "2026-08-04"),
 (5, "WEAR comfort and thermal safety check",            "2026-07-20", "2026-08-04"),
 (5, "ISO/IEC 25010 expert evaluation (N = 5)",          "2026-07-20", "2026-08-08"),
 (5, "Data encoding and Likert analysis",                "2026-08-01", "2026-08-18"),
 (6, "Manuscript writing and APA 7th revisions",         "2026-08-01", "2026-08-27"),
 (6, "Soft copy and deliverables submission",            "2026-08-28", "2026-08-29"),
 (6, "Hard copy submission",                             "2026-09-02", "2026-09-02"),
 (6, "Final defense",                                    "2026-09-23", "2026-09-23"),
 (7, "RA 10173 face-registration consent",               "2026-09-24", "2026-09-27"),
 (7, "Manuscript and figure revisions",                  "2026-09-24", "2026-09-30"),
]

def axis(ax, start="2025-12-01", end="2026-10-01"):
    ax.set_xlim(D(start), D(end))
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
    ax.xaxis.tick_top()
    ax.grid(axis="x", color="#E3E3E3")
    ax.set_axisbelow(True)
    for s in ("right", "bottom", "left"): ax.spines[s].set_visible(False)
    ax.tick_params(axis="y", length=0)

# H.1
fig, ax = plt.subplots(figsize=(11, 4.4), dpi=220)
for i, (name, a, b) in enumerate(PHASES):
    ax.barh(i, (D(b) - D(a)).days, left=D(a), height=0.55, color=COL[i])
ax.set_yticks(range(len(PHASES)), [p[0] for p in PHASES], fontsize=10.5)
ax.invert_yaxis(); axis(ax)
plt.tight_layout(); plt.savefig(OUT + "fig_h_1_gantt_phases.png", facecolor="white"); plt.close()

# H.2
fig, ax = plt.subplots(figsize=(12, 11.5), dpi=200)
labels, y = [], 0
ys = []
for pi, (pname, _, _) in enumerate(PHASES):
    ys.append(("phase", y, pname, pi)); labels.append(pname); y += 1
    for (p, name, a, b) in TASKS:
        if p == pi:
            ys.append(("task", y, name, p, a, b)); labels.append("   " + name); y += 1
for row in ys:
    if row[0] == "phase":
        ax.axhspan(row[1] - 0.5, row[1] + 0.5, color="#F2F2F2", zorder=0)
    else:
        _, yy, name, p, a, b = row
        ax.barh(yy, max((D(b) - D(a)).days, 3), left=D(a), height=0.6, color=COL[p], zorder=2)
ax.set_yticks(range(len(labels)), labels, fontsize=9.5)
for t, row in zip(ax.get_yticklabels(), ys):
    if row[0] == "phase": t.set_fontweight("bold")
ax.set_ylim(len(labels) - 0.5, -0.5); axis(ax)
plt.tight_layout(); plt.savefig(OUT + "fig_h_2_gantt_detailed.png", facecolor="white"); plt.close()
print("ok")
