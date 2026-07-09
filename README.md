# 🏠 Real Estate Data Warehouse Pipeline

A complete **Data Engineering & Business Intelligence** project implementing a **Medallion Architecture (Bronze, Silver, Gold)** using **Snowflake**, **dbt**, **Apache Airflow**, and **Power BI**.

---

# 📖 Project Overview

This project aims to design and implement an end-to-end Data Warehouse for worldwide real estate data.

The pipeline performs the following tasks:

- Import raw real estate data from a CSV file.
- Load raw data into the Bronze layer in Snowflake.
- Clean and transform data using dbt in the Silver layer.
- Build a dimensional model (Star Schema) in the Gold layer.
- Orchestrate the workflow using Apache Airflow.
- Visualize business insights with Power BI.

---

# 🛠️ Technologies Used

- 🐍 Python
- ❄️ Snowflake
- 🌱 dbt
- 🔄 Apache Airflow
- 🐳 Docker
- 📊 Power BI
- 🌐 Git & GitHub

---

# 📁 Project Structure

```text
real-estate-data-warehouse/
│
├── .vscode/
│   └── settings.json
│
├── dags/
│   ├── __pycache__/
│   ├── dag.py
│   └── data/
│       └── real-estate-raw.csv
│
├── dbt/
│   ├── logs/
│   │   └── dbt.log
│   │
│   ├── models/
│   │   ├── gold/
│   │   ├── silver/
│   │   └── sources.yml
│   │
│   ├── target/
│   ├── profiles.yml
│   ├── dbt_project.yml
│   └── user.yml
│
├── docs/
│   ├── Architecture_globale_du_projet.pdf
│   └── Documentation_qualite_des_donnees.pdf
│
├── logs/
│   ├── dag_id_real_estate_pipeline/
│   ├── dag_processor_manager/
│   ├── scheduler/
│   └── dbt.log
│
├── macros/
│   └── generate_schema_name.sql
│
├── python/
│   ├── __pycache__/
│   └── load_bronze.py
│
├── target/
│   ├── compiled/
│   ├── run/
│   ├── manifest.json
│   ├── graph_summary.json
│   └── run_results.json
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🏗️ Pipeline Architecture

```text
                     real-estate-raw.csv
                              │
                              ▼
                 Python Ingestion Script
                 (python/load_bronze.py)
                              │
                              ▼
                 Snowflake Bronze Layer
                  Raw Listings Table
                 + _loaded_at metadata
                              │
                     dbt Silver Models
                              │
                              ▼
                 Snowflake Silver Layer
         Data Cleaning & Standardization
     • Remove duplicates
     • Handle missing values
     • Correct data types
     • Normalize text values
     • Price per m²
     • Property Age
                              │
                      dbt Gold Models
                              │
                              ▼
                  Snowflake Gold Layer
                 Star Schema Data Warehouse
                              │
                              ▼
               Apache Airflow Orchestration
                     (dags/dag.py)
                              │
                              ▼
                 Power BI Interactive Dashboard
```

---

# 🥉 Bronze Layer

The Bronze layer stores the raw dataset exactly as received.

### Tasks

- Load CSV into Snowflake
- Preserve original data
- Add `_loaded_at` timestamp
- Ensure complete traceability

---

# 🥈 Silver Layer

The Silver layer cleans and enriches the raw data using dbt.

### Data Cleaning

- Remove duplicate records
- Handle missing values
- Convert incorrect data types
- Normalize property types
- Standardize parking values
- Standardize heating types
- Parse inconsistent dates
- Remove unrealistic prices
- Remove invalid surface values

### Derived Columns

- Price per m²
- Property Age

---

# 🥇 Gold Layer

The Gold layer contains a **Star Schema** optimized for analytical reporting.

### Fact Table

- FACT_LISTINGS

### Dimension Tables

- DIM_LOCATION
- DIM_PROPERTY
- DIM_DATE
- DIM_ENERGY

---

# 🔄 Apache Airflow

Apache Airflow orchestrates the entire ETL pipeline.

### Workflow

1. Load CSV into Bronze.
2. Execute dbt Silver models.
3. Execute dbt Gold models.
4. Verify execution.
5. Generate execution logs.

### Features

- Automatic retries
- Error handling
- Logging
- Task dependencies

---

# 📊 Power BI Dashboard

The dashboard is connected directly to the Gold schema in Snowflake.

## 📌 Page 1 — Market Overview

- Total Listings
- Average Price
- Average Surface
- Listings by Country
- Property Type Distribution

---

## 📌 Page 2 — Price Analysis

- Average Price by Country
- Average Price by City
- Median Price per m²
- Price Distribution
- Price Trend Over Time

---

## 📌 Page 3 — Property Analysis

- Surface Distribution
- Energy Rating Distribution
- Average Property Age
- Parking Availability
- City Summary Table

---

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/nohasabb2005-spec/real-estate-data-warehouse.git
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run dbt

```bash
dbt run
```

Run tests

```bash
dbt test
```

---

# ▶️ Start Apache Airflow

```bash
docker compose up -d
```

Open Airflow

```
http://localhost:8080
```

Run the DAG

```
real_estate_pipeline
```

---

# 📦 Deliverables

- ✅ GitHub Repository
- ✅ Snowflake Data Warehouse
- ✅ Bronze Layer
- ✅ Silver Layer
- ✅ Gold Layer
- ✅ dbt Models
- ✅ Apache Airflow Pipeline
- ✅ Power BI Dashboard
- ✅ Technical Documentation

---

# 👥 Team Members

- Manal Bessar
- Nouhaila Sabbar
- Fatima Ezzahra Derrag
- Salma El yamani
---

# 📄 License

This project was developed for educational purposes as part of the **INT-Maroc Data Analyst Training Program**.
