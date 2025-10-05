# Ensuring Consistency in Knowledge Bases with Generative AI

## 📘 Overview
This repository contains a **Generative AI pipeline for detecting contradictions** in unstructured company text data.  
It integrates **Large Language Models (LLMs)**, **vector databases**, and **semantic similarity search** to automatically identify conflicting or inconsistent information within document collections.

The system combines fine-tuned transformer models with embedding-based retrieval and large-model reasoning to enhance data quality and consistency in organizational information systems.

---

## 🧩 Objectives
- Detect and classify contradictions in large text corpora.  
- Fine-tune a laguage model on domain-specific data.  
- Use a vector database for scalable semantic similarity matching.  
- Apply an LLM to validate and correct uncertain classifications.

---

## ⚙️ System Architecture
The **Contradiction Detection (CD) Pipeline** includes the following core components:

1. **Data Preparation** – Generates a domain-specific contradiction dataset using an LLM.  
2. **Fine-Tuned Classifier** – A RoBERTa model trained on multi-label contradiction types (antonymy, negation, numeric, lexical, world knowledge, etc.).  
3. **Vector Database Integration** – Embeds documents using an embedding model and stores them in **ChromaDB** for similarity-based retrieval.  
4. **Similarity Search** – Finds related sentence pairs across documents that potentially refer to the same entities or timeframes, a prerequisite for contradictions.  
5. **LLM Refiner** – A large language model (e.g., Llama 3) re-evaluates or refines uncertain predictions for higher-level semantic validation.

---

## 🧠 Methodology
The pipeline combines classic contradiction detection techniques with modern generative AI components:

- **Sentence Embedding & Search:** Vector representations enable scalable semantic pairing of potentially contradictory statements.  
- **Transformer-Based Classification:** Fine-tuned RoBERTa models perform contradiction classification.  
- **Generative Validation:** LLMs resolve ambiguous or context-dependent contradictions.  
- **Hybrid Evaluation:** Results are benchmarked on both generated and real-world company text data.

---

## 📊 Key Results
- Automatically generated a **domain-specific contradiction dataset** with over **3,400 labeled sentence pairs**.  
- Fine-tuned RoBERTa-base achieved **≈81 % accuracy** across 11 contradiction labels.  
- Simplified 3-class setup (entailment / neutral / contradiction) reached **94–97 % accuracy**.  
- Embedding-based search efficiently identified related text pairs for contradiction testing.  
- LLM reasoning improved accuracy for complex contradiction types such as *world knowledge* and *factive* inconsistencies.
