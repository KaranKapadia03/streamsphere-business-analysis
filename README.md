# 📊 StreamSphere Analytics

### End-to-End Data Analyst Portfolio Project

**SQL Server • SQL • Python • Pandas • NumPy • Matplotlib • Seaborn • Power BI • DAX**

> An end-to-end analytics project built around a fictional global streaming platform to analyze customers, acquisition, subscriptions, churn, revenue, marketing performance, content, and user engagement.

---

## 📌 Project Overview

StreamSphere Analytics simulates a real-world data analytics project for a global streaming platform.

### Project Workflow

```text
Raw CSV Data
      ↓
Python Data Generation
      ↓
SQL Server Database
      ↓
Data Validation
      ↓
SQL Exploratory Data Analysis
      ↓
Python Exploratory Data Analysis
      ↓
Power BI Data Model
      ↓
DAX Measures
      ↓
Interactive Dashboard
      ↓
Business Insights & Recommendations
```

---

## 🎯 Business Objectives

- Analyze customer acquisition and demographics
- Understand subscription performance
- Measure customer churn
- Identify cancellation reasons
- Analyze revenue and payment performance
- Evaluate marketing campaigns and conversion
- Measure content and user engagement
- Identify high-value customers
- Develop business recommendations

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Microsoft SQL Server | Relational database |
| SQL | Data analysis, EDA and validation |
| Python | Data generation, analysis and validation |
| Pandas | Data manipulation |
| NumPy | Numerical analysis |
| Matplotlib | Visualization |
| Seaborn | Statistical visualization |
| Power BI | Interactive dashboard |
| DAX | KPIs and business measures |
| GitHub | Version control and portfolio |

---

# 📂 Dataset

The project contains **8 interconnected datasets** with **815,021 records**.

| Dataset | Records | Description |
|---|---:|---|
| `customers` | 50,000 | Customer demographics and acquisition |
| `subscriptions` | 60,000 | Subscription history, status and cancellations |
| `transactions` | 200,000 | Payment and revenue transactions |
| `user_events` | 500,000 | User activity and content engagement |
| `content` | 5,000 | Movies and series metadata |
| `marketing_campaigns` | 10 | Campaign performance |
| `subscription_plans` | 3 | Subscription pricing and features |
| `geography` | 8 | Country, region and currency |
| **TOTAL** | **815,021** | |

---

# 📊 Power BI Dashboard

The project contains a 4-page interactive Power BI dashboard.

## 1️⃣ Executive Overview

![Executive Overview](./dashboard/Executive%20Overview.png)

**Includes:** Total Customers, Total Revenue, Total Subscriptions, Active Subscriptions, Churn Rate, Average Transaction Value, Customers by Country, Acquisition by Channel, Revenue by Plan, Subscription Status and Monthly Revenue Trend.

## 2️⃣ Customer & Acquisition

![Customer & Acquisition](./dashboard/Customer%20%26%20Acquisition.png)

**Includes:** Customers by Country, Acquisition by Channel, Country × Acquisition Channel, Gender Distribution, Monthly Customer Acquisition Trend and Age Distribution.

## 3️⃣ Subscription & Churn

![Subscription & Churn](./dashboard/Subscription%20%26%20Churn.png)

**Includes:** Subscription Status, Subscriptions by Plan, Churn Rate by Plan, Cancellation Reasons, Cancellation Reasons by Plan and Subscription Status by Plan.

## 4️⃣ Revenue & Engagement

![Revenue & Engagement](./dashboard/Revenue%20%26%20Engagement.png)

**Includes:** Revenue by Country, Revenue by Subscription Plan, User Engagement by Event Type, Watch Engagement by Country, Transaction Performance by Payment Method and Top 10 Content by Engagement.

---

# 🗄️ SQL Analysis

SQL Server was used to create the relational database, establish relationships, validate the data and perform exploratory analysis.

## SQL Concepts Demonstrated

`SELECT` `WHERE` `DISTINCT` `ORDER BY` `TOP` `GROUP BY` `HAVING` `CASE` `COUNT` `SUM` `AVG` `MIN` `MAX` `JOINs` `Subqueries` `CTEs` `Window Functions` `RANK()` `CAST()` `NULLIF()` `ISNULL()` `Date Functions` `Views` `Primary Keys` `Foreign Keys`

---

# ❓ SQL Business Questions, Queries & Answers

## 👥 Customer Analysis

### Q1. Which countries have the highest number of customers?

```sql
SELECT country, COUNT(*) AS [Number of Customers]
FROM dbo.customers
GROUP BY country
ORDER BY [Number of Customers] DESC;
```

**Answer:** The United States has the largest customer base, followed by India and the United Kingdom.

### Q2. Which regions have the highest number of customers?

```sql
SELECT g.region, COUNT(*) AS [Region Members]
FROM dbo.customers AS c
LEFT JOIN dbo.geography AS g ON c.country = g.country
GROUP BY g.region
ORDER BY [Region Members] DESC;
```

**Answer:** This compares customer concentration across geographic regions.

### Q3. Which marketing campaigns acquired the most customers?

```sql
SELECT mc.campaign_name, COUNT(*) AS [Number of Customers Acquired]
FROM dbo.customers AS c
LEFT JOIN dbo.marketing_campaigns AS mc
    ON c.campaign_id = mc.campaign_id
GROUP BY mc.campaign_name
ORDER BY [Number of Customers Acquired] DESC;
```

**Answer:** The query ranks campaigns by customers acquired.

### Q4. Which marketing channels acquired the most customers?

```sql
SELECT acquisition_channel, COUNT(*) AS [Number of Customers]
FROM dbo.customers
GROUP BY acquisition_channel
ORDER BY [Number of Customers] DESC;
```

**Answer:** Instagram was the leading acquisition channel with **10,057 customers**.

### Q5. Which acquisition channels perform best within each country?

```sql
SELECT country, acquisition_channel, COUNT(*) AS [Number of Customers]
FROM dbo.customers
GROUP BY country, acquisition_channel
ORDER BY country, [Number of Customers] DESC;
```

**Answer:** This identifies the strongest acquisition channel within each country.

---

## 💳 Subscription Analysis

### Q6. Which subscription plans are the most popular?

```sql
SELECT sp.plan_name, COUNT(*) AS [Subscribers]
FROM dbo.subscriptions AS s
LEFT JOIN dbo.subscription_plans AS sp
    ON s.plan_id = sp.plan_id
GROUP BY sp.plan_name
ORDER BY [Subscribers] DESC;
```

**Answer:** The Standard plan has the largest subscription volume.

### Q7. How many subscriptions are Active vs Cancelled?

```sql
SELECT subscription_status, COUNT(*) AS [Number of Subscriptions]
FROM dbo.subscriptions
GROUP BY subscription_status
ORDER BY [Number of Subscriptions] DESC;
```

**Answer:**

- Active: **39,086**
- Cancelled: **20,914**

### Q8. What is the subscription status by plan?

```sql
SELECT sp.plan_name, s.subscription_status,
       COUNT(*) AS [Number of Subscriptions]
FROM dbo.subscriptions AS s
LEFT JOIN dbo.subscription_plans AS sp
    ON s.plan_id = sp.plan_id
GROUP BY sp.plan_name, s.subscription_status
ORDER BY sp.plan_name, s.subscription_status;
```

**Answer:** This compares Active and Cancelled subscriptions across plans.

### Q9. What are the most common cancellation reasons?

```sql
SELECT cancellation_reason, COUNT(*) AS [Number of Cancellations]
FROM dbo.subscriptions
WHERE subscription_status = 'Cancelled'
GROUP BY cancellation_reason
ORDER BY [Number of Cancellations] DESC;
```

**Answer:** **Too Expensive** was the most common cancellation reason.

### Q10. Which subscription plan has the highest cancellation rate?

```sql
SELECT
    sp.plan_name,
    COUNT(*) AS [Total Subscriptions],
    SUM(CASE WHEN s.subscription_status = 'Cancelled' THEN 1 ELSE 0 END)
        AS [Cancelled Subscriptions],
    CAST(
        SUM(CASE WHEN s.subscription_status = 'Cancelled' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*) AS DECIMAL(5,2)
    ) AS [Cancellation Rate]
FROM dbo.subscriptions AS s
LEFT JOIN dbo.subscription_plans AS sp
    ON s.plan_id = sp.plan_id
GROUP BY sp.plan_name
ORDER BY [Cancellation Rate] DESC;
```

**Answer:** The Basic plan had the highest cancellation rate at approximately **35.24%**.

---

## 💰 Revenue Analysis

### Q11. What is the total successful revenue?

```sql
SELECT SUM(amount) AS [Total Revenue]
FROM dbo.transactions
WHERE transaction_status = 'Successful';
```

**Answer:** **$2,264,919.51**

### Q12. What is the average successful transaction value?

```sql
SELECT AVG(CAST(amount AS DECIMAL(18,2)))
       AS [Average Transaction Value]
FROM dbo.transactions
WHERE transaction_status = 'Successful';
```

**Answer:** **$12.05**

### Q13. Which subscription plans generate the most revenue?

```sql
SELECT
    sp.plan_name,
    SUM(t.amount) AS [Total Revenue]
FROM dbo.transactions AS t
LEFT JOIN dbo.subscriptions AS s
    ON t.subscription_id = s.subscription_id
LEFT JOIN dbo.subscription_plans AS sp
    ON s.plan_id = sp.plan_id
WHERE t.transaction_status = 'Successful'
GROUP BY sp.plan_name
ORDER BY [Total Revenue] DESC;
```

**Answer:** The Standard plan generated the highest revenue at approximately **$1.09M**.

### Q14. Which countries generate the highest revenue?

```sql
SELECT
    c.country,
    SUM(t.amount) AS [Total Revenue]
FROM dbo.transactions AS t
LEFT JOIN dbo.customers AS c
    ON t.customer_id = c.customer_id
WHERE t.transaction_status = 'Successful'
GROUP BY c.country
ORDER BY [Total Revenue] DESC;
```

**Answer:** The United States generated the highest revenue at approximately **$663K**.

### Q15. How does revenue change month over month?

```sql
SELECT
    YEAR(transaction_date) AS [Year],
    MONTH(transaction_date) AS [Month],
    SUM(amount) AS [Monthly Revenue]
FROM dbo.transactions
WHERE transaction_status = 'Successful'
GROUP BY YEAR(transaction_date), MONTH(transaction_date)
ORDER BY [Year], [Month];
```

**Answer:** This provides the monthly revenue trend.

---

## 🎬 Content & Engagement

### Q16. Which content receives the most user interactions?

```sql
SELECT
    ue.content_id,
    c.title,
    COUNT(*) AS [Number of Interactions]
FROM dbo.user_events AS ue
LEFT JOIN dbo.content AS c
    ON ue.content_id = c.content_id
GROUP BY ue.content_id, c.title
ORDER BY [Number of Interactions] DESC;
```

**Answer:** This ranks content according to total user interactions.

### Q17. Which customers are the most active?

```sql
SELECT customer_id, COUNT(*) AS [Number of Events]
FROM dbo.user_events
GROUP BY customer_id
ORDER BY [Number of Events] DESC;
```

**Answer:** This identifies customers generating the highest number of platform events.

### Q18. What types of user events occur most frequently?

```sql
SELECT event_type, COUNT(*) AS [Number of Events]
FROM dbo.user_events
GROUP BY event_type
ORDER BY [Number of Events] DESC;
```

**Answer:** **Play** was the most common event with **225,189 events**.

### Q19. Which content has the highest average watch duration?

```sql
SELECT
    ue.content_id,
    c.title,
    AVG(CAST(ue.watch_duration_minutes AS DECIMAL(18,2)))
        AS [Average Watch Duration]
FROM dbo.user_events AS ue
LEFT JOIN dbo.content AS c
    ON ue.content_id = c.content_id
WHERE ue.watch_duration_minutes IS NOT NULL
GROUP BY ue.content_id, c.title
ORDER BY [Average Watch Duration] DESC;
```

**Answer:** This identifies content with the highest average viewing duration.

### Q20. Which countries have the highest user engagement?

```sql
SELECT
    c.country,
    COUNT(*) AS [Number of User Events]
FROM dbo.user_events AS ue
LEFT JOIN dbo.customers AS c
    ON ue.customer_id = c.customer_id
GROUP BY c.country
ORDER BY [Number of User Events] DESC;
```

**Answer:** This compares engagement levels across countries.

---

## 📈 Advanced SQL

### Q21. How has customer acquisition changed month over month?

```sql
SELECT
    YEAR(signup_date) AS [Year],
    MONTH(signup_date) AS [Month],
    COUNT(*) AS [New Customers]
FROM dbo.customers
GROUP BY YEAR(signup_date), MONTH(signup_date)
ORDER BY [Year], [Month];
```

**Answer:** This provides the monthly customer acquisition trend.

### Q22. What percentage of subscriptions have been cancelled?

```sql
SELECT
    COUNT(*) AS [Total Subscriptions],
    SUM(CASE WHEN subscription_status = 'Cancelled' THEN 1 ELSE 0 END)
        AS [Cancelled Subscriptions],
    CAST(
        SUM(CASE WHEN subscription_status = 'Cancelled' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*) AS DECIMAL(5,2)
    ) AS [Overall Churn Rate]
FROM dbo.subscriptions;
```

**Answer:** **34.86% overall churn rate.**

### Q23. Which marketing campaigns have the highest conversion rate?

```sql
SELECT
    campaign_name,
    impressions,
    clicks,
    conversions,
    CAST(
        conversions * 100.0 / NULLIF(clicks, 0)
        AS DECIMAL(5,2)
    ) AS [Conversion Rate]
FROM dbo.marketing_campaigns
ORDER BY [Conversion Rate] DESC;
```

**Answer:** Email Re-engagement achieved the highest conversion rate at **20%**.

### Q24. What is Customer Lifetime Value?

```sql
SELECT
    c.customer_id,
    SUM(
        CASE
            WHEN t.transaction_status = 'Successful'
            THEN t.amount
            ELSE 0
        END
    ) AS [Customer Lifetime Value]
FROM dbo.customers AS c
LEFT JOIN dbo.transactions AS t
    ON c.customer_id = t.customer_id
GROUP BY c.customer_id
ORDER BY [Customer Lifetime Value] DESC;
```

**Answer:** This ranks customers using their total successful transaction revenue.

### Q25. Who are the highest-revenue customers?

```sql
WITH CustomerRevenue AS
(
    SELECT
        c.customer_id,
        SUM(
            CASE
                WHEN t.transaction_status = 'Successful'
                THEN t.amount
                ELSE 0
            END
        ) AS [Total Revenue]
    FROM dbo.customers AS c
    LEFT JOIN dbo.transactions AS t
        ON c.customer_id = t.customer_id
    GROUP BY c.customer_id
)
SELECT
    customer_id,
    [Total Revenue],
    RANK() OVER (
        ORDER BY [Total Revenue] DESC
    ) AS [Revenue Rank]
FROM CustomerRevenue
ORDER BY [Revenue Rank];
```

**Answer:** This uses a **CTE + RANK() window function** to rank customers by successful revenue.

---

# 🐍 Python Analysis

Python was used for:

- Synthetic data generation
- Data validation
- Exploratory Data Analysis
- Statistical analysis
- Visualization
- Business insight generation

## Python Files

### `python/01_generate_data.py`

Generates the synthetic datasets:

- Customers
- Subscriptions
- Transactions
- Content
- User Events
- Marketing Campaigns
- Geography
- Subscription Plans

### `python/02_data_quality_check.py`

Performs:

- Missing-value checks
- Duplicate checks
- Invalid-value checks
- Date validation
- Referential consistency
- Business-rule validation

---

# 💻 Python Code Examples

### Customer Data Generation

```python
customers = pd.DataFrame({
    "customer_id": customer_ids,
    "signup_date": signup_dates,
    "age": ages,
    "gender": genders,
    "country": customer_countries,
    "city": customer_cities,
    "campaign_id": customer_campaign_ids
})

customers["acquisition_channel"] = customers[
    "campaign_id"
].map(campaign_channel_map)
```

### Transaction Data Generation

```python
transactions = pd.DataFrame({
    "transaction_id": transaction_ids,
    "subscription_id": transaction_subscription_ids,
    "customer_id": transaction_customer_ids,
    "transaction_date": transaction_dates,
    "amount": transaction_amounts,
    "transaction_status": transaction_status,
    "payment_method": payment_methods
})
```

### User Event Generation

```python
user_events = pd.DataFrame({
    "event_id": event_ids,
    "customer_id": event_customer_ids,
    "content_id": event_content_ids,
    "event_timestamp": event_timestamps,
    "event_type": event_type_values,
    "watch_duration_minutes": watch_durations,
    "device_type": event_device_types
})
```

### Python Validation Examples

```python
# Duplicate IDs
customers["customer_id"].duplicated().sum()

# Missing values
customers.isnull().sum()

# Invalid transaction amounts
transactions[transactions["amount"] <= 0]

# Invalid watch durations
user_events[
    user_events["watch_duration_minutes"] < 0
]
```

---

# 📈 Python EDA Highlights

The Python analysis found:

- Customer base: **50,000**
- Average customer age: **41.64**
- Median customer age: **42**
- Active subscriptions: **39,086**
- Cancelled subscriptions: **20,914**
- Successful transactions: **187,949**
- Successful revenue: **$2,264,919.51**
- Average successful transaction: **$12.05**
- Total user events: **500,000**
- Most common event: **Play**
- Most common acquisition channel: **Instagram**

---

# 🔎 Data Quality & Validation

Validation was performed using both SQL and Python.

### Checks

- NULL values
- Duplicate primary keys
- Foreign-key integrity
- Negative financial values
- Invalid dates
- Business-rule validation
- Transaction validation

### Results

✅ No key-column NULL values  
✅ No duplicate primary keys  
✅ No broken foreign-key relationships  
✅ No negative financial values  
✅ No invalid subscription date ranges  

### ⚠️ Known Anomaly

Five successful transactions occurred shortly before the associated subscription start dates.

These records were **retained and documented rather than deleted** so that the original data remained intact.

---

# 📊 Executive KPIs

| KPI | Result |
|---|---:|
| Total Customers | **50,000** |
| Total Subscriptions | **60,000** |
| Active Subscriptions | **39,086** |
| Cancelled Subscriptions | **20,914** |
| Churn Rate | **34.86%** |
| Successful Revenue | **$2,264,919.51** |
| Average Transaction Value | **$12.05** |
| Total Transactions | **200,000** |
| Successful Transactions | **187,949** |
| Total User Events | **500,000** |

---

# 💡 Key Business Insights

### 💰 Revenue
StreamSphere generated approximately **$2.26M** in successful transaction revenue.

### 📉 Churn
Overall churn was **34.86%**. Basic had the highest cancellation rate and Premium the lowest.

### ❌ Cancellation
**Too Expensive** was the most common cancellation reason.

### 📣 Acquisition
**Instagram** was the leading acquisition channel with **10,057 customers**.

### 📧 Marketing
**Email Re-engagement** achieved the highest campaign conversion rate at **20%**.

### 🌎 Geography
The **United States** generated the highest revenue at approximately **$663K**.

### 💳 Plan Revenue
The **Standard plan** generated the highest revenue at approximately **$1.09M**.

### 🎬 Engagement
**Play** was the most common user event with **225,189 events**.

---

# 💡 Business Recommendations

## 1. Reduce Customer Churn
Develop targeted retention strategies for customers showing cancellation signals.

## 2. Review Basic Plan Value
Review pricing, features and perceived value because the Basic plan has the highest cancellation rate.

## 3. Address Pricing Concerns
Since "Too Expensive" is the most common cancellation reason, consider targeted discounts, bundles and retention offers.

## 4. Strengthen High-Performing Acquisition
Continue evaluating high-performing channels using both acquisition volume and customer value.

## 5. Expand Email Re-engagement
Test and expand Email Re-engagement for retention and win-back campaigns.

## 6. Focus on High-Value Markets
Develop targeted retention and monetization strategies for high-revenue markets.

## 7. Use Engagement Data
Use user-event and content data to improve personalization, recommendations and retention.

---

# 📁 Project Structure

```text
StreamSphere-Analytics/
│
├── dashboard/
│   ├── Customer & Acquisition.png
│   ├── Executive Overview.png
│   ├── Revenue & Engagement.png
│   ├── StreamSphere Analytics.png
│   └── Subscription & Churn.png
│
├── data/
│   └── raw/
│       ├── content.csv
│       ├── customers.csv
│       ├── geography.csv
│       ├── marketing_campaigns.csv
│       ├── subscription_plans.csv
│       ├── subscriptions.csv
│       ├── transactions.csv
│       └── user_events.csv
│
├── notebooks/
│   ├── 01_python_eda.ipynb
│   └── Business insights.ipynb
│
├── python/
│   ├── 01_generate_data.py
│   └── 02_data_quality_check.py
│
├── sql/
│   ├── 01_create_tables.sql
│   ├── 02_eda.sql
│   └── 03_data_validation.sql
│
├── .gitattributes
├── README.md
├── Readme.txt
└── requirement.txt
```

---

# 📚 Project Files

| File | Purpose |
|---|---|
| `python/01_generate_data.py` | Generate synthetic datasets |
| `python/02_data_quality_check.py` | Python data-quality checks |
| `sql/01_create_tables.sql` | Create SQL Server tables and relationships |
| `sql/02_eda.sql` | SQL business analysis |
| `sql/03_data_validation.sql` | SQL validation |
| `notebooks/01_python_eda.ipynb` | Python exploratory analysis |
| `notebooks/Business insights.ipynb` | Business insights |
| `dashboard/` | Power BI dashboard screenshots |
| `data/raw/` | Raw CSV datasets |

---

# 🧠 Skills Demonstrated

### SQL
`SQL Server` `SQL` `Joins` `CTEs` `Subqueries` `Window Functions` `CASE` `Aggregations` `Views` `Data Validation` `Database Design`

### Python
`Python` `Pandas` `NumPy` `Matplotlib` `Seaborn` `PyODBC` `EDA` `Data Validation`

### Power BI
`Power BI` `DAX` `Data Modeling` `KPIs` `Interactive Dashboards` `Slicers` `Filters` `Data Visualization`

### Business Analytics
`Customer Analytics` `Customer Acquisition` `Churn Analysis` `Revenue Analytics` `Marketing Analytics` `Customer Lifetime Value` `User Engagement`

---

# 🚀 Project Outcome

StreamSphere Analytics demonstrates the ability to take a business problem from raw data to actionable insights through a complete analytics lifecycle:

```text
DATA
 ↓
SQL SERVER
 ↓
DATA VALIDATION
 ↓
SQL EDA
 ↓
PYTHON EDA
 ↓
POWER BI
 ↓
DAX
 ↓
BUSINESS INSIGHTS
 ↓
RECOMMENDATIONS
```

---

# 👨‍💻 Author

## Karan Kapadia

`SQL` • `Python` • `Power BI` • `DAX` • `Data Analytics`

---

⭐ If you found this project useful, feel free to explore the SQL scripts, Python notebooks, datasets and Power BI dashboard.
