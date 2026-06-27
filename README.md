# Cloud-Native Retail Data Lakehouse (Local Medallion Architecture)

## 📌 Project Overview
This project demonstrates the implementation of a modern, multi-stage **Data Lakehouse** using the **Medallion Architecture**. 

It handles raw e-commerce transaction tracking data (customers, products, and orders), processes it through automated programmatic cleaning scripts, and organizes it into an enterprise-grade **Star-Schema Data Warehouse**. The system uses a highly optimized columnar layout to maximize analytics query performance while maintaining strict data quality enforcement checks.

---

## 🏗️ System Architecture & Data Flow

The project structures data pipelines across three distinct quality zones:

1. **Bronze Layer (Raw Storage):** Unstructured, raw CSV files containing untreated operational e-commerce transaction data logs.
2. **Silver Layer (Conformed Storage):** A Python cleaning pipeline built on **DuckDB** reads the raw entries, drops null values, standardizes data types, fixes timestamp configurations, and exports data into highly compressed, columnar **Parquet files**.
3. **Gold Layer (Analytical Warehouse):** Using **dbt Core (Data Build Tool)**, conformed silver tables are modeled, joined, and compiled into production-ready analytical tables optimized for business intelligence queries.

---

## 🛠️ Tech Stack & Core Tools
* **Database Engine:** DuckDB (In-process analytical database management system)
* **Data Transformation & Modeling:** dbt Core (Data Build Tool)
* **File Formats:** Apache Parquet (Columnar storage optimization)
* **Languages:** SQL, Python 3.x
* **Database UI:** DBeaver

---

## 🗄️ Dimensional Modeling (Star Schema)

The final **Gold Layer** transformations restructure operational tracking tables into an analytical data model optimized for reporting efficiency:

* **Fact Table:** `fact_sales` (Tracks numeric transactions: order ID, quantities, order timestamps, and relational key identifiers).
* **Dimension Tables:** `dim_customers` (Tracks customer attributes, names, and profiles).

### Data Quality Assurance & Assertion Testing
Using native dbt testing blocks, data boundaries are protected automatically. The pipeline runs integrated quality assertions to continuously test for structural compliance:
* Enforces structural uniqueness constraints on critical business key indices (e.g., `order_id`).
* Validates `NOT NULL` compliance on essential structural data columns.

---

## 🚀 How to Run and Deploy Locally

### Prerequisites
* Python (3.8 or higher)

### 1. Install Project Requirements
Install the required analytical engines and data modeling packages:

```bash
pip install duckdb dbt-core dbt-duckdb