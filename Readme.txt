# StreamSphere Analytics

## 📊 End-to-End Data Analyst Portfolio Project

StreamSphere Analytics is an end-to-end data analytics project for a fictional streaming platform. The project analyzes customer acquisition, subscription behavior, churn, revenue performance, marketing effectiveness, content engagement, and customer value.

The project demonstrates the complete workflow of a Data Analyst:

**SQL Server → Data Validation → Python EDA → Data Visualization → Power BI Dashboard → Business Insights → Recommendations**

---

## 🎯 Business Objectives

The project aims to answer the following business questions:

- How are customers distributed across countries and regions?
- Which acquisition channels bring in the most customers?
- Which subscription plans are most popular?
- What is the overall churn rate?
- Why are customers cancelling their subscriptions?
- Which subscription plans generate the most revenue?
- Which countries generate the most revenue?
- How does revenue change over time?
- Which content receives the highest engagement?
- Which countries have the highest watch engagement?
- Which marketing campaigns have the highest conversion rates?
- Which customers generate the highest revenue?

---

## 🛠️ Tools & Technologies

- **SQL Server / SSMS** — Database management and SQL analysis
- **SQL** — Data exploration and validation
- **Python** — Data analysis and validation
- **Pandas** — Data manipulation
- **NumPy** — Numerical analysis
- **Matplotlib** — Data visualization
- **Seaborn** — Statistical visualization
- **Power BI** — Interactive dashboard and business reporting
- **Jupyter Notebook** — Python analysis environment

---

## 🗂️ Dataset

The project contains 8 relational datasets:

| Dataset | Description |
|---|---|
| Customers | Customer demographic and acquisition information |
| Subscriptions | Subscription plans, status and cancellations |
| Transactions | Payment and revenue transactions |
| User Events | Customer content interaction and engagement |
| Content | Movies and series information |
| Subscription Plans | Plan pricing and features |
| Marketing Campaigns | Campaign cost, impressions, clicks and conversions |
| Geography | Country, region and currency information |

### Dataset Size

| Table | Rows |
|---|---:|
| Customers | 50,000 |
| Subscriptions | 60,000 |
| Transactions | 200,000 |
| User Events | 500,000 |
| Content | 5,000 |
| Marketing Campaigns | 10 |
| Subscription Plans | 3 |
| Geography | 8 |

---

## 🗄️ SQL Analysis

SQL Server was used to create the relational database, establish primary and foreign keys, validate data integrity, and perform exploratory analysis.

### SQL files

```text
sql/
├── 01_create_tables.sql
├── 02_eda.sql
└── 03_data_validation.sql