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

## 📦 Deployment

### Kubernetes (Helm)
```bash
helm install ai-guardrails helm/ai-guardrails
Istio / Envoy
Envoy ext_authz blocks malicious AI requests before they reach the chatbot
Guardrails are enforced at the mesh boundary
🔁 CI/CD
GitHub Actions pipeline includes:
Dependency installation
Unit tests
Guardrails regression tests
PR & main-branch validation
Workflow location:
.github/workflows/ci.yml
🧪 Testing Strategy
Unit tests for guardrails detectors
Prompt injection fuzzing
Ransomware intent simulations
Chaos testing for LLM fallback paths
🎯 Use Cases
Internal enterprise chatbot
Secure RAG over proprietary data
Banking / healthcare AI assistants
Regulated GenAI platforms
🧠 Why This Project Matters
This repository demonstrates:
Zero-trust AI architecture
Security-first GenAI design
Production-ready cloud deployment
MITRE-aligned AI threat modeling
📜 License
MIT License

---

If you want next, I can:
- Generate **architecture diagrams (PNG / SVG)**
- Add **Terraform (EKS + RDS + Bedrock)**
- Create a **LinkedIn post** explaining this system
- Turn this into an **interview walkthrough**

Just tell me 👍