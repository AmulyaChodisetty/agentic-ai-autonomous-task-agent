# Agentic AI – Autonomous Task-Oriented AI Agent

## Problem Statement
Design an Agentic AI system that can autonomously plan and execute a multi-step task using external tools.

## Scenario
The AI agent receives the following user goal:

**“Find the top 3 recent AI research papers on agriculture, summarize them, and store the output in a structured format.”**

---

## System Overview
This project implements an **Agentic AI** using a **planner–executor architecture**.  
The agent autonomously decomposes the user goal into smaller tasks and executes them using specialized tools while maintaining context through memory.

---

## Architecture

User Goal  
↓  
Planner (Task Decomposition)  
↓  
Executor  
↓  
Search Tool → Summarization Tool → Storage Tool  
↓  
Memory / Context Handling  
↓  
Structured JSON Output  

---

## Key Components

- **Agent (`agent.py`)**
  - Handles planning and execution
  - Orchestrates tool usage
  - Manages agent workflow

- **Search Tool (`tools.py`)**
  - Retrieves recent AI research papers related to agriculture

- **Summarization Tool (`tools.py`)**
  - Generates concise summaries for each research paper

- **Storage Tool (`tools.py`)**
  - Stores results in a structured JSON format

- **Memory (`memory.py`)**
  - Maintains intermediate context and results during execution

---

## Agent Workflow
1. The agent receives a high-level user goal.
2. The planner decomposes the goal into smaller tasks.
3. The executor invokes tools sequentially:
   - Search for research papers
   - Summarize selected papers
   - Store results
4. Memory is used to track intermediate outputs.
5. The final structured output is generated.

---

## Folder Structure
