# 🔐 AI Secure Chatbot Platform  
## Zero-Trust GenAI with Guardrails, RAG, Multi-LLM Fallback, and Observability

This repository implements an **enterprise-grade internal AI chatbot platform** with **security-first design**.  
It combines **Google ADK agent orchestration**, **RAG using PostgreSQL + pgvector**, **AWS Bedrock hosting**, **multi-LLM fallback**, and **comprehensive AI guardrails** enforced via **FastAPI, Envoy/Istio, and OIDC**.

The platform is designed for **regulated, security-sensitive environments** where GenAI must be controlled, auditable, and resilient.

---

## 🚀 Key Features

### 🤖 AI Chatbot
- Google ADK–based agent orchestration
- Retrieval-Augmented Generation (RAG)
- PostgreSQL + pgvector vector database
- Context re-ranking
- Multi-LLM fallback strategy
- Primary inference hosted on **AWS Bedrock**

### 🛡️ AI Guardrails & Security
- **Pre-LLM guardrails**
  - Prompt injection detection
  - Indirect prompt injection protection
  - Ransomware / malware intent detection
  - Image-based attack hooks
- **Post-LLM guardrails**
  - LLM self-critique / output validation
- Envoy / Istio `ext_authz` enforcement
- OIDC authentication (Cognito / Okta / ForgeRock compatible)
- MITRE ATT&CK–aligned threat detection

### 📊 Observability
- Prometheus metrics
- Grafana dashboards
- Security KPIs and anomaly monitoring

### ☁️ Cloud-Native & DevOps
- FastAPI microservices
- Kubernetes & Istio ready
- Helm charts
- GitHub Actions CI/CD

---

## 🏗️ High-Level Architecture

Client
↓
Istio Ingress / Envoy
→ ext_authz (Guardrails Service)
↓
Chatbot API (FastAPI + OIDC)
↓
Google ADK Agent
↓
RAG (pgvector + PostgreSQL)
↓
Reranker
↓
Multi-LLM Fallback
→ AWS Bedrock (primary)
→ Secondary LLM
↓
Post-LLM Self-Critique Guard
↓
Response

---

## 📁 Project Structure

ai-secure-chatbot/
├── chatbot-api/
│ ├── main.py
│ ├── auth/oidc.py
│ ├── guardrails/
│ │ ├── pre_guard.py
│ │ └── post_guard.py
│ ├── rag/
│ │ ├── pgvector_store.py
│ │ ├── retriever.py
│ │ └── reranker.py
│ ├── llm/
│ │ ├── bedrock.py
│ │ ├── openai.py
│ │ └── fallback.py
│ └── agents/google_adk_agent.py
│
├── guardrails-service/
├── envoy/envoy-filter.yaml
├── helm/ai-guardrails/
├── grafana/ai_guardrails_dashboard.json
├── mitre/mitre_attack_mapping.json
├── .github/workflows/ci.yml
├── requirements.txt
└── README.md

---

## 🔐 Guardrails Coverage

| Threat | Enforcement Layer |
|------|-------------------|
| Prompt Injection | Pre-LLM |
| Indirect Prompt Injection | Pre-LLM + RAG filtering |
| Ransomware / Malware Intent | Pre-LLM |
| Data Exfiltration | Pre-LLM |
| Unsafe LLM Output | Post-LLM Self-Critique |
| Model Abuse | Rate & entropy checks |
| Image-based Attacks | Vision moderation hooks |

---

## 🧭 MITRE ATT&CK Mapping

The system maps AI-specific threats to MITRE ATT&CK tactics, including:

- **Initial Access** (T1190, T1078)
- **Execution** (T1059)
- **Defense Evasion** (T1027, T1562)
- **Command & Control** (T1071, T1095)
- **Exfiltration** (T1041)

Mappings are defined in:
mitre/mitre_attack_mapping.json

---

## 📊 Metrics & Dashboards

### Prometheus Metrics
- `prompt_injection_blocks_total`
- `ransomware_blocks_total`
- `guardrails_request_latency_seconds`
- `llm_fallback_total`

### Grafana
- Security event trends
- Guardrails latency
- LLM fallback rate
- Anomalous request behavior

---

## 🔑 Authentication (OIDC)

- Bearer token–based authentication
- Compatible with:
  - AWS Cognito
  - Okta
  - ForgeRock
- Enforced **before any LLM or RAG call**

---

## 🚀 Deployment & Run Guide

### Prerequisites

**Local**

* Python 3.10+
* Docker & Docker Compose
* kubectl
* Helm v3+

**Kubernetes**

* Kubernetes cluster (EKS / kind / minikube)
* Prometheus Operator
* AWS credentials (for Bedrock access)

---

### Local Run (Development Mode)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Set environment variables:

```bash
export AWS_REGION=us-east-1
export BEDROCK_MODEL_ID=anthropic.claude-3
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/chatbot
export OIDC_ISSUER=https://auth.example.com
export OIDC_AUDIENCE=chatbot
```

Start PostgreSQL + pgvector:

```bash
docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=postgres ankane/pgvector
```

Run the application:

```bash
uvicorn app.main:app --reload --port 8080
```

Verify:

```bash
curl http://localhost:8080/health
curl http://localhost:8080/metrics
```

---

### Docker Build & Run

```bash
docker build -t ai-secure-chatbot:latest .

docker run -p 8080:8080 \
  -e AWS_REGION=us-east-1 \
  -e DATABASE_URL=postgresql://postgres:postgres@host.docker.internal:5432/chatbot \
  ai-secure-chatbot
```

---

### Kubernetes Deployment (Helm)

Add Prometheus Helm repo:

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

Install Prometheus Operator:

```bash
helm install prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring --create-namespace
```

---

### Deploy Chatbot via Helm

```bash
helm lint helm/chatbot
helm template chatbot helm/chatbot

helm install chatbot helm/chatbot \
  --namespace ai --create-namespace
```

Upgrade:

```bash
helm upgrade chatbot helm/chatbot -n ai
```

---

### Verify Deployment

```bash
kubectl get pods -n ai
kubectl get svc -n ai
kubectl get servicemonitor -n ai
```

Port forward:

```bash
kubectl port-forward svc/chatbot 8080:80 -n ai
```

---

### Metrics & Observability

* **Prometheus** scrapes `/metrics` via ServiceMonitor
* **Grafana** dashboards visualize latency, token usage, guardrail blocks, and MITRE ATT&CK mappings

Access Grafana:

```bash
kubectl port-forward svc/prometheus-grafana 3000:80 -n monitoring
```

---

### Runtime Guardrails Flow

```
User Prompt
   ↓
Envoy / Istio Filter (optional)
   ↓
FastAPI Guardrails Engine
   ├─ Prompt Injection Detection
   ├─ Ransomware / Malware Intent Detection
   ├─ Image Safety Validation
   ├─ MITRE ATT&CK Mapping
   ↓
RAG (PostgreSQL + pgvector)
   ↓
LLM (AWS Bedrock → Fallback Models)
   ↓
LLM Self‑Critique Guard
   ↓
Final Response
```

---

### CI/CD (GitHub Actions)

```text
.github/workflows/
 ├─ ci.yml        # Tests + linting
 ├─ docker.yml    # Docker build & push
 └─ helm.yml      # Helm lint & template validation
```

Triggered on pull requests and main branch pushes.

---

### Troubleshooting

* **ServiceMonitor not found**:

  ```bash
  kubectl get crd | grep servicemonitor
  ```
* **Helm YAML errors**:

  ```bash
  helm template chatbot helm/chatbot --debug
  ```
* **Metrics not scraped**:

  * Verify Service labels match ServiceMonitor selector
  * Ensure Prometheus release label is correct

🔗 **GitHub**: [https://github.com/ramukunireddy6/ai-secure-chatbot](https://github.com/ramukunireddy6/ai-secure-chatbot)
