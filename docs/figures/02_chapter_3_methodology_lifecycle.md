# Chapter 3: Research Methodology & Lifecycle Models

---

## Figure 3.1: EasyLens Project Implementation Timeline and Seven-Phase Activity Roadmap

### APA 7th Citation & Metadata
- **Figure Number**: Figure 3.1
- **Figure Title**: *EasyLens Project Implementation Timeline and Seven-Phase Activity Roadmap*
- **Manuscript Page**: 42
- **PDF Page**: 49
- **Image Asset**: [fig_3_1_timeline_roadmap.png](file:///Users/arronkianparejas/easylens/docs/figures/assets/fig_3_1_timeline_roadmap.png)

```
Figure 3.1
EasyLens Project Implementation Timeline and Seven-Phase Activity Roadmap

Note. Figure 3.1 represents the chronological Gantt chart mapping out the hardware prototyping, machine learning engineering, mobile software construction, empirical walking evaluations, and thesis document finalization phases executed between December 2025 and August 2026.
```

---

### Technical Diagram (Mermaid)

```mermaid
gantt
    title EasyLens Seven-Phase Implementation Roadmap (Dec 2025 – Aug 2026)
    dateFormat  YYYY-MM-DD
    axisFormat  %b %Y

    section Phase 1: Research & Hardware
    Literature Review & Architecture Sourcing       :p1, 2025-12-01, 2026-01-15
    Component Procurement (ESP32-CAM, Lens, Battery) :p1b, 2025-12-15, 2026-01-31

    section Phase 2: Hardware & Enclosure
    Parametric CAD 3D Box Frame Design              :p2, 2026-01-15, 2026-02-28
    PLA 3D Printing, Heatsink & Frame Assembly      :p2b, 2026-02-15, 2026-03-31

    section Phase 3: AI Model Training
    24-Class COCO Cleaning & Spatial Augmentation   :p3, 2026-03-15, 2026-04-30
    4-Phase MobileNetV2 Transfer Learning & TFLite  :p3b, 2026-04-01, 2026-05-15

    section Phase 4: Flutter Mobile App
    Flutter Core Architecture & Dart Isolates       :p4, 2026-05-01, 2026-06-15
    ML Kit OCR, Gemma 2B & Spatial Audio/Haptics    :p4b, 2026-05-15, 2026-06-30

    section Phase 5: Cloud & Backend Sync
    Cloudflare D1 SQL Telemetry & R2 Storage Sync   :p5, 2026-06-15, 2026-07-15
    Firebase Authentication & CI/CD Pipeline Setup  :p5b, 2026-06-20, 2026-07-20

    section Phase 6: Empirical User Testing
    Visually Impaired Walking Trials (N=15)         :p6, 2026-07-01, 2026-08-10
    Technical Expert Quality Evaluations (N=5)      :p6b, 2026-07-15, 2026-08-15

    section Phase 7: Document Polish & Release
    Empirical Data Analysis & WCAG AAA Verification :p7, 2026-08-01, 2026-08-20
    Final Manuscript Defense & Open-Source Release  :p7b, 2026-08-15, 2026-08-28
```

---

## Figure 3.2: The Six-Phase Cross-Industry Standard Process for Data Mining (CRISP-DM) Lifecycle for EasyLens AI Development

### APA 7th Citation & Metadata
- **Figure Number**: Figure 3.2
- **Figure Title**: *The Six-Phase Cross-Industry Standard Process for Data Mining (CRISP-DM) Lifecycle for EasyLens AI Development*
- **Manuscript Page**: 43
- **PDF Page**: 50
- **Image Asset**: [fig_crisp_dm_lifecycle.png](assets/fig_crisp_dm_lifecycle.png)

```
Figure 3.2
The Six-Phase Cross-Industry Standard Process for Data Mining (CRISP-DM) Lifecycle for EasyLens AI Development

Note. Figure 3.2 shows the six CRISP-DM phases followed to develop the custom 24-class MobileNetV2 classifier, from business and data understanding through data preparation, modeling and evaluation. The deployment phase records that the final model was saved but not yet integrated into the Buddy application.
```

---

### Technical Diagram (Mermaid)

```mermaid
%%{init: {"flowchart": {"wrappingWidth": 330, "nodeSpacing": 40, "rankSpacing": 55}}}%%
flowchart TD
    BU["<b>1. Business Understanding</b><br/>• Recognize common pedestrian hazards for visually impaired users<br/>• Low-cost wearable: ESP32-CAM glasses connected to a smartphone"]

    DU["<b>2. Data Understanding</b><br/>• Kaggle obstacle dataset (Gobara), 30 classes<br/>• Found duplicate labels (person / Person), severe class imbalance and near-empty 'ghost' classes"]

    DP["<b>3. Data Preparation</b><br/>• Merged person into Person; removed 5 ghost classes (bench, chair, handbag, umbrella, traffic_light) → 24 classes<br/>• Images resized to 224 × 224<br/>• Augmentation: rotation ±20°, zoom 20%, width shift 20%, horizontal flip<br/>• Balanced class weights<br/>• Split: 31,866 train / 4,185 validation / 2,125 test (38,176 images)"]

    M["<b>4. Modeling</b><br/>• MobileNetV2 backbone (ImageNet weights) + Dense 512 → Dense 256 → Softmax (24 classes)<br/>• Four training phases, unfreezing progressively more layers (Adam, learning rate 5e-4 → 1e-5 → 5e-6 → 1e-7)<br/>• Early stopping and learning-rate reduction on plateau<br/>• Trained in Google Colab (NVIDIA T4 GPU)"]

    EV["<b>5. Evaluation</b> (held-out test set, 2,125 images)<br/>• Top-1, Top-2 and Top-3 accuracy<br/>• Balanced accuracy<br/>• Weighted precision, recall and F1-score<br/>• Inference time (GPU, offline)"]

    DEP["<b>6. Deployment</b><br/>• Final model saved in Keras format (.keras)<br/>• Not yet converted to TFLite or integrated into Buddy (see Recommendations)"]

    BU <--> DU
    DU --> DP
    DP <--> M
    M --> EV
    EV --> DEP
    EV -.->|Refine when results fall short| BU
```

---

### Methodological Narrative & Manuscript Context

The research follows the standardized CRISP-DM framework adapted for resource-constrained edge-AI mobile deployment:
1. **Iterative Alignment**: Data understanding and preparation required extensive cleansing to prevent class imbalance from skewing obstacle detection on mobile hardware.
2. **Deployment Status**: The final Phase 4 model was saved in Keras format after training in Google Colab. It has not been converted to TensorFlow Lite or integrated into the mobile application; live detection in Buddy uses the COCO-pretrained SSD MobileNet model and Google ML Kit.
