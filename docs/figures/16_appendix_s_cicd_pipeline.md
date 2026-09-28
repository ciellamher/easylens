# Appendix S: Continuous Integration and Continuous Deployment (CI/CD) Pipeline

Figure S.1 is drawn from the project's GitHub Actions workflow, `.github/workflows/ci_cd.yml`, with Graphviz.

---

## Figure S.1: CI/CD Pipeline of the EasyLens Project

- **Image Asset**: [fig_s_1_cicd_pipeline.png](assets/fig_s_1_cicd_pipeline.png)

```
Figure S.1
CI/CD Pipeline of the EasyLens Project

Note. The pipeline runs on GitHub Actions for every push and pull request to the main branch, and can also be started manually. The first job installs the app's dependencies, runs static analysis (flutter analyze) and runs the unit and widget tests (flutter test). If these pass, the second job builds a Docker image of the EasyLens download landing page, an nginx web server, and checks that the page responds. For changes pushed to main, the image is published to the GitHub Container Registry (GHCR); pull requests are checked but not published. The pipeline does not build the mobile app: the Android (APK) and iOS (IPA) packages were built and uploaded to GitHub Releases manually, and the app's Check for Updates feature reads the latest release from there.
```

### Source (Graphviz)

```dot
digraph S1 {
  graph [rankdir=TB, fontname="Helvetica", nodesep=0.5, ranksep=0.45, dpi=220, pad=0.3, bgcolor=white, compound=true];
  node  [fontname="Helvetica", fontsize=11, shape=box, style="rounded,filled", fillcolor="#EEF3FB", color="#4C72B0", width=3.2];
  edge  [fontname="Helvetica", fontsize=10, color="#444444"];

  trig [shape=box, style="filled,bold", fillcolor="#F2F2F2", color="#222222", label="Push or pull request to main\n(or started manually)"];

  subgraph cluster_j1 {
    label=<<b>Job 1: Analyze and Test</b>>; fontsize=12; labeljust="l"; labelloc="b"; style="rounded"; color="#9A9A9A";
    a1 [label="Check out code\nSet up Java 17 and Flutter (stable)"];
    a2 [label="flutter pub get"];
    a3 [label="flutter analyze"];
    a4 [label="flutter test\n(7 unit and widget test files)"];
    a1 -> a2 -> a3 -> a4;
  }

  fail [shape=box, style="filled", fillcolor="#FDEBDD", color="#DD8452", label="Pipeline fails;\nchange is flagged on GitHub"];

  subgraph cluster_j2 {
    label=<<b>Job 2: Docker Build and Publish</b>>; fontsize=12; labeljust="l"; style="rounded"; color="#9A9A9A";
    b1 [label="Build Docker image\n(nginx download landing page)"];
    b2 [label="Health check: start container,\nrequest the page"];
    b3 [shape=diamond, fillcolor="#FFF6E5", color="#DD8452", width=2.2, height=1.0, label="Push to main?"];
    b4 [label="Publish image to GitHub\nContainer Registry (GHCR)\ntags: latest and commit SHA"];
    b5 [label="Stop (pull requests are\nchecked but not published)"];
    b1 -> b2 -> b3;
    b3 -> b4 [label=" yes"];
    b3 -> b5 [label=" no"];
  }

  man [shape=box, style="filled,dashed", fillcolor="#F7F7F7", color="#555555", label="Manual release (outside the pipeline)\nDeveloper builds APK and IPA\nand uploads them to GitHub Releases"];
  app [shape=box, style="filled", fillcolor="#F2F2F2", color="#555555", label="Buddy app: Check for Updates\nreads the latest GitHub Release"];

  trig -> a1;
  a4 -> b1 [label=" all passed", lhead=cluster_j2];
  a4 -> fail [label=" any step fails", style=dashed, tailport=w];
  man -> app [style=dashed];
}
```
