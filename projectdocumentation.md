# Project Documentation: Multi-Agent Content Generation System

## 1. Problem Statement
The objective of this project is to design and implement a modular agentic automation system capable of transforming raw, unstructured product data into structured, machine-readable web content. The challenge addresses the need for scalable content generation where manual copywriting is inefficient. [cite_start]The system must autonomously generate FAQ pages, Product Description pages, and Comparison pages without human intervention, ensuring strict JSON output formats [cite: 172-179].

## 2. Solution Overview
The solution is a **LangChain-based Agentic System** built in Python. Unlike basic scripts that rely on manual string parsing, this system leverages industry-standard frameworks to ensure robustness and scalability.

**Key Components:**
* [cite_start]**Orchestration Framework:** **LangChain** is used to manage agent workflows, replacing custom `client` calls with structured Chains [cite: 235-238].
* [cite_start]**Schema Validation:** **Pydantic** is used to define strict data models, guaranteeing that the AI's output is always valid, parseable JSON [cite: 254-255].
* **LLM Inference:** Utilizes **Google Gemini Flash** via the `langchain-google-genai` adapter for high-speed, cost-effective text generation.
* [cite_start]**Logic Layer:** Dedicated reusable functions (Logic Blocks) handle pre-processing and data extraction before the AI is even invoked [cite: 242-243].

## 3. Scopes & Assumptions
* **Scope:** The system generates three specific page types: FAQ, Product Detail, and Competitor Comparison.
* **Input Assumption:** The input data is assumed to be text-based key-value pairs (as provided in the GlowBoost dataset).
* **Output Assumption:** All outputs are strictly valid JSON for consumption by a frontend application.
* **Technology Stack:** Python 3.10+, LangChain, Pydantic, Google Generative AI.

## 4. System Design
The architecture follows a **Modular Agent Factory Pattern**.
[FLOWCHART :](https://drive.google.com/file/d/1P57MMD9DKwASa6uHgJ4invSGSPtN9HBL/view?usp=drivesdk) 

### 4.1 High-Level Architecture
1.  **Main (Orchestrator):** The entry point. It initializes the `AgentFactory` and triggers specific pipelines based on the required output.
2.  [cite_start]**Logic Layer (`logic.py`):** A collection of deterministic "Logic Blocks" that clean data, extract specs, and define static competitor info *before* the AI processes it [cite: 242-246].
3.  **Agent Layer (`agents.py`):** Uses LangChain to define "Chains". Each chain consists of:
    * **PromptTemplate:** Instructions with dynamic variables.
    * **LLM:** The Google Gemini Model.
    * **JsonOutputParser:** A parser injected with Pydantic schemas to enforce structure.
4.  **Schema Layer (`models.py`):** Defines the "Contract" for the output using Pydantic classes (`FAQPage`, `ProductPage`).

### 4.2 Automation Flow
The system uses a Linear Chain of Execution managed by the main script:

1.  **Ingestion:** Raw text is loaded from `data.py`.
2.  **Pre-processing:** `logic.py` extracts key specs and loads competitor data.
3.  **Agent Execution:**
    * *FAQ Agent:* Receives data -> LangChain Prompt -> LLM -> Pydantic Validation -> `faq.json`
    * *Product Agent:* Receives data -> LangChain Prompt -> LLM -> Pydantic Validation -> `product_page.json`
    * *Comparison Agent:* Receives User & Competitor data -> LangChain Prompt -> LLM -> Pydantic Validation -> `comparison_page.json`

### 4.3 Key Design Decisions
* **Adoption of LangChain:** Shifted from a custom script to the **LangChain Framework** to standardize orchestration and prompt management. [cite_start]This avoids "reinventing the wheel" and ensures the system is extensible[cite: 4, 166].
* **Pydantic for Validation:** Instead of hoping the AI writes valid JSON, we inject Pydantic schemas directly into the prompt instructions. This guarantees type safety (e.g., ensuring "Price" is always a string/number as defined).
* [cite_start]**Reusable Logic Blocks:** Static logic (like defining a competitor) is moved to `logic.py` to keep the Agent code pure and focused only on inference[cite: 242].

## 5. Folder Structure
The project is organized modules to ensure separation of concerns:

kasparro-ai-agentic-content-generation-system/
├── agents.py             # LangChain definitions & AgentFactory
├── data.py               # Raw input data repository
├── logic.py              # Reusable logic blocks & helper functions
├── main.py               # Orchestrator script
├── models.py             # Pydantic schemas (JSON Templates)
├── requirements.txt      # List of dependencies (LangChain, etc.)
├── README.md             # Setup instructions
├── projectdocumentation.md  # Architecture documentation
├── faq.json              # Generated Output
├── product_page.json     # Generated Output
└── comparison_page.json  # Generated Output