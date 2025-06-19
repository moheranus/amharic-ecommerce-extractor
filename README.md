Amharic E-commerce Data Extractor
This repository contains the code and deliverables for the B5W4 Challenge: Building an Amharic E-commerce Data Extractor for EthioMart. The goal is to develop a system that extracts entities (e.g., products, prices, locations) from Ethiopian Telegram e-commerce channels and builds a vendor analytics engine for micro-lending.
Project Overview
EthioMart aims to consolidate Telegram-based e-commerce activities in Ethiopia into a centralized platform. This project involves:

Scraping data from Telegram channels.
Labeling Amharic text for Named Entity Recognition (NER).
Fine-tuning transformer-based models for NER.
Comparing models and interpreting predictions.
Creating a vendor scorecard for micro-lending.

Repository Structure

task-1-data-ingestion-preprocessing/: Scripts for scraping and preprocessing data.
task-2-conll-labeling/: Labeled dataset in CoNLL format.
task-3-ner-finetuning/: NER model fine-tuning code.
task-4-model-comparison/: Model comparison scripts.
task-5-model-interpretability/: SHAP/LIME analysis.
task-6-vendor-scorecard/: Vendor analytics engine.
docs/: PDF reports and documentation.
## Task 2: CoNLL Labeling
- **Scripts**: `scripts/select_messages.py`, `scripts/print_messages_for_labeling.py`, `scripts/auto_label_conll.py`, `scripts/validate_conll.py`
- **Functionality**: Selects 30 messages, applies rule-based labeling with manual review for NER (Product, Price, Location, Contact Info).
- **Output**: `samples/labeled_data.conll`
- **Usage**:
  ```bash
  python scripts/select_messages.py
  python scripts/print_messages_for_labeling.py
  python scripts/auto_label_conll.py
  python scripts/validate_conll.py



Setup Instructions

Clone the repository:git clone https://github.com/your-username/amharic-ecommerce-extractor.git
cd amharic-ecommerce-extractor


Install dependencies:pip install -r requirements.txt


Set up Telegram API credentials:
Register an app at my.telegram.org.
Save api_id and api_hash in a secure location (not committed).



Tasks

Data Ingestion & Preprocessing: Scrape 5+ Telegram channels, preprocess Amharic text.
CoNLL Labeling: Label 30–50 messages for NER.
NER Fine-Tuning: Fine-tune models like XLM-RoBERTa.
Model Comparison: Compare models based on F1-score, speed.
Model Interpretability: Use SHAP/LIME for prediction analysis.
Vendor Scorecard: Build analytics engine for vendor lending scores.

Deliverables

Interim Submission (June 22, 2025): GitHub link for Tasks 1–2, 1–2 page PDF summary.
Final Submission (June 24, 2025): Blog-style PDF, complete GitHub code.

Team
Tutors: Mahlet, Rediet, Kerod, Rehmet
License
MIT License
