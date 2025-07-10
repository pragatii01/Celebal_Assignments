# 📊 Change Data Capture (CDC) Pipeline using Azure Data Factory & Databricks

This project implements a **Change Data Capture (CDC)** pipeline using:
- **Azure SQL Server** (as the source system),
- **Azure Data Factory** (as orchestrator), and
- **Azure Databricks** (for transformation and storage in Delta Lake format).

---

## 🎯 Objective

To track and process **Insert**, **Update**, and **Delete** operations on source SQL tables using CDC, and store the transformed data in **Delta Lake format** for downstream analytics.

---

## 🗂 Project Structure

CDC_Project/
├── databricks_notebooks/
│ └── CDC_SQL_to_Delta.py # PySpark notebook to process CDC and write to Delta
├── sql_scripts/
│ └── create_tables.sql # SQL script to create & enable CDC on source tables
├── adf_arm_template/
│ ├── ARMTemplateForFactory.json # Main ARM template for ADF resources
│ ├── ARMTemplateParametersForFactory.json # Deployment parameters (fill in before deploy)
│ └── linkedTemplates/
│ └── armTemplate_0.json # Child template for linked deployment
├── .env # Contains ngrok & SQL credentials (optional)
├── README.md # Project documentation


---

## 🛠 Technologies Used

- Azure SQL Server
- Azure Data Factory
- Azure Databricks
- Delta Lake (Spark + Parquet)
- PySpark
- ARM Templates (Infra-as-Code)

---
## 🧱 Architecture Overview

SQL Server (Local)
⬇ (via ngrok + JDBC)
Databricks Notebook (CDC Logic in PySpark)
⬇
Delta Table (Databricks / DBFS)
⬇ (Optional)
ADF Pipeline (Trigger Notebook via REST API or native activity)


---

## 🔁 CDC Workflow Steps

1. ✅ Create tables in SQL Server: Customer, Product, Order, Inventory.
2. ✅ Enable and simulate CDC (manually track changes).
3. ✅ Use ngrok to expose your local SQL Server to the public securely.
4. ✅ Create a Databricks Notebook to:
   - Read SQL Server data via JDBC
   - Detect new/updated/deleted rows
   - Write Delta output to `/tmp/customer_cdc_delta`
5. ✅ Validate Delta Lake output in Databricks.
6. ✅ (Optional) Create ADF Pipeline to:
   - Trigger the CDC notebook
   - Schedule the CDC job to run hourly or daily.

---

## ✅ Project Completion Checklist

| Step | Task Description | Status |
|------|------------------|--------|
| 1️⃣ | Defined project objective & architecture | ✅ Done |
| 2️⃣ | Created SQL Server tables | ✅ Done |
| 3️⃣ | Created Self-hosted IR & Linked Services in ADF | ✅ Done |
| 4️⃣ | Created Databricks workspace & notebook | ✅ Done |
| 5️⃣ | Connected via JDBC using ngrok | ✅ Done |
| 6️⃣ | Loaded and transformed data into Delta format | ✅ Done |
| 7️⃣ | Tested and validated manually | ✅ Done |
| 8️⃣ | Created optional ADF pipeline to trigger notebook | 🔁 Optional |
| 9️⃣ | Scheduled hourly CDC refresh (trigger) | 🔁 Optional |

---


## 📝 How to Run This Project

1. Clone the repository:
   ```bash
   git clone https://github.com/pragatii01/Celebal_Assignments.git

2. Navigate to the CDC project directory:
   cd Celebal_Assignments/CDC_Project
   
4. Open and configure .env with your:

   - SQL Server credentials

   - JDBC connection string

   - Ngrok auth token (if used)

5. Run the CDC notebook manually in Databricks or via ADF.



📃 License
This project is submitted as part of the Celebal Internship Assignments and is for educational/demo purposes only.

---

### ✅ Next Step:
Let me know if you want me to:
- Create this structure locally as `.md` files and scripts
- Help you push everything to your GitHub repo

Ready to finish strong! 💪
