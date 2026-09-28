# Chapter 3: Interface Design, RAD Lifecycle & User Journey Flowcharts

---

## Figure 3.7: Side-by-Side Interface Layout of the EasyLens Default Light Theme and High-Contrast AMOLED Black Theme

### APA 7th Citation & Metadata
- **Figure Number**: Figure 3.7
- **Figure Title**: *Side-by-Side Interface Layout of the EasyLens Default Light Theme and High-Contrast AMOLED Black Theme*
- **Manuscript Page**: 67
- **PDF Page**: 74
- **Image Asset**: [fig_3_7_theme_comparison_layout.png](file:///Users/arronkianparejas/easylens/docs/figures/assets/fig_3_7_theme_comparison_layout.png)

```
Figure 3.7
Side-by-Side Interface Layout of the EasyLens Default Light Theme and High-Contrast AMOLED Black Theme

Note. Figure 3.7 illustrates the side-by-side interface layout comparing the default clean light accessibility theme with the high-contrast AMOLED black theme engineered to maximize contrast ratios and reduce photophobia for low-vision users.
```

---

### Contrast Ratios & Color Specification Table

| Interface Element | Default Light Theme Hex | High-Contrast AMOLED Black Hex | Contrast Ratio (vs. Canvas) | WCAG 2.2 Level |
| :--- | :---: | :---: | :---: | :---: |
| **Canvas Background** | `#FFFFFF` | `#000000` | — | Base |
| **Primary Typography** | `#1A1A1A` | `#FFFFFF` | **21.00:1** | AAA (Pass) |
| **Warning / Hazard Highlight** | `#D32F2F` | `#E6E600` (Yellow) | **16.51:1** | AAA (Pass) |
| **Success / Navigation Arrow** | `#2E7D32` | `#33CC33` (Green) | **10.37:1** | AAA (Pass) |
| **Card Surface Border** | `#E0E0E0` | `#FCFCFC` | **16.49:1** | AAA (Pass) |

---

## Figure 3.9: The Customized Rapid Application Development (RAD) Prototyping and Evaluation Lifecycle

### APA 7th Citation & Metadata
- **Figure Number**: Figure 3.9
- **Figure Title**: *The Customized Rapid Application Development (RAD) Prototyping and Evaluation Lifecycle*
- **Manuscript Page**: 98
- **PDF Page**: 105
- **Image Asset**: [fig_rad_lifecycle.png](assets/fig_rad_lifecycle.png)

```
Figure 3.9
The Customized Rapid Application Development (RAD) Prototyping and Evaluation Lifecycle

Note. Figure 3.9 shows the customized Rapid Application Development (RAD) lifecycle: requirements planning, user design, construction and cutover/evaluation, with iterative prototyping between design and construction and refinements fed back from evaluation.
```

---

### Technical Diagram (Mermaid)

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#EEF3FB", "primaryBorderColor": "#4C72B0", "primaryTextColor": "#1A1A1A", "secondaryColor": "#FFF6E5", "tertiaryColor": "#F7F7F7", "lineColor": "#444444", "fontFamily": "arial, sans-serif", "fontSize": "15px", "edgeLabelBackground": "#FFFFFF", "clusterBkg": "#F7F7F7", "clusterBorder": "#9A9A9A", "actorBkg": "#EEF3FB", "actorBorder": "#4C72B0", "actorTextColor": "#1A1A1A", "actorLineColor": "#9A9A9A", "signalColor": "#333333", "signalTextColor": "#1A1A1A", "noteBkgColor": "#F2F2F2", "noteBorderColor": "#9A9A9A", "labelBoxBkgColor": "#F2F2F2", "labelBoxBorderColor": "#9A9A9A", "loopTextColor": "#1A1A1A", "activationBkgColor": "#EEF3FB"}, "flowchart": {"wrappingWidth": 460, "nodeSpacing": 45, "rankSpacing": 60}, "fontFamily": "arial, sans-serif"}}%%
flowchart TB
    P1["<b>Phase 1: Requirements Planning</b><br/>• Define assistive goals for visually impaired pedestrians<br/>• Set evaluation criteria (usability and system quality)<br/>• Select low-cost hardware: ESP32-CAM glasses and a smartphone"]

    P2["<b>Phase 2: User Design</b><br/>• Voice-first, accessible app screens<br/>• Large text and high-contrast themes<br/>• Smart-glasses enclosure design"]

    P3["<b>Phase 3: Construction</b><br/>• Flutter app (Buddy) and ESP32-CAM Wi-Fi video stream<br/>• Hazard detection: COCO-pretrained SSD MobileNet and Google ML Kit<br/>• Text reading, face recognition and Buddy assistant (Gemma 2B / Gemini)<br/>• Custom MobileNetV2 classifier trained in parallel (CRISP-DM)"]

    P4["<b>Phase 4: Cutover and Evaluation</b><br/>• End-user testing (n = 15)<br/>• Expert evaluation (n = 5)<br/>• Fixes released as new app versions"]

    P1 --> P2
    P2 <-->|Iterative prototyping| P3
    P3 --> P4
    P4 -.->|Refinements| P2
```

---

## Figure 3.10: EasyLens Simplified User Journey and System Interaction Flowchart

### APA 7th Citation & Metadata
- **Figure Number**: Figure 3.10
- **Figure Title**: *EasyLens Simplified User Journey and System Interaction Flowchart*
- **Manuscript Page**: 100
- **PDF Page**: 107
- **Image Asset**: [fig_user_journey_flowchart.png](assets/fig_user_journey_flowchart.png)

```
Figure 3.10
EasyLens Simplified User Journey and System Interaction Flowchart

Note. Figure 3.10 shows the simplified user journey in EasyLens: connecting the smart glasses, choosing a feature by voice or touch, and what each feature does, including the Navigation-mode hazard warnings, Buddy's spoken answers, turn-by-turn walking navigation and the Emergency SOS countdown.
```

---

### Technical Diagram (Mermaid)

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#EEF3FB", "primaryBorderColor": "#4C72B0", "primaryTextColor": "#1A1A1A", "secondaryColor": "#FFF6E5", "tertiaryColor": "#F7F7F7", "lineColor": "#444444", "fontFamily": "arial, sans-serif", "fontSize": "15px", "edgeLabelBackground": "#FFFFFF", "clusterBkg": "#F7F7F7", "clusterBorder": "#9A9A9A", "actorBkg": "#EEF3FB", "actorBorder": "#4C72B0", "actorTextColor": "#1A1A1A", "actorLineColor": "#9A9A9A", "signalColor": "#333333", "signalTextColor": "#1A1A1A", "noteBkgColor": "#F2F2F2", "noteBorderColor": "#9A9A9A", "labelBoxBkgColor": "#F2F2F2", "labelBoxBorderColor": "#9A9A9A", "loopTextColor": "#1A1A1A", "activationBkgColor": "#EEF3FB"}, "flowchart": {"wrappingWidth": 260, "nodeSpacing": 30, "rankSpacing": 45}, "fontFamily": "arial, sans-serif"}}%%
flowchart TD
    START(["User turns on the smart glasses and opens Buddy"])
    WIFI["Join the 'EasyLens-Camera' Wi-Fi in phone settings, then tap Connect<br/>(the phone camera is used if the glasses are not connected)"]
    DASH["Dashboard: time-of-day greeting and voice prompt"]
    CHOICE{"User chooses a feature<br/>by voice or touch"}

    CAM["Smart Glasses camera<br/>(Navigation mode)"]
    OCR["Text Reader"]
    BUDDY["Talk to Buddy"]
    NAV["Walking Navigation"]
    SOS["Emergency SOS"]

    DETECT["Google ML Kit detects objects and labels each frame"]
    HAZ{"Obstacle or hazard<br/>in the path?"}
    STOP["Very close and centered:<br/>'Stop immediately' + strong vibration"]
    AVOID["Close and centered:<br/>'Obstacle ahead, step to your left/right' + vibration"]
    WARN["Hazard recognized (e.g., vehicle, stairs, fire):<br/>spoken warning"]
    CLEAR["Path clear:<br/>no warning"]
    REPEAT(["Repeat for the next frame"])

    OCR_OUT["Reads the text aloud<br/>(English / Filipino)"]
    BUDDY_OUT["Answers by voice:<br/>Gemma 2B on the phone (Local AI mode, default)<br/>or Google Gemini (online mode, and some Filipino questions)"]
    NAV_OUT["Speaks turn-by-turn steps and<br/>alerts the user near each turn (GPS)"]

    COUNT["5-second countdown<br/>(tap Cancel to stop the alert)"]
    SOS_SEND["SMS with Google Maps location link<br/>sent to emergency contacts"]

    START --> WIFI --> DASH --> CHOICE
    CHOICE --> CAM
    CHOICE --> OCR
    CHOICE --> BUDDY
    CHOICE --> NAV
    CHOICE --> SOS

    CAM --> DETECT --> HAZ
    HAZ -->|Yes| STOP
    HAZ -->|Yes| AVOID
    HAZ -->|Yes| WARN
    HAZ -->|No| CLEAR
    STOP --> REPEAT
    AVOID --> REPEAT
    WARN --> REPEAT
    CLEAR --> REPEAT

    OCR --> OCR_OUT
    BUDDY --> BUDDY_OUT
    NAV --> NAV_OUT

    SOS --> COUNT
    COUNT -->|Not cancelled| SOS_SEND

    classDef decision fill:#FFF6E5,stroke:#DD8452,color:#1A1A1A
    classDef terminal fill:#F2F2F2,stroke:#555555,color:#1A1A1A
    class CHOICE,HAZ decision
    class START,REPEAT terminal
```
