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
- **Image Asset**: [fig_3_9_rad_prototyping_lifecycle.png](file:///Users/arronkianparejas/easylens/docs/figures/assets/fig_3_9_rad_prototyping_lifecycle.png)

```
Figure 3.9
The Customized Rapid Application Development (RAD) Prototyping and Evaluation Lifecycle

Note. Figure 3.9 illustrates the customized Rapid Application Development (RAD) lifecycle model incorporating rapid CAD enclosure modeling, continuous machine learning integration, and iterative usability testing with visually impaired participants.
```

---

### Technical Diagram (Mermaid)

```mermaid
flowchart LR
    subgraph RAD_LIFECYCLE ["EASYLENS CUSTOMIZED RAD LIFECYCLE"]
        direction TB

        P1["Phase 1: Requirements Planning\n• Define pedestrian assistive objectives\n• Map ISO/IEC 25010 & WEAR scale metrics\n• Select low-cost, off-the-shelf hardware (ESP32-CAM)"]

        P2["Phase 2: User Design & Rapid Prototyping\n• Figma accessible wireframes & WCAG AAA tokens\n• Parametric CAD box frame & clip modeling\n• Interactive high-contrast UI swatches"]

        P3["Phase 3: Construction & AI Model Integration\n• 3D printing PLA enclosures & heatsink mounting\n• Flutter core development with Dart Isolates\n• TFLite MobileNetV2 SSD, OCR & Gemma 2B LLM\n• Cloudflare D1/R2 & Firebase synchronization"]

        P4["Phase 4: Cutover & Empirical Evaluation\n• Live walking trials with N=15 visually impaired users\n• Technical evaluations with N=5 expert panel\n• Continuous integration & OTA update release"]
    end

    P1 --> P2
    P2 <--> P3
    P3 <--> P4
    P4 -.->|Iterative Refinements| P2
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
%%{init: {"flowchart": {"wrappingWidth": 260, "nodeSpacing": 30, "rankSpacing": 45}}}%%
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
    BUDDY_OUT["Answers by voice:<br/>Gemma 2B on the phone (English)<br/>or Gemini online (Filipino)"]
    NAV_OUT["Speaks turn-by-turn steps and<br/>alerts the user near each turn (GPS)"]

    COUNT{"Cancelled within<br/>5 seconds?"}
    SOS_CANCEL["SOS cancelled"]
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
    COUNT -->|Yes| SOS_CANCEL
    COUNT -->|No| SOS_SEND
```
