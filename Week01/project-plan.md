# Project Plan – Week 01 (KSW Fall 2025 Capstone)

## 1. Team & Roles
- **Team Name:** P31-T1
- **Members & Emails:**
  - Rami Elmostafa – Project Manager – relmost1@students.kennesaw.edu
  - Eni Meduteni – CI/CD Lead – emeduten@students.kennesaw.edu
  - Matt Crowley – Kubernetes/GitOps – mcrowl16@students.kennesaw.edu
  - Cecily Graffree – Kubernetes/GitOps – mcrowl16@students.kennesaw.edu
  - Kade Fleming – Monitoring Lead – kflemi38@students.kennesaw.edu

### Role Ownership (Milestone 1)
- **CI/CD Lead (Jenkins):** Eni Meduteni
  - Pipeline design, Jenkinsfile ownership, build/test stages
- **Kubernetes/GitOps:** Matt Crowley, Cecily Graffree
  - Manifests/Helm, ArgoCD/Flux setup, deployment strategy
- **Monitoring Lead (Prometheus/Grafana):** Kade Fleming
  - Exporters/metrics, dashboards, alerts (later milestones)
- **Documentation/PM Lead:** Rami Elmostafa
  - Weekly notes, diagrams, README, meeting minutes, deadlines

## 2. Scope (Week 1 → Week 12)
- **Goal:** Build a cloud-native CI/CD pipeline that automates build → containerize → deploy to Kubernetes via GitOps, with security & observability.
- **Week 1 Deliverables:** GitHub org/repos, role assignments, draft architecture diagram, 1–2 page plan (this doc).

## 3. Repositories & Branching
- **Org/Owner:** https://github.com/P31CI-CD/CI-CD-Pipeline.git
- **Repos:**
  - `app` – sample application
  - `infra` – IaC / K8s manifests / Helm charts
  - `ops` – Jenkins pipeline config, scripts, docs
- **Branching Model:** `feature/*` → `dev` → `main`
- **PR Policy:** 
- 2 reviews - 
- feature -> dev by PM (Rami Elmostafa)
- dev -> main by Sudheer
- Status checks must pass, squash merge

## ✅ Commit Message Format

Follow a **conventional commits** style (easy to read + good for changelogs):

```
<type>(<scope>): <short summary>
```

### Types

- **feat**: A new feature (`feat(auth): add login endpoint`)
- **fix**: A bug fix (`fix(ui): correct navbar alignment`)
- **docs**: Documentation changes (`docs: update README for Week01`)
- **style**: Code style (formatting, missing semi-colons, no logic changes)
- **refactor**: Code changes that aren’t bug fixes or new features
- **test**: Adding or modifying tests
- **chore**: Maintenance tasks (CI/CD, dependencies, configs)

### Rules

- **Max 72 chars** for the subject line

- Use **imperative mood** (e.g., “add” not “added”)

- Optionally add a body with more context:

  ```
  feat(api): add user authentication
  
  - Implemented JWT-based login
  - Updated CI/CD pipeline to run new tests
  ```

------

## ✅ Pull Request (PR) Process

1. **Branching**

   - Always create a new branch from `dev` (never from `main`)
   - Use clear branch names:
     - `feature/login-auth`
     - `fix/navbar-bug`
     - `docs/week01-plan`

2. **PR Creation**

   - Target branch: `dev`

   - Use a **descriptive title** (similar to commit style):

     - `feat(api): add login authentication`

   - PR template:

     ```
     ## Summary
     What does this PR do?
     
     ## Changes
     - List key changes here
     
     ## Testing
     - How did you test this?
     
     ## Checklist
     - [ ] Code compiles
     - [ ] Tests pass
     - [ ] Documentation updated (if needed)
     ```

3. **Review**

   - No direct pushes to `main`
   - The PR will be reviewed by the Project Manager (Rami Elmostafa) before committing to dev branch.
   - After PR merges into `dev`, once stable, create a PR `dev → main` which will undergo a code review by Sudheer.

## 4. Tools & Versions (initial)
- **Source Control:** GitHub
- **CI:** Jenkins (LTS)  
- **Containers:** Docker
- **Kubernetes:** Minikube (local) or managed (EKS/GKE/AKS) later
- **GitOps:** ArgoCD **or** Flux (choose one by Week 5)
- **Registry:** Docker Hub / GHCR
- **Security:** Trivy (Week 6+), K8s RBAC
- **Observability:** Prometheus, Grafana (Weeks 7–10)
- **Diagrams:** Draw.io / Excalidraw / Mermaid

## 5. Initial Architecture (Draft)
High-level flow to refine in Week 3–6:

GitHub → Jenkins → Docker Registry → Kubernetes
↓ ↑
Tests ArgoCD/Flux (pull-based deploy)
→ Prometheus/Grafana (metrics/dashboards)

## 6. Approvals
- **Student Lead:** Rami Elmostafa, 09/05/2025
- **Mentor (Sudheer Amgothu):** <!-- date -->