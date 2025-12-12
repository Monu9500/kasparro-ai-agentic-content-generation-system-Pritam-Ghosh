# Kasparro - Multi-Agent Content Generation System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-Orchestration-green)
![Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange)
![Pydantic](https://img.shields.io/badge/Validation-Pydantic-red)

A production-grade, agentic automation system designed to transform unstructured product data into structured, machine-readable web content (JSON). This project demonstrates the use of **LangChain** for orchestration and **Pydantic** for strict schema validation.
## Features

* **Multi-Agent Architecture:** Distinct agents for Content Generation, Product Analysis, and Competitor Comparison.
* **LangChain Orchestration:** Utilizes `LCEL` (LangChain Expression Language) for robust prompt management and chaining.
* **Strict JSON Validation:** Uses Pydantic schemas to ensure 100% valid, type-safe output suitable for frontend integration.
* **Modular Design:** Clean separation between Data, Logic, Schemas, and Agents.
* **Cost-Effective:** Powered by Google's Gemini 1.5 Flash model for high-speed inference.

## Project Structure

kasparro-ai-agentic-content-generation-system/
├── agents.py             
├── data.py               
├── logic.py             
├── main.py               
├── models.py            
├── requirements.txt      
├── projectdocumentation.md 
└── README.md            
