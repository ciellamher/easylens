# Appendix F: Entity Relationship Diagrams

Both diagrams show the data EasyLens actually stores, checked against the current code (`upstream/main`, commit `c10062e`). EasyLens has no SQL database: account data is stored in Google Cloud Firestore (a document database), and registered faces, settings and a copy of the emergency contacts are stored on the phone. In Figure F.2, each Firestore subcollection is shown as a table whose foreign key is the parent user document (`users/{uid}`).

---

## Figure F.1: Conceptual Entity Relationship Diagram

### APA 7th Citation & Metadata
- **Figure Number**: Figure F.1
- **Figure Title**: *Conceptual Entity Relationship Diagram*
- **Image Asset**: [fig_f_1_conceptual_erd.png](assets/fig_f_1_conceptual_erd.png)

```
Figure F.1
Conceptual Entity Relationship Diagram

Note. Figure F.1 shows the main data entities in EasyLens and how they relate to the user, in Chen notation. A user can add up to three emergency contacts, and can register any number of faces, navigate to any number of destinations, and submit any number of feedback entries.
```

### Source (Graphviz)

```dot
graph F1 {
  graph [layout=neato, overlap=false, splines=true, dpi=220, pad=0.3, bgcolor=white, fontname="Helvetica"];
  node  [fontname="Helvetica", fontsize=12];
  edge  [fontname="Helvetica", fontsize=11, color="#444444", len=1.6];

  node [shape=box, style="filled,bold", fillcolor="#EEF3FB", color="#4C72B0", width=1.9, height=0.6];
  USER    [label="USER", pos="0,0!"];
  CONTACT [label="EMERGENCY CONTACT", pos="5.2,2.2!"];
  FACE    [label="REGISTERED FACE", pos="5.2,0.7!"];
  DEST    [label="RECENT DESTINATION", pos="5.2,-0.8!"];
  FB      [label="FEEDBACK", pos="5.2,-2.3!"];

  node [shape=diamond, style=filled, fillcolor="#FFF6E5", color="#DD8452", width=1.5, height=0.8, fontsize=11];
  R1 [label="adds", pos="2.6,2.2!"];
  R2 [label="registers", pos="2.6,0.7!"];
  R3 [label="navigates to", pos="2.6,-0.8!"];
  R4 [label="submits", pos="2.6,-2.3!"];

  USER -- R1 [headlabel="", taillabel="1", labeldistance=2.2];
  R1 -- CONTACT [headlabel="0..3", labeldistance=2.2];
  USER -- R2 [taillabel="1", labeldistance=2.2];
  R2 -- FACE [headlabel="0..N", labeldistance=2.2];
  USER -- R3 [taillabel="1", labeldistance=2.2];
  R3 -- DEST [headlabel="0..N", labeldistance=2.2];
  USER -- R4 [taillabel="1", labeldistance=2.2];
  R4 -- FB [headlabel="0..N", labeldistance=2.2];
}
```

---

## Figure F.2: Relational Entity Relationship Diagram

### APA 7th Citation & Metadata
- **Figure Number**: Figure F.2
- **Figure Title**: *Relational Entity Relationship Diagram*
- **Image Asset**: [fig_f_2_relational_erd.png](assets/fig_f_2_relational_erd.png)

```
Figure F.2
Relational Entity Relationship Diagram

Note. Figure F.2 lists the fields, data types, primary keys (PK) and foreign keys (FK) of each entity, in crow's foot notation, with where each is stored. USERS, EMERGENCY_CONTACTS, RECENT_NAVIGATION and FEEDBACKS are stored in Google Cloud Firestore; emergency contacts and the last five destinations are also kept on the phone. REGISTERED_FACES is stored only on the phone and is never uploaded. Submitted feedback is also copied to a Notion database.
```

### Source (Graphviz)

```dot
digraph F2 {
  graph [rankdir=LR, dpi=200, pad=0.3, bgcolor=white, nodesep=0.4, ranksep=1.3, fontname="Helvetica"];
  node [shape=plaintext, fontname="Helvetica", fontsize=10];
  edge [color="#444444", dir=both, fontname="Helvetica", fontsize=10];
  USERS [label=<<table border="1" cellborder="0" cellspacing="0" cellpadding="4" color="#4C72B0"><tr><td colspan="3" bgcolor="#DCE6F5"><b>USERS</b></td></tr><tr><td colspan="3" bgcolor="#DCE6F5"><font point-size="9">Firestore: users/{uid}</font></td></tr><tr><td align="left" width="34"><font color="#8A5A00"><b>PK</b></font></td><td align="left">uid</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">email</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">displayName</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">photoUrl</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">isForMyself</td><td align="left"><font color="#555555">boolean</font></td></tr><tr><td align="left" width="34"></td><td align="left">selectedConditions</td><td align="left"><font color="#555555">array&lt;string&gt;</font></td></tr><tr><td align="left" width="34"></td><td align="left">preferences.birthday</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">preferences.selectedLanguage</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">preferences.selectedContrastTheme</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">preferences.selectedVoicePersona</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">preferences.selectedUnit</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">preferences.selectedMobilityAid</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">preferences.voiceFeedback</td><td align="left"><font color="#555555">boolean</font></td></tr><tr><td align="left" width="34"></td><td align="left">preferences.hapticFeedback</td><td align="left"><font color="#555555">boolean</font></td></tr><tr><td align="left" width="34"></td><td align="left">createdAt</td><td align="left"><font color="#555555">timestamp</font></td></tr><tr><td align="left" width="34"></td><td align="left">updatedAt</td><td align="left"><font color="#555555">timestamp</font></td></tr></table>>];
  CONTACTS [label=<<table border="1" cellborder="0" cellspacing="0" cellpadding="4" color="#4C72B0"><tr><td colspan="3" bgcolor="#DCE6F5"><b>EMERGENCY_CONTACTS</b></td></tr><tr><td colspan="3" bgcolor="#DCE6F5"><font point-size="9">Firestore: users/{uid}/contacts/{phone}; copy on phone</font></td></tr><tr><td align="left" width="34"><font color="#8A5A00"><b>PK</b></font></td><td align="left">phone (normalized)</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"><font color="#8A5A00"><b>FK</b></font></td><td align="left">uid</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">name</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">relationship</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">isActive</td><td align="left"><font color="#555555">boolean</font></td></tr></table>>];
  FACES [label=<<table border="1" cellborder="0" cellspacing="0" cellpadding="4" color="#55A868"><tr><td colspan="3" bgcolor="#DDEFE2"><b>REGISTERED_FACES</b></td></tr><tr><td colspan="3" bgcolor="#DDEFE2"><font point-size="9">Phone only (never uploaded)</font></td></tr><tr><td align="left" width="34"><font color="#8A5A00"><b>PK</b></font></td><td align="left">id</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"><font color="#8A5A00"><b>FK</b></font></td><td align="left">userId</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">name</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">imageLocalPath</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">faceFeatures</td><td align="left"><font color="#555555">list&lt;double&gt;</font></td></tr><tr><td align="left" width="34"></td><td align="left">multiSampleFeatures</td><td align="left"><font color="#555555">list&lt;list&lt;double&gt;&gt;</font></td></tr><tr><td align="left" width="34"></td><td align="left">registeredAt</td><td align="left"><font color="#555555">datetime</font></td></tr><tr><td align="left" width="34"></td><td align="left">isGdprConsented</td><td align="left"><font color="#555555">boolean</font></td></tr><tr><td align="left" width="34"></td><td align="left">consentDate</td><td align="left"><font color="#555555">datetime</font></td></tr></table>>];
  DEST [label=<<table border="1" cellborder="0" cellspacing="0" cellpadding="4" color="#4C72B0"><tr><td colspan="3" bgcolor="#DCE6F5"><b>RECENT_NAVIGATION</b></td></tr><tr><td colspan="3" bgcolor="#DCE6F5"><font point-size="9">Firestore: users/{uid}/recent_navigation/{id}; last 5 on phone</font></td></tr><tr><td align="left" width="34"><font color="#8A5A00"><b>PK</b></font></td><td align="left">id (time in ms)</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"><font color="#8A5A00"><b>FK</b></font></td><td align="left">uid</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">name</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">address</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">latitude</td><td align="left"><font color="#555555">double</font></td></tr><tr><td align="left" width="34"></td><td align="left">longitude</td><td align="left"><font color="#555555">double</font></td></tr><tr><td align="left" width="34"></td><td align="left">dist</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">time</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">steps</td><td align="left"><font color="#555555">array&lt;string&gt;</font></td></tr><tr><td align="left" width="34"></td><td align="left">timestamp</td><td align="left"><font color="#555555">timestamp</font></td></tr></table>>];
  FB [label=<<table border="1" cellborder="0" cellspacing="0" cellpadding="4" color="#4C72B0"><tr><td colspan="3" bgcolor="#DCE6F5"><b>FEEDBACKS</b></td></tr><tr><td colspan="3" bgcolor="#DCE6F5"><font point-size="9">Firestore: users/{uid}/feedbacks/{autoId}; copy sent to Notion</font></td></tr><tr><td align="left" width="34"><font color="#8A5A00"><b>PK</b></font></td><td align="left">autoId</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"><font color="#8A5A00"><b>FK</b></font></td><td align="left">userId</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">email</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">displayName</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">rating</td><td align="left"><font color="#555555">int (1–5)</font></td></tr><tr><td align="left" width="34"></td><td align="left">subject</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">comment</td><td align="left"><font color="#555555">string</font></td></tr><tr><td align="left" width="34"></td><td align="left">timestamp</td><td align="left"><font color="#555555">timestamp</font></td></tr></table>>];
  USERS -> CONTACTS [arrowtail=teetee, arrowhead=crowodot, label="has (0..3)"];
  USERS -> FACES [arrowtail=teetee, arrowhead=crowodot, label="registers"];
  USERS -> DEST [arrowtail=teetee, arrowhead=crowodot, label="navigates to"];
  USERS -> FB [arrowtail=teetee, arrowhead=crowodot, label="submits"];
}
```
