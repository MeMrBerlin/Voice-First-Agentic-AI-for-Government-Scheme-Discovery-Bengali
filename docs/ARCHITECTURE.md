# Architecture Document: Voice-First Agentic AI System

## Overview
This system is a **voice-first, agentic AI assistant** designed to help users identify eligible
government welfare schemes using **Bengali voice interaction**.

The system is explicitly **not a chatbot** and follows a **Planner–Executor–Evaluator**
agent architecture with memory and tool usage.

---

## High-Level Architecture

User (Voice - Bengali)
        ↓
Speech-to-Text (Whisper)
        ↓
Agent Planner
        ↓
Agent Executor
        ↓
Tools
  ├── Eligibility Engine
  └── Scheme Database
        ↓
Agent Evaluator
        ↓
Conversation Memory
        ↓
Text-to-Speech (Bengali)
        ↓
User (Voice Output)

---

## Agent Lifecycle

### 1. Voice Input
- User speaks in Bengali.
- Speech is captured via microphone.
- Whisper converts speech to text.

### 2. Planning Phase
- Planner inspects conversation memory.
- Determines next missing information:
  - Age
  - Income
  - Occupation
  - State

### 3. Execution Phase
- Executor invokes tools:
  - Eligibility Engine to decide scheme key.
  - Scheme Database to fetch scheme details.

### 4. Evaluation Phase
- Evaluator checks tool outputs.
- Decides whether:
  - To return a successful scheme
  - To handle failure
  - To terminate the interaction

### 5. Memory Management
- User responses are stored across turns.
- Contradictions are detected and resolved.

---

## Tools Used

### Eligibility Engine
- Implemented as a modular tool.
- Determines scheme eligibility based on user profile.
- Designed to be replaceable by an ML model.

### Scheme Database
- Stores scheme details in Bengali.
- Includes benefits and required documents.

---

## Failure Handling
- Silence detection
- Unclear speech handling
- Invalid numeric input handling
- Graceful termination when no scheme applies

---

## Key Design Principles
- Voice-first interaction
- Native language support
- Explainable agent behavior
- Modular and scalable architecture
