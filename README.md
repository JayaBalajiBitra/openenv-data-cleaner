# Data Cleaning OpenEnv Environment

## Overview
This project implements a real-world OpenEnv environment for data cleaning tasks.

The agent interacts with the environment using step(), reset(), and state() APIs.

## Features
- Real-world dataset simulation
- 3 tasks: easy, medium, hard
- Reward system with partial scoring
- Baseline agent for evaluation
- FastAPI endpoints for interaction

## Tasks
- Easy: Remove missing values
- Medium: Remove missing values and duplicates
- Hard: Full cleaning including formatting

## API Endpoints
- /tasks → List tasks
- /baseline → Run baseline agent
- /grader → Get scores

## Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload