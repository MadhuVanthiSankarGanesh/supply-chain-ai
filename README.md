# 🚢 AI Supply Chain Intelligence Platform

An **end-to-end intelligent supply chain monitoring system** that leverages **Databricks, Azure OpenAI, and real-time data streams** to provide actionable insights into global logistics risks and disruptions.

## 🌐 Overview
This platform integrates **machine learning, natural language processing, and geospatial analytics** to assess and visualize supply chain vulnerabilities. It continuously monitors real-world events—such as natural disasters, political instability, and trade disruptions—to support data-driven logistics decision-making.

---

## ✨ Key Features
- 🤖 **AI-Powered Risk Analysis** — Automated detection and classification of supply chain risks using Azure OpenAI and LangChain.  
- 🗺️ **Interactive Route Analysis** — Real-time mapping of supply routes with geospatial visualization and risk overlays.  
- 📊 **Dynamic Dashboards** — Streamlit-powered dashboards for intuitive monitoring of key metrics.  
- 🌪️ **Disaster Intelligence** — Integration with GDACS and GNews APIs for live natural disaster and news event tracking.  
- 📄 **Automated Reporting** — Generates daily and on-demand analytical summaries for stakeholders.

---

## 🧠 Tech Stack & Expertise

### 💻 Data Engineering & Processing
- **Azure Databricks** — End-to-end data pipelines for ingestion, transformation, and feature engineering.  
- **Delta Lake** — Unified batch and streaming data storage with version control.  
- **PySpark** — Scalable data processing for multi-source integration and transformation.  

### 🤖 Artificial Intelligence & Analytics
- **Azure OpenAI + LangChain** — Risk analysis and event summarization using LLMs.  
- **MLflow** — Experiment tracking and model management on Databricks.  
- **Pandas / NumPy** — Lightweight data wrangling and analytics during exploratory phases.

### 🧱 Cloud Infrastructure
- **Azure Cloud** — Data orchestration, model deployment, and environment scalability.  
- **Databricks Notebooks** — Modularized workflows for each pipeline stage:
  - `01_Environment_Setup.ipynb` — Cluster setup and environment configuration  
  - `02_Data_Ingestion_Pipeline.ipynb` — Data ingestion and Delta Lake integration  
  - `03_FeatureEngineering_RiskAnalysis.ipynb` — Feature engineering and ML-based risk computation  

### 🌍 APIs & Real-Time Data
- **GDACS API** — Natural disaster alerts and event metadata.  
- **GNews API** — News-based supply chain event extraction and sentiment tagging.  

### 🎨 Visualization & Deployment
- **Streamlit** — Interactive visualization and deployment of AI dashboards.  
- **Plotly / Altair** — Advanced analytics and geospatial visualizations.  

---

## 🚀 Live Demo
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://supply-chain-ai-smchpstajndwkv8jjb6zwq.streamlit.app/)

---

## 🧩 Project Workflow
1. **Environment Setup** — Configure Databricks workspace, clusters, and data mounts.  
2. **Data Ingestion** — Collect and clean data from GDACS, GNews, and structured sources.  
3. **Feature Engineering** — Extract risk indicators and compute risk scores per route or supplier.  
4. **AI Risk Analysis** — Apply LLM-based summarization and predictive models.  
5. **Visualization** — Display interactive insights via Streamlit dashboard.  
6. **Automation** — Generate daily reports and refresh dashboards with new data.

---

## ⚙️ Local Development
```bash
pip install -r requirements.txt
streamlit run enhanced_streamlit_app.py
