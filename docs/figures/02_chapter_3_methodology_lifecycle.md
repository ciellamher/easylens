# Chapter 3: Research Methodology & Lifecycle Models

---

## Figure 3.1: EasyLens Project Implementation Timeline and Eight-Phase Activity Roadmap

### APA 7th Citation & Metadata
- **Figure Number**: Figure 3.1
- **Figure Title**: *EasyLens Project Implementation Timeline and Eight-Phase Activity Roadmap*
- **Image Asset**: [fig_3_1_timeline_roadmap.png](assets/fig_3_1_timeline_roadmap.png)

```
Figure 3.1
EasyLens Project Implementation Timeline and Eight-Phase Activity Roadmap

Note. Figure 3.1 shows the eight phases of the EasyLens project from December 2025 to September 2026: research and sourcing, hardware prototyping, offline AI model training, mobile app development, cloud services and deployment, user testing and evaluation, documentation and defense, and post-defense revisions. The detailed task breakdown is compiled in Appendix H.
```

The image is the same chart as Figure H.1, drawn by `docs/figures/src/appendix_h_gantt.py`. After redrawing, copy `fig_h_1_gantt_phases.png` to `fig_3_1_timeline_roadmap.png` so the two figures stay identical.

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
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#EEF3FB", "primaryBorderColor": "#4C72B0", "primaryTextColor": "#1A1A1A", "secondaryColor": "#FFF6E5", "tertiaryColor": "#F7F7F7", "lineColor": "#444444", "fontFamily": "arial, sans-serif", "fontSize": "15px", "edgeLabelBackground": "#FFFFFF", "clusterBkg": "#F7F7F7", "clusterBorder": "#9A9A9A", "actorBkg": "#EEF3FB", "actorBorder": "#4C72B0", "actorTextColor": "#1A1A1A", "actorLineColor": "#9A9A9A", "signalColor": "#333333", "signalTextColor": "#1A1A1A", "noteBkgColor": "#F2F2F2", "noteBorderColor": "#9A9A9A", "labelBoxBkgColor": "#F2F2F2", "labelBoxBorderColor": "#9A9A9A", "loopTextColor": "#1A1A1A", "activationBkgColor": "#EEF3FB"}, "flowchart": {"wrappingWidth": 330, "nodeSpacing": 40, "rankSpacing": 55}, "fontFamily": "arial, sans-serif"}}%%
flowchart TD
    BU["<b>1. Business Understanding</b><br/>• Recognize common pedestrian hazards for visually impaired users<br/>• Low-cost wearable: ESP32-CAM glasses connected to a smartphone"]

    DU["<b>2. Data Understanding</b><br/>• Kaggle obstacle dataset (Gobara), 30 classes<br/>• Found duplicate labels (person / Person), severe class imbalance and near-empty 'ghost' classes"]

    DP["<b>3. Data Preparation</b><br/>• Merged person into Person; removed 5 ghost classes (bench, chair, handbag, umbrella, traffic_light) → 24 classes<br/>• Images resized to 224 × 224<br/>• Augmentation: rotation ±20°, zoom 20%, width shift 20%, horizontal flip<br/>• Balanced class weights<br/>• Split: 31,866 train / 4,185 validation / 2,125 test (38,176 images)"]

    M["<b>4. Modeling</b><br/>• MobileNetV2 backbone (ImageNet weights) + Dense 512 → Dense 256 → Softmax (24 classes)<br/>• Four training phases: head only, top 30 layers, then all layers (twice) (Adam, learning rate 5e-4 → 1e-5 → 5e-6 → 1e-7)<br/>• Early stopping and learning-rate reduction on plateau<br/>• Trained in Google Colab (NVIDIA T4 GPU)"]

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
