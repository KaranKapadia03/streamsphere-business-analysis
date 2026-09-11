--CREATE TABLE dbo.geography (
--    country VARCHAR(100) NOT NULL PRIMARY KEY,
--    region VARCHAR(100),
--    continent VARCHAR(100)
--);

--CREATE TABLE dbo.subscription_plans (
--    plan_id INT NOT NULL PRIMARY KEY,
--    plan_name VARCHAR(50) NOT NULL,
--    monthly_price DECIMAL(10,2) NOT NULL
--);


--CREATE TABLE dbo.marketing_campaigns (
--    campaign_id INT NOT NULL PRIMARY KEY,
--    campaign_name VARCHAR(100) NOT NULL,
--    channel VARCHAR(50) NOT NULL,
--    start_date DATE,
--    end_date DATE,
--    budget DECIMAL(12,2)
--);

--CREATE TABLE dbo.customers (
--    customer_id VARCHAR(20) NOT NULL PRIMARY KEY,
--    signup_date DATE NOT NULL,
--    age INT NOT NULL,
--    gender VARCHAR(20) NOT NULL,
--    country VARCHAR(100) NOT NULL,
--    city VARCHAR(100) NOT NULL,
--    campaign_id INT NOT NULL,
--    acquisition_channel VARCHAR(50) NOT NULL,

--    CONSTRAINT FK_customers_geography
--        FOREIGN KEY (country)
--        REFERENCES dbo.geography(country),

--    CONSTRAINT FK_customers_campaign
--        FOREIGN KEY (campaign_id)
--        REFERENCES dbo.marketing_campaigns(campaign_id)
--);


--CREATE TABLE dbo.subscriptions (
--    subscription_id VARCHAR(20) NOT NULL PRIMARY KEY,
--    customer_id VARCHAR(20) NOT NULL,
--    plan_id INT NOT NULL,
--    start_date DATE NOT NULL,
--    end_date DATE NULL,
--    subscription_status VARCHAR(20) NOT NULL,
--    cancellation_reason VARCHAR(100) NULL,

--    CONSTRAINT FK_subscriptions_customer
--        FOREIGN KEY (customer_id)
--        REFERENCES dbo.customers(customer_id),

--    CONSTRAINT FK_subscriptions_plan
--        FOREIGN KEY (plan_id)
--        REFERENCES dbo.subscription_plans(plan_id)
--);


--CREATE TABLE dbo.content (
--    content_id VARCHAR(20) NOT NULL PRIMARY KEY,
--    title VARCHAR(200) NOT NULL,
--    genre VARCHAR(50) NOT NULL,
--    content_type VARCHAR(20) NOT NULL,
--    release_year INT NOT NULL,
--    duration_minutes INT NOT NULL
--);

--CREATE TABLE dbo.transactions (
--    transaction_id VARCHAR(20) NOT NULL PRIMARY KEY,
--    subscription_id VARCHAR(20) NOT NULL,
--    customer_id VARCHAR(20) NOT NULL,
--    transaction_date DATE NOT NULL,
--    amount DECIMAL(10,2) NOT NULL,
--    transaction_status VARCHAR(20) NOT NULL,
--    payment_method VARCHAR(50) NOT NULL,

--    CONSTRAINT FK_transactions_subscription
--        FOREIGN KEY (subscription_id)
--        REFERENCES dbo.subscriptions(subscription_id),

--    CONSTRAINT FK_transactions_customer
--        FOREIGN KEY (customer_id)
--        REFERENCES dbo.customers(customer_id)
--);


--CREATE TABLE dbo.user_events (
--    event_id VARCHAR(20) NOT NULL PRIMARY KEY,
--    customer_id VARCHAR(20) NOT NULL,
--    content_id VARCHAR(20) NOT NULL,
--    event_timestamp DATETIME2 NOT NULL,
--    event_type VARCHAR(20) NOT NULL,
--    watch_duration_minutes INT NOT NULL,
--    device_type VARCHAR(50) NOT NULL,

--    CONSTRAINT FK_events_customer
--        FOREIGN KEY (customer_id)
--        REFERENCES dbo.customers(customer_id),

--    CONSTRAINT FK_events_content
--        FOREIGN KEY (content_id)
--        REFERENCES dbo.content(content_id)
--);

--DROP TABLE IF EXISTS dbo.user_events;
--DROP TABLE IF EXISTS dbo.transactions;
--DROP TABLE IF EXISTS dbo.subscriptions;
--DROP TABLE IF EXISTS dbo.customers;
--DROP TABLE IF EXISTS dbo.content;
--DROP TABLE IF EXISTS dbo.marketing_campaigns;
--DROP TABLE IF EXISTS dbo.subscription_plans;
--DROP TABLE IF EXISTS dbo.geography;


