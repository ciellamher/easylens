# Appendix G: Data Dictionary

Every entry is checked against the current code (`upstream/main`, commit `c10062e`). EasyLens has no SQL database: data is kept in the phone's memory while the app runs, in the phone's local key-value storage (Android SharedPreferences / iOS NSUserDefaults), in files on the phone, in Google Cloud Firestore (a document database), and in Cloudflare R2 (one profile photo per account). Types are the Dart and Firestore types the code uses.

---

**Table G.1**
*Core System Variables and Operational Parameters*

| Variable Name | Data Type | Storage Location | Purpose and Constraint |
| :--- | :--- | :--- | :--- |
| `participant_id` | string | Research data sheets (not stored by the app) | Code identifying each testing record: BETA-01 to BETA-15 (end-users) and EXP-01 to EXP-05 (experts). |
| `label` (detected object) | string | Phone memory only (not saved) | Name of a detected object. In Object Detection mode it is a COCO class from the SSD MobileNet model (e.g., person, car, bicycle); in Navigation mode it is a Google ML Kit image label. |
| `score` (confidence) | double, 0.00–1.00 | Phone memory only | Model confidence for a detection or label. SSD MobileNet detections below 0.35 are dropped; the glasses-screen ML Kit image labeler also uses 0.35. |
| `normCenterX` | double, 0.00–1.00 | Phone memory only | Horizontal center of the largest detected box. Below 0.38 = left, 0.38–0.62 = center, above 0.62 = right. |
| `largestArea` | double, 0.00–1.00 | Phone memory only | Share of the frame covered by the largest centered box. Above 0.45 triggers a "stop" warning; above 0.18 triggers a "step aside" warning. |
| `selectedLanguage` | string | Phone settings storage; Firestore | App and speech language: `English (US)` (default) or `Tagalog`. |
| `useLocalAI` | boolean | Phone settings storage | Buddy's AI mode: `true` = Local AI mode with Gemma 2B (default); `false` = online mode with Google Gemini. |
| spoken question | string | Phone memory; saved to chat history and the day's journal | The user's question as converted by speech-to-text, answered by Buddy. |

---

**Table G.2**
*Local User Settings (phone settings storage, SharedPreferences)*

| Key | Data Type | Default | Allowed Values / Range | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| `selectedLanguage` | string | `English (US)` | `English (US)`, `Tagalog` | App and speech language. |
| `selectedContrastTheme` | string | `Default` | `Default`, `Black on White`, `White on Black`, `Green on Black`, `Yellow on Black`, `Cyan on Black` | High-contrast color theme. |
| `selectedVoicePersona` | string | `Aria (Calm)` | `Aria (Calm)`, `Max (Bold)`, `Nova (Bright)`, `Echo (Deep)`, `Leo (Child)` | Buddy's voice. |
| `selectedUnit` | string | `Metric` | `Metric`, `Imperial` | Units for distances. |
| `selectedMobilityAid` | string | `None (Hands-Free)` | Chosen at sign-up | Used to tailor Buddy's answers. |
| `selectedTextSize` | string | `Default` | `Small`, `Default`, `Large`, `Extra Large`, `Custom` | Text size. |
| `textSizeCustomScale` | double | 1.0 | 0.85–1.35 | Text scale when size is `Custom`. |
| `speechRate` | double | 0.5 | 0.0–1.0 (slider) | Speaking speed; the app uses 0.5 + value. |
| `speechPitch` | double | 0.5 | 0.0–1.0 (slider) | Voice pitch; the app uses 0.5 + value, limited to 0.5–2.0 on Android. |
| `voiceFeedback` | boolean | `true` | `true` / `false` | Turns spoken feedback on or off. |
| `buttonHaptics`, `hapticFeedback` | boolean | `true` | `true` / `false` | Vibration when buttons are pressed. |
| `navigationHaptics` | boolean | `true` | `true` / `false` | Vibration for navigation and hazard warnings. |
| `soundEffects` | boolean | `true` | `true` / `false` | App sound effects. |
| `useLocalAI` | boolean | `true` | `true` / `false` | Local AI mode (Gemma 2B) or online mode (Gemini). |
| `geminiApiKey` | string | empty | Optional | Gemini API key entered by the user; stored as plain text on the phone. |
| `userDisplayName` | string | empty | — | Name Buddy uses to address the user. |

---

**Table G.3**
*User Profile (Google Cloud Firestore: `users/{uid}`)*

| Field | Firestore Type | Required | Key | Description |
| :--- | :--- | :---: | :---: | :--- |
| `uid` | string | Yes | PK | Firebase Authentication user ID; also the document ID. |
| `email` | string | Yes | — | Account email address. |
| `displayName` | string | Yes | — | User's name. |
| `photoUrl` | string | No | — | Link to the profile photo in Cloudflare R2 (empty if none). |
| `isForMyself` | boolean | Yes | — | Whether the account is for the user or set up by someone else. |
| `selectedConditions` | array of strings | No | — | Eye conditions chosen at sign-up (health information). |
| `preferences` | map | Yes | — | Copy of the sign-up settings in Table G.2, plus `birthday` and `name`. |
| `createdAt` | timestamp | Yes | — | When the profile was first saved. |
| `updatedAt` | timestamp | Yes | — | When the profile was last saved. |

---

**Table G.4**
*Emergency Contacts (Firestore: `users/{uid}/contacts/{phone}`; copy on the phone)*

| Field | Data Type | Required | Key | Description |
| :--- | :--- | :---: | :---: | :--- |
| `phone` | string | Yes | PK | Contact's mobile number, normalized to the 11-digit `09XXXXXXXXX` format; also the document ID. |
| `uid` | string | Yes | FK | Parent user document (`users/{uid}`); not stored as a field. |
| `name` | string | Yes | — | Contact's name. |
| `relationship` | string | No | — | Relationship to the user (e.g., parent, caregiver). |
| `isActive` | boolean | Yes | — | Whether this contact receives SOS alerts; every active contact is sent the SMS. |

Constraint: at most three contacts per user. On the phone they are stored under the key `easylens_emergency_contacts_{uid}`.

---

**Table G.5**
*Cloud Storage Objects (Cloudflare R2)*

| Object Key Pattern | MIME Type | Access | Description |
| :--- | :--- | :--- | :--- |
| `users/{uid}/avatar.png` | `image/png` | Public read (anyone with the link) | Optional profile photo chosen at sign-up or in Profile Details. This is the only object EasyLens uploads to R2. |

No other files are uploaded to R2. Audio cues are bundled inside the app, and face data, camera frames and settings are not backed up to R2.

---

**Table G.6**
*Registered Faces (phone only, never uploaded)*

| Field | Data Type | Required | Key | Description |
| :--- | :--- | :---: | :---: | :--- |
| `id` | string | Yes | PK | Unique ID of the registered person. |
| `userId` | string | No | FK | Account that registered the face. |
| `name` | string | Yes | — | Name Buddy announces when the face is recognized. |
| `imageLocalPath` | string | No | — | Path to the captured photo on the phone. |
| `faceFeatures` | list of 25 doubles | No | — | Geometric face measurements (distances and proportions between eyes, nose, mouth and face outline). |
| `multiSampleFeatures` | list of lists of doubles | No | — | Feature vectors from the front, left and right captures. |
| `registeredAt` | datetime | Yes | — | When the face was registered. |
| `isGdprConsented` | boolean | Yes | — | Whether the RA 10173 consent box was ticked. |
| `consentDate` | datetime | No | — | When consent was given. |

Stored under the key `registered_face_profiles_{uid}`.

---

**Table G.7**
*Recent Navigation (Firestore: `users/{uid}/recent_navigation/{id}`; last five on the phone)*

| Field | Data Type | Key | Description |
| :--- | :--- | :---: | :--- |
| `id` | string | PK | Time the entry was saved, in milliseconds; the document ID. |
| `uid` | string | FK | Parent user document. |
| `name` | string | — | Destination name. |
| `address` | string | — | Destination address. |
| `latitude`, `longitude` | double | — | Destination coordinates. |
| `dist`, `time` | string | — | Distance and time shown to the user (e.g., "1.2 km"). |
| `steps` | array of strings | — | Route instructions. |
| `timestamp` | timestamp | — | Server time when saved. |

The phone keeps only the last five destinations; Firestore keeps every saved destination.

---

**Table G.8**
*Feedback (Firestore: `users/{uid}/feedbacks/{autoId}`; copy sent to Notion)*

| Field | Data Type | Key | Description |
| :--- | :--- | :---: | :--- |
| `autoId` | string | PK | Document ID created by Firestore. |
| `userId` | string | FK | User who submitted the feedback. |
| `email`, `displayName` | string | — | Submitter's email and name. |
| `rating` | int, 1–5 | — | Satisfaction rating (emoji scale). |
| `subject` | string | — | `Bug`, `Suggestion`, `Content`, `Compliment` or `Other`. |
| `comment` | string | — | Free-text comment. |
| `timestamp` | timestamp | — | Server time when submitted. |

---

**Table G.9**
*Interaction Journals (phone only: `journals/journal_YYYY-MM-DD.md`)*

| Field | Data Type | Key | Description |
| :--- | :--- | :---: | :--- |
| `date` | date (YYYY-MM-DD) | PK | Day of the journal; one file per day. |
| `insights` | list of strings | — | Short notes about the user, written by Gemini when online or a simple note when offline. |
| `logs[].time` | string (HH:MM) | — | Time of each exchange. |
| `logs[].userMessage` | string | — | What the user asked or did (including visited places). |
| `logs[].buddyResponse` | string | — | Buddy's reply. |

Journals have no user ID, so every account signed in on the same phone shares them. The last seven days are searched with TF-IDF when Buddy answers.
