/* ============================================================
   EDA QUESTION 1
   Customer Distribution by Country

   Business Question:
   Which countries have the highest number of StreamSphere
   customers?
   ============================================================ */

SELECT
    country,
    COUNT(*) AS [Number of Customers]
FROM dbo.customers
GROUP BY country
ORDER BY [Number of Customers]


/* ============================================================
   EDA QUESTION 2
   Customer Distribution by Region

   Business Question:
   Which regions have the highest number of StreamSphere
   customers?
   ============================================================ */

SELECT
    g.region,
    COUNT(*) AS [Region Members]
FROM dbo.customers AS c
LEFT JOIN dbo.geography AS g
    ON c.country = g.country
GROUP BY g.region
ORDER BY [Region Members] DESC



/* ============================================================
   EDA QUESTION 3
   Customer Acquisition by Marketing Campaign

   Business Question:
   Which marketing campaigns acquired the highest number of
   customers?
   ============================================================ */

SELECT
    mc.campaign_name,
    COUNT(*) AS [Number of Customers Acquired]
FROM dbo.customers AS c
LEFT JOIN dbo.marketing_campaigns AS mc
    ON c.campaign_id = mc.campaign_id
GROUP BY mc.campaign_name
ORDER BY [Number of Customers Acquired] DESC;



/* ============================================================
   EDA QUESTION 4
   Customer Acquisition by Marketing Channel

   Business Question:
   Which marketing channels acquired the highest number of
   customers?
   ============================================================ */

SELECT
    acquisition_channel,
    COUNT(*) AS [Number of Customers]
FROM dbo.customers
GROUP BY acquisition_channel
ORDER BY [Number of Customers] DESC;



/* ============================================================
   EDA QUESTION 5
   Customer Acquisition by Country and Marketing Channel

   Business Question:
   Which marketing channels are most effective within each
   customer country?
   ============================================================ */

SELECT
    country,
    acquisition_channel,
    COUNT(*) AS [Number of Customers]
FROM dbo.customers
GROUP BY country, acquisition_channel
ORDER BY country, [Number of Customers] DESC;
GO


/* ============================================================
   SUBSCRIPTION ANALYSIS
   ============================================================ */


/* ============================================================
   EDA QUESTION 6
   Most Popular Subscription Plans

   Business Question:
   Which subscription plans are the most popular?
   ============================================================ */

SELECT
    sp.plan_name,
    COUNT(*) AS [Subscribers]
FROM dbo.subscriptions AS s
LEFT JOIN dbo.subscription_plans AS sp
    ON s.plan_id = sp.plan_id
GROUP BY sp.plan_name
ORDER BY [Subscribers] DESC;



/* ============================================================
   EDA QUESTION 7
   Active vs Cancelled Subscriptions

   Business Question:
   How many subscriptions are Active vs Cancelled?
   ============================================================ */

SELECT
    subscription_status,
    COUNT(*) AS [Number of Subscriptions]
FROM dbo.subscriptions
GROUP BY subscription_status
ORDER BY [Number of Subscriptions] DESC;



/* ============================================================
   EDA QUESTION 8
   Subscription Status by Plan

   Business Question:
   How many Active and Cancelled subscriptions does each
   subscription plan have?
   ============================================================ */

SELECT
    sp.plan_name,
    s.subscription_status,
    COUNT(*) AS [Number of Subscriptions]
FROM dbo.subscriptions AS s
LEFT JOIN dbo.subscription_plans AS sp
    ON s.plan_id = sp.plan_id
GROUP BY
    sp.plan_name,
    s.subscription_status
ORDER BY
    sp.plan_name,
    s.subscription_status;



/* ============================================================
   EDA QUESTION 9
   Cancellation Reasons

   Business Question:
   What are the most common reasons customers cancel their
   subscriptions?
   ============================================================ */

SELECT
    cancellation_reason,
    COUNT(*) AS [Number of Cancellations]
FROM dbo.subscriptions
WHERE subscription_status = 'Cancelled'
GROUP BY cancellation_reason
ORDER BY [Number of Cancellations] DESC;


/* ============================================================
   EDA QUESTION 10
   Cancellation Rate by Plan

   Business Question:
   Which subscription plan has the highest cancellation rate?
   ============================================================ */

SELECT
    sp.plan_name,
    COUNT(*) AS [Total Subscriptions],
    SUM(
        CASE
            WHEN s.subscription_status = 'Cancelled' THEN 1
            ELSE 0
        END
    ) AS [Cancelled Subscriptions],
    CAST(
        SUM(
            CASE
                WHEN s.subscription_status = 'Cancelled' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*)
        AS DECIMAL(5,2)
    ) AS [Cancellation Rate]
FROM dbo.subscriptions AS s
LEFT JOIN dbo.subscription_plans AS sp
    ON s.plan_id = sp.plan_id
GROUP BY sp.plan_name
ORDER BY [Cancellation Rate] DESC;


/* ============================================================
   REVENUE & TRANSACTION ANALYSIS
   ============================================================ */


/* ============================================================
   EDA QUESTION 11
   Total Revenue

   Business Question:
   What is the total revenue generated by StreamSphere?


   ============================================================ */

SELECT
    SUM(amount) AS [Total Revenue]
FROM dbo.transactions;


/* ============================================================
   EDA QUESTION 12
   Average Transaction Value

   Business Question:
   What is the average value of a StreamSphere transaction?

   NOTE:
   Assumes dbo.transactions contains a numeric column named
   transaction_amount.
   ============================================================ */

SELECT
    AVG(cast(amount AS DECIMAL(18,2))) AS [Average Transaction Value]
FROM dbo.transactions;




/* ============================================================
   EDA QUESTION 13
   Revenue by Subscription Plan

   Business Question:
   Which subscription plans generate the most revenue?

 
   ============================================================ */

SELECT
    sp.plan_name,
    SUM(t.amount) AS [Total Revenue]
FROM dbo.transactions AS t
LEFT JOIN dbo.subscriptions AS s
    ON t.subscription_id = s.subscription_id
LEFT JOIN dbo.subscription_plans AS sp
    ON s.plan_id = sp.plan_id
GROUP BY sp.plan_name
ORDER BY [Total Revenue] DESC;



/* ============================================================
   EDA QUESTION 14
   Revenue by Country

   Business Question:
   Which countries generate the highest revenue?

   ============================================================ */

SELECT
    c.country,
    SUM(t.amount) AS [Total Revenue]
FROM dbo.transactions AS t
LEFT JOIN dbo.customers AS c
    ON t.customer_id = c.customer_id
GROUP BY c.country
ORDER BY [Total Revenue] DESC;



/* ============================================================
   EDA QUESTION 15
   Monthly Revenue Trend

   Business Question:
   How does StreamSphere's revenue change month over month?

   NOTE:
   Assumes dbo.transactions contains:
   - transaction_date
   - transaction_amount
   ============================================================ */

SELECT
    YEAR(transaction_date) AS [Year],
    MONTH(transaction_date) AS [Month],
    SUM(amount) AS [Monthly Revenue]
FROM dbo.transactions
GROUP BY
    YEAR(transaction_date),
    MONTH(transaction_date)
ORDER BY
    [Year],
    [Month];


/* ============================================================
   CONTENT & USER ENGAGEMENT
   ============================================================ */


/* ============================================================
   EDA QUESTION 16
   Most Popular Content

   Business Question:
   Which content receives the most user interactions?
   ============================================================ */

SELECT
    ue.content_id,
    c.title,
    COUNT(*) AS [Number of Interactions]
FROM dbo.user_events AS ue
LEFT JOIN dbo.content AS c
    ON ue.content_id = c.content_id
GROUP BY
    ue.content_id,
    c.title
ORDER BY [Number of Interactions] DESC;



/* ============================================================
   EDA QUESTION 17
   Most Active Customers

   Business Question:
   Which customers are the most active on the StreamSphere
   platform?
   ============================================================ */

SELECT
    customer_id,
    COUNT(*) AS [Number of Events]
FROM dbo.user_events
GROUP BY customer_id
ORDER BY [Number of Events] DESC;


/* ============================================================
   EDA QUESTION 18
   Most Common Event Types

   Business Question:
   What types of user events occur most frequently?
   ============================================================ */

SELECT
    event_type,
    COUNT(*) AS [Number of Events]
FROM dbo.user_events
GROUP BY event_type
ORDER BY [Number of Events] DESC;



/* ============================================================
   EDA QUESTION 19
   Content with Highest Average Watch Duration

   Business Question:
   Which content has the highest average watch duration?

 
   ============================================================ */

SELECT
    ue.content_id,
    c.title,
    AVG(CAST(ue.watch_duration_minutes AS DECIMAL(18,2))) AS [Average Watch Duration]
FROM dbo.user_events AS ue
LEFT JOIN dbo.content AS c
    ON ue.content_id = c.content_id
WHERE ue.watch_duration_minutes IS NOT NULL
GROUP BY
    ue.content_id,
    c.title
ORDER BY [Average Watch Duration] DESC;



/* ============================================================
   EDA QUESTION 20
   User Engagement by Country

   Business Question:
   Which countries have the highest level of user engagement?
   ============================================================ */

SELECT
    c.country,
    COUNT(*) AS [Number of User Events]
FROM dbo.user_events AS ue
LEFT JOIN dbo.customers AS c
    ON ue.customer_id = c.customer_id
GROUP BY c.country
ORDER BY [Number of User Events] DESC;


/* ============================================================
   ADVANCED SQL ANALYSIS
   ============================================================ */


/* ============================================================
   EDA QUESTION 21
   Monthly Customer Acquisition Trend

   Business Question:
   How has customer acquisition changed month over month?
   ============================================================ */

SELECT
    YEAR(signup_date) AS [Year],
    MONTH(signup_date) AS [Month],
    COUNT(*) AS [New Customers]
FROM dbo.customers
GROUP BY
    YEAR(signup_date),
    MONTH(signup_date)
ORDER BY
    [Year],
    [Month];



/* ============================================================
   EDA QUESTION 22
   Overall Churn Rate

   Business Question:
   What percentage of StreamSphere subscriptions have been
   cancelled?
   ============================================================ */

SELECT
    COUNT(*) AS [Total Subscriptions],
    SUM(
        CASE
            WHEN subscription_status = 'Cancelled' THEN 1
            ELSE 0
        END
    ) AS [Cancelled Subscriptions],
    CAST(
        SUM(
            CASE
                WHEN subscription_status = 'Cancelled' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*)
        AS DECIMAL(5,2)
    ) AS [Overall Churn Rate]
FROM dbo.subscriptions;


/* ============================================================
   EDA QUESTION 23
   Marketing Campaign Conversion Rate

   Business Question:
   Which marketing campaigns have the highest customer
   conversion rate?

   NOTE:
   This requires a campaign-level denominator such as campaign
   reach/impressions. If marketing_campaigns has a numeric
   reach/impressions column, replace [campaign_reach] below
   with the exact column name.

   If the dataset does not contain campaign reach/impressions,
   use Question 3 as the acquisition analysis rather than
   inventing a conversion rate.
   ============================================================ */


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



/* ============================================================
   EDA QUESTION 24
   Customer Lifetime Value (CLV)

   Business Question:
   What is the estimated lifetime value of StreamSphere
   customers?

   ============================================================ */

SELECT
    c.customer_id,
    SUM(t.amount) AS [Customer Lifetime Value]
FROM dbo.customers AS c
LEFT JOIN dbo.transactions AS t
    ON c.customer_id = t.customer_id
GROUP BY c.customer_id
ORDER BY [Customer Lifetime Value] DESC;



/* ============================================================
   EDA QUESTION 25
   Customer Revenue Ranking

   Business Question:
   Who are the highest-revenue customers, and how do they rank
   against one another?
   ============================================================ */

WITH CustomerRevenue AS
(
    SELECT
        c.customer_id,
        SUM(t.amount) AS [Total Revenue]
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