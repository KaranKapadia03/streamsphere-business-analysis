/* ============================================================
   StreamSphere Analytics
   03_data_validation.sql

   Purpose:
   Validate data integrity after importing the datasets
   ============================================================ */

USE StreamSphereAnalytics;
GO


/* ============================================================
   1. ROW COUNT VALIDATION
   Check that all tables contain the expected number of rows
   ============================================================ */

SELECT 'geography' AS table_name, COUNT(*) AS row_count
FROM dbo.geography

UNION ALL

SELECT 'subscription_plans', COUNT(*)
FROM dbo.subscription_plans

UNION ALL

SELECT 'marketing_campaigns', COUNT(*)
FROM dbo.marketing_campaigns

UNION ALL

SELECT 'customers', COUNT(*)
FROM dbo.customers

UNION ALL

SELECT 'subscriptions', COUNT(*)
FROM dbo.subscriptions

UNION ALL

SELECT 'content', COUNT(*)
FROM dbo.content

UNION ALL

SELECT 'transactions', COUNT(*)
FROM dbo.transactions

UNION ALL

SELECT 'user_events', COUNT(*)
FROM dbo.user_events;
GO


/* ============================================================
   2. NULL VALUE CHECK
   Check important key columns for NULL values
   ============================================================ */

SELECT
    'customers.customer_id' AS column_name,
    COUNT(*) AS null_count
FROM dbo.customers
WHERE customer_id IS NULL

UNION ALL

SELECT
    'subscriptions.subscription_id',
    COUNT(*)
FROM dbo.subscriptions
WHERE subscription_id IS NULL

UNION ALL

SELECT
    'transactions.transaction_id',
    COUNT(*)
FROM dbo.transactions
WHERE transaction_id IS NULL

UNION ALL

SELECT
    'user_events.event_id',
    COUNT(*)
FROM dbo.user_events
WHERE event_id IS NULL;
GO


/* ============================================================
   3. DUPLICATE PRIMARY KEY CHECK
   Check for duplicate IDs
   ============================================================ */

SELECT
    customer_id,
    COUNT(*) AS duplicate_count
FROM dbo.customers
GROUP BY customer_id
HAVING COUNT(*) > 1;
GO

SELECT
    subscription_id,
    COUNT(*) AS duplicate_count
FROM dbo.subscriptions
GROUP BY subscription_id
HAVING COUNT(*) > 1;
GO

SELECT
    transaction_id,
    COUNT(*) AS duplicate_count
FROM dbo.transactions
GROUP BY transaction_id
HAVING COUNT(*) > 1;
GO

SELECT
    event_id,
    COUNT(*) AS duplicate_count
FROM dbo.user_events
GROUP BY event_id
HAVING COUNT(*) > 1;
GO


/* ============================================================
   4. FOREIGN KEY VALIDATION
   Find records that do not have matching parent records
   ============================================================ */

-- Customers → Geography
SELECT c.customer_id, c.country
FROM dbo.customers AS c
LEFT JOIN dbo.geography AS g
    ON c.country = g.country
WHERE g.country IS NULL;
GO

-- Customers → Marketing Campaigns
SELECT c.customer_id, c.campaign_id
FROM dbo.customers AS c
LEFT JOIN dbo.marketing_campaigns AS mc
    ON c.campaign_id = mc.campaign_id
WHERE mc.campaign_id IS NULL;
GO

-- Subscriptions → Customers
SELECT s.subscription_id, s.customer_id
FROM dbo.subscriptions AS s
LEFT JOIN dbo.customers AS c
    ON s.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
GO

-- Subscriptions → Subscription Plans
SELECT s.subscription_id, s.plan_id
FROM dbo.subscriptions AS s
LEFT JOIN dbo.subscription_plans AS sp
    ON s.plan_id = sp.plan_id
WHERE sp.plan_id IS NULL;
GO

-- Transactions → Subscriptions
SELECT t.transaction_id, t.subscription_id
FROM dbo.transactions AS t
LEFT JOIN dbo.subscriptions AS s
    ON t.subscription_id = s.subscription_id
WHERE s.subscription_id IS NULL;
GO

-- Transactions → Customers
SELECT t.transaction_id, t.customer_id
FROM dbo.transactions AS t
LEFT JOIN dbo.customers AS c
    ON t.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
GO

-- User Events → Customers
SELECT ue.event_id, ue.customer_id
FROM dbo.user_events AS ue
LEFT JOIN dbo.customers AS c
    ON ue.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
GO

-- User Events → Content
SELECT ue.event_id, ue.content_id
FROM dbo.user_events AS ue
LEFT JOIN dbo.content AS ct
    ON ue.content_id = ct.content_id
WHERE ct.content_id IS NULL;
GO


/* ============================================================
   5. BUSINESS VALUE VALIDATION
   Check for invalid numeric values
   ============================================================ */

-- Customer age
SELECT *
FROM dbo.customers
WHERE age < 0 OR age > 120;
GO

-- Subscription plan price
SELECT *
FROM dbo.subscription_plans
WHERE monthly_price < 0;
GO

-- Transaction amount
SELECT *
FROM dbo.transactions
WHERE amount < 0;
GO

-- Content duration
SELECT *
FROM dbo.content
WHERE duration_minutes < 0;
GO

-- Watch duration
SELECT *
FROM dbo.user_events
WHERE watch_duration_minutes < 0;
GO


/* ============================================================
   6. DATE VALIDATION
   Check for logically invalid dates
   ============================================================ */

-- Subscription end date before start date
SELECT *
FROM dbo.subscriptions
WHERE end_date IS NOT NULL
  AND end_date < start_date;
GO

-- Transaction date before subscription start
SELECT
    t.transaction_id,
    t.transaction_date,
    s.start_date
FROM dbo.transactions AS t
JOIN dbo.subscriptions AS s
    ON t.subscription_id = s.subscription_id
WHERE t.transaction_date < s.start_date;
GO

/* ============================================================
   7. DATA-QUALITY FINDING
   ============================================================

   The validation identified 5 successful transactions that
   occurred 1–2 days before their corresponding subscription
   start dates.

   These records are retained because they represent successful
   transactions. The issue is documented as a data-quality
   anomaly rather than deleting the records.

   ============================================================ */


/* ============================================================
   VALIDATION SUMMARY
   ============================================================

   Checks performed:
   ✓ Row counts
   ✓ NULL values
   ✓ Duplicate primary keys
   ✓ Foreign-key integrity
   ✓ Negative/invalid numeric values
   ✓ Subscription date consistency
   ✓ Transaction date consistency

   Finding:
   ⚠ 5 transactions occurred before subscription start dates.

   Action:
   → Records retained and documented.
   ============================================================ */