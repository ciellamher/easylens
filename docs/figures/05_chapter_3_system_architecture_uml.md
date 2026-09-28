# Chapter 3: System Architecture & UML Sequence Diagram

---

## Figure 3.11: EasyLens System Architecture and Detailed UML Sequence Diagram

### APA 7th Citation & Metadata
- **Figure Number**: Figure 3.11
- **Figure Title**: *EasyLens System Architecture and Detailed UML Sequence Diagram*
- **Manuscript Page**: 102
- **PDF Page**: 109
- **Image Asset**: [fig_system_sequence_diagram.png](assets/fig_system_sequence_diagram.png)

```
Figure 3.11
EasyLens System Architecture and Detailed UML Sequence Diagram

Note. Figure 3.11 shows the EasyLens system architecture as a unified modeling language (UML) sequence diagram: connecting the smart glasses over their local Wi-Fi network, the Navigation-mode hazard-warning loop using Google ML Kit on the phone, Buddy's question-and-answer flow (Gemma 2B on the phone in Local AI mode, the default, or Google Gemini in online mode and for some Filipino questions), and the Emergency SOS flow.
```

---

### Technical Diagram (Mermaid Sequence Diagram)

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#EEF3FB", "primaryBorderColor": "#4C72B0", "primaryTextColor": "#1A1A1A", "secondaryColor": "#FFF6E5", "tertiaryColor": "#F7F7F7", "lineColor": "#444444", "fontFamily": "arial, sans-serif", "fontSize": "15px", "edgeLabelBackground": "#FFFFFF", "clusterBkg": "#F7F7F7", "clusterBorder": "#9A9A9A", "actorBkg": "#EEF3FB", "actorBorder": "#4C72B0", "actorTextColor": "#1A1A1A", "actorLineColor": "#9A9A9A", "signalColor": "#333333", "signalTextColor": "#1A1A1A", "noteBkgColor": "#F2F2F2", "noteBorderColor": "#9A9A9A", "labelBoxBkgColor": "#F2F2F2", "labelBoxBorderColor": "#9A9A9A", "loopTextColor": "#1A1A1A", "activationBkgColor": "#EEF3FB"}, "sequence": {"messageFontFamily": "arial, sans-serif", "actorFontFamily": "arial, sans-serif", "noteFontFamily": "arial, sans-serif", "mirrorActors": false, "messageFontSize": 15, "actorFontSize": 15, "noteFontSize": 15, "boxMargin": 8}, "fontFamily": "arial, sans-serif"}}%%
sequenceDiagram
    actor User as User
    participant Glasses as Smart Glasses (ESP32-CAM)
    participant App as Buddy App (smartphone)
    participant Vision as Google ML Kit (on phone)
    participant Output as Voice & Vibration
    participant Gemini as Google Gemini (cloud)
    participant Contacts as Emergency Contacts

    rect rgb(243, 247, 253)
        note over User, App: Connecting to the glasses
        Glasses->>Glasses: Start "EasyLens-Camera" Wi-Fi network
        User->>App: Join the Wi-Fi in phone settings, then tap Connect
        App->>Glasses: Request video stream (192.168.4.1:81/stream)
        Glasses-->>App: Send continuous JPEG frames
    end

    rect rgb(244, 250, 245)
        note over Glasses, Output: Navigation mode (hazard warnings)
        loop Every ~0.5 seconds
            Glasses->>App: Latest camera frame
            App->>Vision: Detect objects and label the image
            Vision-->>App: Bounding boxes and labels
            alt Obstacle centered and close, or hazard recognized
                App->>Output: Warning (e.g., "Stop immediately", "Obstacle ahead, step to your left")
                Output-->>User: Spoken warning + vibration
            else Path clear
                App->>App: Keep scanning
            end
        end
    end

    rect rgb(253, 249, 240)
        note over User, Gemini: Talking to Buddy
        User->>App: Spoken question
        App->>App: Speech-to-text and knowledge-base search (TF-IDF)
        alt Local AI mode (default)
            App->>App: Answer with Gemma 2B on the phone (offline)
        else Online mode, or some Filipino questions
            App->>Gemini: Question with context
            Gemini-->>App: Answer
        end
        App->>Output: Speak the answer
        Output-->>User: Spoken answer
    end

    rect rgb(252, 243, 243)
        note over User, Contacts: Emergency SOS
        User->>App: Press SOS
        App-->>User: 5-second countdown (tap Cancel to stop)
        opt Not cancelled
            App->>App: Get GPS location
            App->>Contacts: SMS with Google Maps location link
            App-->>User: "SOS alert sent"
        end
    end
```

---

### Architectural Characteristics

1. **Dart Isolate Concurrency**: Offloads raw frame resizing, tensor formatting, and TFLite execution to background threads, guaranteeing that the Flutter UI thread renders at a consistent 60 FPS without frame stutter.
2. **Dual-Tier Large Language Model Orchestration**: Ensures complete offline functionality via the local Gemma-IT 2B INT4 quantized LLM while providing high-quality contextual reasoning via Gemini 3.6 Flash Low when network access is available.
3. **Priority Audio Management**: Audio alerts operate on a strict priority queue where immediate collision and hazard warnings instantly preempt background voice dialogue or navigation prompts.
