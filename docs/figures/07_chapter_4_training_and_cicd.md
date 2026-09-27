# Chapter 4: Model Training, CI/CD Pipeline & Over-The-Air Update Architecture

---

## Figure 4.1: The Multi-Phase Transfer Learning and Unfreezing Workflow for the MobileNetV2 Classifier

### APA 7th Citation & Metadata
- **Figure Number**: Figure 4.1
- **Figure Title**: *The Multi-Phase Transfer Learning and Unfreezing Workflow for the MobileNetV2 Classifier*
- **Manuscript Page**: 122
- **PDF Page**: 130
- **Image Asset**: [fig_transfer_learning_workflow.png](assets/fig_transfer_learning_workflow.png)

```
Figure 4.1
The Multi-Phase Transfer Learning and Unfreezing Workflow for the MobileNetV2 Classifier

Note. Figure 4.1 shows the four-phase transfer learning workflow used in Google Colab to train the custom 24-class MobileNetV2 image classifier, from training a new classifier head on a frozen ImageNet backbone to fine-tuning all layers at very low learning rates, followed by evaluation on the held-out test set. The final model was saved in Keras format; it was not converted to TFLite or integrated into Buddy.
```

---

### Technical Diagram (Mermaid Flowchart)

```mermaid
%%{init: {"flowchart": {"wrappingWidth": 420, "nodeSpacing": 30, "rankSpacing": 40}}}%%
flowchart TD
    BASE["<b>Starting model</b><br/>MobileNetV2 backbone with ImageNet weights (224 × 224 input)<br/>+ new classifier head: Dense 512 → Dropout 0.5 → Dense 256 → Dropout 0.3 → Softmax (24 classes)<br/>Balanced class weights in every phase"]

    P1["<b>Phase 1: Train the new head</b><br/>Backbone fully frozen<br/>Adam, learning rate 5e-4 · ran 15 epochs (maximum 15)"]

    P2["<b>Phase 2: Unfreeze the top 30 backbone layers</b><br/>Adam, learning rate 1e-5 · stopped early after 8 epochs (maximum 50)"]

    P3["<b>Phase 3: Unfreeze all layers</b><br/>Adam, learning rate 5e-6 · maximum 150 epochs (epoch count not recorded)"]

    P4["<b>Phase 4: Continue from the Phase 3 model</b><br/>All layers, Adam, learning rate 1e-7 · stopped early after 21 epochs (maximum 200)"]

    EVAL["<b>Final evaluation</b> (held-out test set, 2,125 images)<br/>Top-1/2/3 accuracy, balanced accuracy, weighted precision, recall and F1-score"]

    SAVE["<b>Output</b><br/>Saved in Keras format (.keras)<br/>Not converted to TFLite or integrated into Buddy"]

    BASE --> P1 --> P2 --> P3 --> P4 --> EVAL --> SAVE
```

---

## Figure 4.2: EasyLens Automated CI/CD Codebase Analysis and Deployment Pipeline Flowchart

### APA 7th Citation & Metadata
- **Figure Number**: Figure 4.2
- **Figure Title**: *EasyLens Automated CI/CD Codebase Analysis and Deployment Pipeline Flowchart*
- **Manuscript Page**: 126
- **PDF Page**: 134
- **Image Asset**: [fig_4_2_cicd_pipeline_flowchart.png](file:///Users/arronkianparejas/easylens/docs/figures/assets/fig_4_2_cicd_pipeline_flowchart.png)

```
Figure 4.2
EasyLens Automated CI/CD Codebase Analysis and Deployment Pipeline Flowchart

Note. Figure 4.2 outlines the automated continuous integration and continuous deployment (CI/CD) pipeline built using GitHub Actions, detailing the static code analysis, native testing, containerized runner compilation, and automated artifact release channels.
```

---

### Technical Diagram (Mermaid Flowchart)

```mermaid
flowchart TD
    DEV_PUSH["Developer Pushes Commit to 'main' Branch"] --> GH_TRIGGER["GitHub Actions Webhook Triggers CI Workflow"]
    
    subgraph STAGE1 ["Stage 1: Code Quality & Static Analysis"]
        direction TB
        SETUP["Setup Runner: Ubuntu Environment + Java 17 + Flutter SDK"]
        PUB["Fetch Dependencies: 'flutter pub get'"]
        LINT["Static Code Linting: 'flutter analyze' (Zero Errors Threshold)"]
    end

    subgraph STAGE2 ["Stage 2: Native Automated Testing"]
        direction TB
        UNIT["Unit & Widget Testing: 'flutter test --coverage'"]
        ASSERT["Assert Test Passes & State Management Isolation"]
    end

    subgraph STAGE3 ["Stage 3: Multi-Architecture Build & Containerization"]
        direction TB
        APK["Compile Release FAT APK ('flutter build apk --release')\n(Bundling TFLite, ML Kit & INT4 Model Weights)"]
        IPA["Compile iOS Release Bundle ('flutter build ipa --no-codesign')"]
        DOCKER["Build Docker Container for CI Artifact Reproducibility"]
    end

    subgraph STAGE4 ["Stage 4: Automated Distribution & Registry"]
        direction TB
        GHCR["Push Docker Image to GitHub Container Registry (GHCR)"]
        RELEASE["Create GitHub Release Tag with Release Notes"]
        ATTACH["Attach 'app-release.apk' & 'app-release.ipa' to GitHub Releases"]
    end

    GH_TRIGGER --> SETUP
    SETUP --> PUB
    PUB --> LINT
    LINT -->|Clean Codebase| UNIT
    UNIT --> ASSERT
    ASSERT -->|All Tests Pass| APK
    APK --> IPA
    IPA --> DOCKER
    DOCKER --> GHCR
    GHCR --> RELEASE
    RELEASE --> ATTACH
    ATTACH --> OTA_READY(["Artifact Ready for In-App Over-The-Air (OTA) Delivery"])
```

---

## Figure 4.3: Detailed CI/CD Sequence and Over-The-Air (OTA) Application Update Architecture

### APA 7th Citation & Metadata
- **Figure Number**: Figure 4.3
- **Figure Title**: *Detailed CI/CD Sequence and Over-The-Air (OTA) Application Update Architecture*
- **Manuscript Page**: 126
- **PDF Page**: 134–135
- **Image Asset**: [fig_4_3_ota_update_sequence.png](file:///Users/arronkianparejas/easylens/docs/figures/assets/fig_4_3_ota_update_sequence.png)

```
Figure 4.3
Detailed CI/CD Sequence and Over-The-Air (OTA) Application Update Architecture

Note. Figure 4.3 displays the UML sequence diagram and physical interaction loop of the over-the-air (OTA) update system, mapping the network transactions between the Buddy client application and the GitHub Releases API to retrieve stable package versions.
```

---

### Technical Diagram (Mermaid Sequence Diagram)

```mermaid
sequenceDiagram
    autonumber
    actor Dev as Developer
    participant Git as GitHub Repository
    participant Actions as GitHub Actions Runner
    participant GHCR as GitHub Container Registry (GHCR)
    participant Releases as GitHub Releases API
    participant App as EasyLens Mobile Client

    %% Continuous Integration & Deployment Flow
    rect rgb(240, 248, 255)
        note over Dev, Releases: CI/CD Build & Release Phase
        Dev->>Git: git push origin main
        Git->>Actions: Trigger CI/CD Workflow
        Actions->>Actions: Run 'flutter analyze' & 'flutter test'
        Actions->>Actions: Compile Release FAT APK (Android) & IPA (iOS)
        Actions->>GHCR: Push Containerized Build Image
        Actions->>Releases: Create Tagged Release (e.g., v1.4.2) & Upload APK Artifacts
        Releases-->>Actions: Artifacts Published Successfully
    end

    %% Over-The-Air (OTA) In-App Update Flow
    rect rgb(255, 250, 240)
        note over App, Releases: Client Over-The-Air (OTA) Update Flow
        App->>App: User Enters Settings Panel / Periodic Background Check
        App->>Releases: GET /repos/Thes-IS-IT/Easylens/releases/latest
        Releases-->>App: Return JSON Payload (tag_name, body, assets[browser_download_url])
        App->>App: Compare Local App Version (e.g., v1.4.1) vs. Remote Tag (v1.4.2)
        
        alt Newer Version Available
            App->>App: Spoken Announcement: "A new EasyLens update is available."
            App->>Releases: GET /download/app-release.apk (Stream Download)
            Releases-->>App: Binary Stream Transferred
            App->>App: Verify SHA-256 Checksum & Prompt Native Package Installer
        else App is Up to Date
            App->>App: Spoken Confirmation: "EasyLens is currently up to date."
        end
    end
```
