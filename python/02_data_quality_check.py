import pandas as pd
from pathlib import Path

# Find the main project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Point to the raw data folder
RAW_DATA_DIR = BASE_DIR / "data" / "raw"

# Load all datasets
customers = pd.read_csv(RAW_DATA_DIR / "customers.csv")
subscriptions = pd.read_csv(RAW_DATA_DIR / "subscriptions.csv")
transactions = pd.read_csv(RAW_DATA_DIR / "transactions.csv")
content = pd.read_csv(RAW_DATA_DIR / "content.csv")
user_events = pd.read_csv(RAW_DATA_DIR / "user_events.csv")
geography = pd.read_csv(RAW_DATA_DIR / "geography.csv")
marketing_campaigns = pd.read_csv(
    RAW_DATA_DIR / "marketing_campaigns.csv"
)
subscription_plans = pd.read_csv(
    RAW_DATA_DIR / "subscription_plans.csv"
)

print("All datasets loaded successfully!")

# Check dataset sizes
print("\n--- Dataset Sizes ---")

datasets = {
    "Customers": customers,
    "Subscriptions": subscriptions,
    "Transactions": transactions,
    "Content": content,
    "User Events": user_events,
    "Geography": geography,
    "Marketing Campaigns": marketing_campaigns,
    "Subscription Plans": subscription_plans
}

for name, df in datasets.items():
    print(f"{name}: {df.shape[0]:,} rows, {df.shape[1]} columns")


# Check missing values in all datasets
print("\n--- Missing Value Check ---")

for name, df in datasets.items():
    missing_values = df.isnull().sum().sum()
    print(f"{name}: {missing_values:,} missing values")


# Check duplicate primary keys
print("\n--- Duplicate Primary Key Check ---")

primary_keys = {
    "Customers": (customers, "customer_id"),
    "Subscriptions": (subscriptions, "subscription_id"),
    "Transactions": (transactions, "transaction_id"),
    "Content": (content, "content_id"),
    "User Events": (user_events, "event_id"),
    "Geography": (geography, "country"),
    "Marketing Campaigns": (
        marketing_campaigns,
        "campaign_id"
    ),
    "Subscription Plans": (
        subscription_plans,
        "plan_id"
    )
}

for table_name, (df, key) in primary_keys.items():
    duplicates = df[key].duplicated().sum()
    print(f"{table_name}: {duplicates:,} duplicate {key} values")
# Validate foreign key relationships
print("\n--- Foreign Key Relationship Check ---")

foreign_key_checks = {
    "Customers → Marketing Campaigns": (
        customers["campaign_id"],
        marketing_campaigns["campaign_id"]
    ),

    "Subscriptions → Customers": (
        subscriptions["customer_id"],
        customers["customer_id"]
    ),

    "Subscriptions → Plans": (
        subscriptions["plan_id"],
        subscription_plans["plan_id"]
    ),

    "Transactions → Customers": (
        transactions["customer_id"],
        customers["customer_id"]
    ),

    "Transactions → Subscriptions": (
        transactions["subscription_id"],
        subscriptions["subscription_id"]
    ),

    "User Events → Customers": (
        user_events["customer_id"],
        customers["customer_id"]
    ),

    "User Events → Content": (
        user_events["content_id"],
        content["content_id"]
    )
}

for relationship, (child_key, parent_key) in foreign_key_checks.items():

    invalid_keys = (~child_key.isin(parent_key)).sum()

    print(f"{relationship}: {invalid_keys:,} invalid records")
# Convert date columns to datetime format
customers["signup_date"] = pd.to_datetime(customers["signup_date"])

subscriptions["start_date"] = pd.to_datetime(
    subscriptions["start_date"]
)

subscriptions["end_date"] = pd.to_datetime(
    subscriptions["end_date"]
)

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

user_events["event_timestamp"] = pd.to_datetime(
    user_events["event_timestamp"]
)

# Validate business rules
print("\n--- Business Rule Validation ---")

# 1. Subscription end date should not be before start date
invalid_subscription_dates = subscriptions[
    subscriptions["end_date"].notna()
    & (subscriptions["end_date"] < subscriptions["start_date"])
]

print(
    "Subscriptions with end date before start date:",
    len(invalid_subscription_dates)
)

# 2. Transaction date should not be before subscription start date
subscription_start_map = subscriptions.set_index(
    "subscription_id"
)["start_date"]

transaction_subscription_start = transactions[
    "subscription_id"
].map(subscription_start_map)

invalid_transaction_dates = (
    transactions["transaction_date"]
    < transaction_subscription_start
).sum()

print(
    "Transactions before subscription start:",
    invalid_transaction_dates
)

# 3. Customer age should be realistic
invalid_ages = customers[
    (customers["age"] < 18)
    | (customers["age"] > 100)
]

print(
    "Customers with invalid age:",
    len(invalid_ages)
)

# 4. Watch duration should not be negative
negative_watch_duration = (
    user_events["watch_duration_minutes"] < 0
).sum()

print(
    "Events with negative watch duration:",
    negative_watch_duration
)
# Advanced subscription and transaction validation
print("\n--- Advanced Subscription Validation ---")

# Get subscription end dates for each transaction
subscription_end_map = subscriptions.set_index(
    "subscription_id"
)["end_date"]

transaction_subscription_end = transactions[
    "subscription_id"
].map(subscription_end_map)

# Check transactions after subscription cancellation
transactions_after_cancellation = (
    transaction_subscription_end.notna()
    & (
        transactions["transaction_date"]
        > transaction_subscription_end
    )
).sum()

print(
    "Transactions after subscription cancellation:",
    transactions_after_cancellation
)

# Validate subscription status consistency
print("\n--- Subscription Status Consistency Check ---")

# Active subscriptions should not have an end date
active_with_end_date = subscriptions[
    (subscriptions["subscription_status"] == "Active")
    & subscriptions["end_date"].notna()
]

print(
    "Active subscriptions with an end date:",
    len(active_with_end_date)
)

# Active subscriptions should not have a cancellation reason
active_with_reason = subscriptions[
    (subscriptions["subscription_status"] == "Active")
    & subscriptions["cancellation_reason"].notna()
]

print(
    "Active subscriptions with cancellation reason:",
    len(active_with_reason)
)

# Cancelled subscriptions should have an end date
cancelled_without_end_date = subscriptions[
    (subscriptions["subscription_status"] == "Cancelled")
    & subscriptions["end_date"].isna()
]

print(
    "Cancelled subscriptions without end date:",
    len(cancelled_without_end_date)
)

# Cancelled subscriptions should have a cancellation reason
cancelled_without_reason = subscriptions[
    (subscriptions["subscription_status"] == "Cancelled")
    & subscriptions["cancellation_reason"].isna()
]

print(
    "Cancelled subscriptions without cancellation reason:",
    len(cancelled_without_reason)
)

# Final Data Quality Summary
print("\n" + "=" * 50)
print("DATA QUALITY SUMMARY")
print("=" * 50)

print("✓ All datasets loaded successfully")
print("✓ Dataset sizes checked")
print("✓ Missing values reviewed")
print("✓ Primary key duplicates checked")
print("✓ Foreign key relationships validated")
print("✓ Date and business rules validated")
print("✓ Subscription cancellation logic validated")
print("✓ Subscription status consistency validated")

print("\nOverall Status: DATA QUALITY CHECK COMPLETED")
print("=" * 50)