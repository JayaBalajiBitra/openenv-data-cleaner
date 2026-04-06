# 🧠 OpenEnv Data Cleaning Environment

## 📌 Overview
This project implements a real-world OpenEnv environment where an AI agent performs data cleaning tasks such as handling missing values, removing duplicates, and improving data consistency.

The environment follows the OpenEnv specification with structured APIs (`step`, `reset`, `state`) and supports automated evaluation using graders.

---

## 🚀 Features
- Real-world data cleaning simulation
- OpenEnv-compliant environment design
- 3 difficulty levels:
  - Easy → Missing values
  - Medium → Missing values + duplicates
  - Hard → Full cleaning + formatting
- Reward system with partial scoring
- Deterministic graders (0.0 → 1.0)
- Baseline agent for reproducible evaluation
- FastAPI endpoints for interaction
- Dockerized for deployment

---

## 🧪 Tasks

### 🟢 Easy
Remove missing values from dataset

### 🟡 Medium
Remove missing values and duplicates

### 🔴 Hard
Perform full data cleaning including formatting consistency

---

## ⚙️ API Endpoints

- `/tasks` → List available tasks  
- `/baseline` → Run baseline agent  
- `/grader` → Evaluate task performance  

---

## ▶️ Run Locally

```bash
pip install pydantic fastapi uvicorn pandas
uvicorn main:app --reload
