# 📊 StreamSphere Analytics

### End-to-End Data Analytics Project | SQL Server • Python • Power BI

> An end-to-end data analytics project analyzing customer acquisition, subscriptions, churn, revenue, marketing performance, and user engagement for a fictional global streaming platform.

---

## 🚀 Project Overview

**StreamSphere Analytics** is an end-to-end Data Analyst portfolio project built to simulate a real-world business analytics environment.

The project covers the complete analytics workflow:

**Raw Data → SQL Database → Data Validation → Exploratory Data Analysis → Python Analysis → Power BI Dashboard → Business Insights & Recommendations**

The objective is to transform raw operational data into actionable insights that can help a streaming business improve **customer retention, revenue, acquisition efficiency, and user engagement**.

---

## 🎯 Business Objectives

The analysis focuses on answering key business questions:

- Which countries generate the most customers and revenue?
- Which marketing channels acquire the most customers?
- Which campaigns have the highest conversion rates?
- Which subscription plans generate the most revenue?
- What is the overall customer churn rate?
- Which subscription plans have the highest churn?
- Why are customers cancelling their subscriptions?
- How is revenue changing over time?
- Which content receives the most engagement?
- Which countries have the highest user engagement?
- What are the highest-value customers?
- How can the business improve retention and revenue?

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| **SQL Server / SSMS** | Database creation, SQL analysis & validation |
| **SQL** | EDA, joins, aggregations, CTEs & window functions |
| **Python** | Data analysis & validation |
| **Pandas** | Data manipulation & analysis |
| **NumPy** | Numerical analysis |
| **Matplotlib** | Data visualization |
| **Seaborn** | Statistical visualization |
| **Power BI** | Interactive dashboard |
| **DAX** | Business KPIs & calculations |
| **GitHub** | Project documentation & version control |

---

## 📂 Dataset

The project contains **8 interconnected datasets** with more than **815,000 records**.

| Dataset | Records | Description |
|---|---:|---|
| Customers | 50,000 | Customer demographics & acquisition |
| Subscriptions | 60,000 | Subscription history & status |
| Transactions | 200,000 | Revenue & payment transactions |
| User Events | 500,000 | User activity & engagement |
| Content | 5,000 | Movies & series metadata |
| Marketing Campaigns | 10 | Campaign performance |
| Subscription Plans | 3 | Pricing & plan information |
| Geography | 8 | Country, region & currency |

**Total Records: 815,021**

---

# 🗄️ SQL Analysis

The SQL analysis was performed using **Microsoft SQL Server**.

### Database Design

The database contains:

- Primary Keys
- Foreign Keys
- One-to-many relationships
- Referential integrity checks
- Data quality validation

### SQL Analysis Covered

- Customer distribution by country
- Customer distribution by region
- Acquisition by marketing campaign
- Acquisition by marketing channel
- Acquisition by country & channel
- Subscription plan popularity
- Active vs cancelled subscriptions
- Subscription status by plan
- Cancellation reasons
- Churn rate by plan
- Total revenue
- Average transaction value
- Revenue by subscription plan
- Revenue by country
- Monthly revenue trends
- Content popularity
- Customer engagement
- Event analysis
- Watch duration analysis
- Marketing conversion rates
- Customer Lifetime Value
- Customer revenue ranking using window functions

---

# 🐍 Python Analysis

Python was used for exploratory data analysis and data validation.

### Analysis Areas

**Customer Analysis**
- Demographics
- Geographic distribution
- Acquisition channels
- Signup trends
- Age distribution

**Subscription Analysis**
- Active vs cancelled subscriptions
- Churn analysis
- Subscription plans
- Cancellation reasons

**Revenue Analysis**
- Total successful revenue
- Average transaction value
- Revenue by country
- Revenue by subscription plan
- Transaction performance

**Engagement Analysis**
- Event types
- Watch duration
- Device usage
- Content engagement

**Marketing Analysis**
- Campaign performance
- Conversion rates
- Customer acquisition

---

# 📊 Power BI Dashboard

The project includes a **4-page interactive Power BI dashboard**.

### 1️⃣ Executive Overview

Provides a high-level view of business performance.

**KPIs include:**
- Total Customers
- Total Revenue
- Total Subscriptions
- Active Subscriptions
- Churn Rate
- Average Transaction Value

---

### 2️⃣ Customer & Acquisition

Analyzes:

- Customer distribution by country
- Acquisition channels
- Country × acquisition channel
- Gender distribution
- Customer acquisition trends
- Age distribution

---

### 3️⃣ Subscription & Churn

Analyzes:

- Active vs cancelled subscriptions
- Subscription plans
- Churn rate by plan
- Cancellation reasons
- Cancellation reasons by plan
- Subscription status by plan

---

### 4️⃣ Revenue & Engagement

Analyzes:

- Revenue by country
- Revenue by subscription plan
- User engagement by event type
- Watch engagement by country
- Transaction performance by payment method
- Top 10 content by engagement

---

# 📈 Key Business Insights

### 💰 Revenue

**$2.26M** in successful transaction revenue was generated.

The **Standard subscription plan** generated the highest revenue.

### 👥 Customer Acquisition

**Instagram** was the leading customer acquisition channel with more than **10K customers acquired**.

### 📉 Churn

The overall subscription churn rate was approximately **34.86%**.

The **Basic plan** showed the highest cancellation rate, while the **Premium plan** had the lowest.

### ❌ Cancellation

**"Too Expensive"** was the most common cancellation reason.

### 📣 Marketing

The **Email Re-engagement** campaign achieved the highest conversion rate at **20%**.

### 🌎 Geography

The **United States** generated the highest revenue among the analyzed markets.

### 🎬 Engagement

**Play** was the most frequently recorded user event, representing the largest component of user activity.

---

# 💡 Business Recommendations

Based on the analysis:

### 1. Improve Customer Retention

Investigate pricing concerns and introduce targeted retention offers for customers showing cancellation signals.

### 2. Review Basic Plan Pricing

The Basic plan has the highest churn rate, suggesting an opportunity to review its pricing and value proposition.

### 3. Strengthen High-Performing Marketing Channels

Continue investing in high-performing acquisition channels while evaluating campaign-level conversion efficiency.

### 4. Expand Email Re-engagement

The strongest campaign conversion rate came from Email Re-engagement, suggesting potential for additional retention and reactivation campaigns.

### 5. Focus on High-Value Markets

The United States and other high-revenue markets should receive targeted retention and monetization strategies.

### 6. Use Engagement Data

Content and user-event data can be used to identify highly engaged customers and personalize content recommendations.

---

# 🔎 Data Quality & Validation

Data quality checks were performed across the datasets.

Validation included:

- NULL checks
- Duplicate primary-key checks
- Foreign-key integrity
- Negative-value checks
- Date validation
- Business-rule validation
- Transaction validation

### Validation Result

✅ No key-column NULL values  
✅ No duplicate primary keys  
✅ No broken foreign-key relationships  
✅ No negative financial values  
✅ No invalid subscription date ranges  

**5 transaction-date anomalies** were identified where successful transactions occurred shortly before the associated subscription start date.

These records were **retained and documented rather than removed**, preserving the original dataset while maintaining transparency.

---

# 🏗️ Project Structure

```text
StreamSphere-Analytics/
│
├── README.md
│
├── data/
│   └── README.md
│
├── sql/
│   ├── 01_create_tables.sql
│   ├── 02_eda.sql
│   └── 03_data_validation.sql
│
├── notebooks/
│   └── 01_python_eda.ipynb
│
├── powerbi/
│   └── StreamSphere_Analytics.pbix
│
├── reports/
│   └── dashboard_screenshots/
│       ├── executive_overview.png
│       ├── customer_acquisition.png
│       ├── subscription_churn.png
│       └── revenue_engagement.png
│
└── requirements.txt
