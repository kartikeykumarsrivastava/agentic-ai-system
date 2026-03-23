# 🧠 Agentic AI System – Phase 1

## 📌 Use Case: Loan Advisor Agent Chatbot

In modern banking systems, users often struggle to:

* Understand **loan eligibility criteria**
* Navigate **policy documents**
* Perform **manual calculations**
* Identify **next steps for application**

### 💡 Solution

This project implements an **Agentic RAG-based chatbot** that:

* Understands user intent
* Retrieves knowledge from documents (RAG)
* Performs eligibility calculations
* Provides policy guidance
* Combines all responses into a single answer

### 🧠 Example Query

> *"I earn ₹8L annually. Am I eligible for a home loan and what is the process?"*

### ✅ System Response

* Eligibility result
* Relevant policy rules
* Supporting knowledge
* Application steps

---

# 🏗️ Phase-1 Objective

Build a **working Agentic RAG system (local setup)** with:

* Independent microservices
* Tool-based architecture
* Agent-driven orchestration
* End-to-end query handling

---

# 🧩 Architecture Overview

```
User
 ↓
Agent Service (Python)
 ↓
 ├── RAG Service
 ├── Eligibility Service
 └── Policy Service
 ↓
LLM → Response
```

---

# 📦 Project Structure

```
agentic-ai-system/
│
├── gateway-service/              # (Phase-2) API Gateway - Spring Boot
├── agent-service/               # Agent (LangChain)
├── rag-service/                 # Retrieval Service
├── eligibility-service/         # Loan eligibility logic
├── policy-service/              # Policy API (Spring Boot)
│
├── shared-contracts/            # JSON schemas
├── infra/                       # Docker, K8s (Phase-2+)
├── ci-cd/                       # Pipelines (Phase-3)
└── observability/               # Monitoring (Phase-4)
```

---

# ⚙️ Services Overview

## 🔹 1. Agent Service

* Acts as the **brain of the system**
* Decides which tool to call
* Combines responses using LLM

---

## 🔹 2. RAG Service

* Retrieves relevant loan information
* Uses vector search (FAISS or similar)

---

## 🔹 3. Eligibility Service

* Calculates loan eligibility based on salary

---

## 🔹 4. Policy Service

* Provides loan rules and guidelines

---

# 🔌 API Endpoints

| Service     | Endpoint    | Description           |
| ----------- | ----------- | --------------------- |
| Agent       | `/ask`      | Main chatbot entry    |
| RAG         | `/retrieve` | Fetch knowledge       |
| Eligibility | `/check`    | Calculate eligibility |
| Policy      | `/policy`   | Get rules             |

---

# ▶️ Running the Services

## 1. Start Python Services

```bash
cd agent-service && uvicorn app:app --port 8000 --reload
cd rag-service && uvicorn app:app --port 8001 --reload
cd eligibility-service && uvicorn app:app --port 8002 --reload
```

---

## 2. Start Policy Service (Spring Boot)

```bash
cd policy-service
mvn spring-boot:run
```

---

## 3. Test the System

```bash
curl -X POST http://localhost:8000/ask \
-H "Content-Type: application/json" \
-d '{"query":"I earn 8 lakh. Am I eligible and what is policy?"}'
```

---

# 🧠 How It Works

1. User sends query
2. Agent analyzes intent
3. Agent calls:

   * RAG → knowledge
   * Eligibility → calculation
   * Policy → rules
4. LLM combines results
5. Final response returned

---

# 🧪 Phase-1 Scope

## ✅ Included

* Multi-service architecture
* Agent + tools integration
* Local execution
* API-based communication

## ❌ Not Included (Next Phases)

* LangGraph orchestration
* CI/CD pipelines
* Docker/Kubernetes
* Observability (ELK, Prometheus)
* Security / Guardrails

---

# 🧾 Definition of Done

* All services run independently
* Agent dynamically calls tools
* End-to-end query works
* No hardcoded logic

---

# 🚀 Next Steps

## Phase-2

* Replace LangChain agent with **LangGraph**
* Add **state management**

## Phase-3

* Add **API Gateway (Spring Boot)**
* Implement **CI/CD**

## Phase-4

* Add **Docker + Kubernetes**
* Integrate **Observability (OpenTelemetry, ELK)**

---

# Key Concepts

| Concept       | Description                     |
| ------------- | ------------------------------- |
| RAG           | Retrieval-Augmented Generation  |
| Agent         | Decision-making unit            |
| Agentic AI    | Iterative reasoning system      |
| Microservices | Independent deployable services |

---

# 🎯 Summary

This phase establishes a **strong foundation** for building:

* Scalable AI systems
* Agent-driven workflows
* Enterprise-grade architectures

👉 You now have a **working Agentic RAG system** ready for production evolution.
