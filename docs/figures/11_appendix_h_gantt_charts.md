# Appendix H: Gantt Chart and Project Timeline

Both charts were drawn with matplotlib. Dates before July 2026 are the research team's schedule. Dates from July 2026 onward are consistent with the project's Git history and GitHub Releases: the app repository begins on July 7, 2026; the CI/CD pipeline was added on July 16 and the Docker landing page on July 25; releases v21–v25 were published between August 4 and August 23; and the RA 10173 face-registration consent was merged on September 27.

To redraw the charts, run `python3 docs/figures/src/appendix_h_gantt.py`.

---

## Figure H.1: Simplified Gantt Chart (Phase-Level Overview)

### APA 7th Citation & Metadata
- **Figure Number**: Figure H.1
- **Figure Title**: *Simplified Gantt Chart (Phase-Level Overview)*
- **Image Asset**: [fig_h_1_gantt_phases.png](assets/fig_h_1_gantt_phases.png)

```
Figure H.1
Simplified Gantt Chart (Phase-Level Overview)

Note. Figure H.1 summarizes the eight phases of the EasyLens project from December 2025 to September 2026, from research and hardware sourcing through the post-defense revisions. The final defense was held on September 23, 2026.
```

---

## Figure H.2: Detailed Gantt Chart (Task and Deliverable Breakdown)

### APA 7th Citation & Metadata
- **Figure Number**: Figure H.2
- **Figure Title**: *Detailed Gantt Chart (Task and Deliverable Breakdown)*
- **Image Asset**: [fig_h_2_gantt_detailed.png](assets/fig_h_2_gantt_detailed.png)

```
Figure H.2
Detailed Gantt Chart (Task and Deliverable Breakdown)

Note. Figure H.2 breaks the eight phases into thirty tasks. The custom MobileNetV2 classifier was trained offline in Google Colab and was not converted to TFLite or added to the app; live detection in the app uses Google ML Kit and a COCO-pretrained SSD MobileNet model.
```
