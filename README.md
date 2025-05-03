# Hadoop-ETL: Data Pipeline with Sqoop, Spark, and Terraform on GCP

This project demonstrates a complete ETL pipeline that moves data from a MySQL database to Hadoop Distributed File System (HDFS) using **Sqoop**, performs transformations using **Apache Spark**, and automates infrastructure provisioning using **Terraform** on **Google Cloud Platform (GCP)**.

---

## 📦 Components

### 1. Infrastructure Provisioning (Terraform)
Terraform scripts are used to provision:

- **Cloud SQL (MySQL) Instance**
- **Dataproc Cluster** (for HDFS, YARN, Spark)
- **Cloud Composer** (Apache Airflow for orchestration)
- **GCS Bucket** (for data and DAG storage)

### 2. Data Movement (Sqoop)
Sqoop scripts in [`src/sqoop_scripts`](https://github.com/shilu10/Hadoop-ETL/tree/master/src/sqoop_scripts) are used to:

- Import data from MySQL to HDFS.
- Export processed data from HDFS back to MySQL.

### 3. Data Processing (Spark)
Spark scripts in [`src/spark_scripts`](https://github.com/shilu10/Hadoop-ETL/tree/master/src/spark_scripts) perform:

- Data cleansing
- Transformations
- Aggregations on data stored in HDFS.

### 4. Query Execution (Hive HQL)
Hive queries in [`src/hql_scripts`](https://github.com/shilu10/Hadoop-ETL/tree/master/src/hql_scripts) are used for:

- Creating external tables
- Querying data from HDFS

---

## ⚙️ GitHub Actions CI/CD

- **Trigger**: On push to `master`
- **Steps**:
  - Setup Terraform
  - `terraform init`, `fmt`, `plan`, `apply`
  - Deploy infrastructure
  - Add SSH metadata to Dataproc Master

File: [`.github/workflows/terraform.yml`](https://github.com/shilu10/Hadoop-ETL/blob/master/.github/workflows/terraform.yml)

---

## 🌐 GCP Integration

- Cloud SQL credentials and SSH keys are handled using GitHub secrets:
  - `GOOGLE_CREDENTIALS`
  - `GCP_PROJECT_ID`
  - `INSTANCE_PUBLIC_KEY`

---
