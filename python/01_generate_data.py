import pandas as pd
import numpy as np
from faker import Faker
import random
from pathlib import Path

fake = Faker()

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Define project paths
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"

# Create the raw data folder if it does not exist
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Create subscription plans data
subscription_plans = pd.DataFrame({
    "plan_id": [1, 2, 3],
    "plan_name": ["Basic", "Standard", "Premium"],
    "monthly_price": [7.99, 12.99, 19.99],
    "max_devices": [1, 2, 4],
    "video_quality": ["HD", "Full HD", "4K"]
})

print(subscription_plans)

subscription_plans.to_csv(
    RAW_DATA_DIR / "subscription_plans.csv",
    index=False
)

print("\nSubscription plans saved successfully!")

# Create geography data
geography = pd.DataFrame({
    "country": [
        "United States",
        "Canada",
        "United Kingdom",
        "India",
        "Australia",
        "Germany",
        "France",
        "Japan"
    ],
    
    "region": [
        "North America",
        "North America",
        "Europe",
        "Asia",
        "Oceania",
        "Europe",
        "Europe",
        "Asia"
    ],
    
    "currency": [
        "USD",
        "CAD",
        "GBP",
        "INR",
        "AUD",
        "EUR",
        "EUR",
        "JPY"
    ]
})

print("\nGeography Data:")
print(geography)

# Save geography data to CSV
geography.to_csv(
    RAW_DATA_DIR / "geography.csv",
    index=False
)

print("\nGeography data saved successfully!")

# Create marketing campaigns data
marketing_campaigns = pd.DataFrame({
    "campaign_id": range(1, 11),

    "campaign_name": [
        "Google Search Q1",
        "Google Search Q2",
        "Instagram Growth Q1",
        "Instagram Growth Q2",
        "Facebook Awareness Q1",
        "YouTube Launch Campaign",
        "Email Re-engagement",
        "Referral Program",
        "Influencer Campaign",
        "Organic Growth"
    ],

    "channel": [
        "Google Ads",
        "Google Ads",
        "Instagram",
        "Instagram",
        "Facebook",
        "YouTube",
        "Email",
        "Referral",
        "Influencer",
        "Organic"
    ],

    "campaign_cost": [
        50000, 60000, 40000, 45000, 35000,
        55000, 10000, 25000, 30000, 5000
    ],

    "impressions": [
        1000000, 1200000, 1500000, 1600000, 1100000,
        1400000, 300000, 800000, 900000, 2000000
    ],

    "clicks": [
        50000, 60000, 75000, 80000, 40000,
        65000, 20000, 50000, 45000, 100000
    ],

    "conversions": [
        5000, 6000, 7000, 7500, 3500,
        5500, 4000, 6000, 4500, 10000
    ]
})

print("\nMarketing Campaigns Data:")
print(marketing_campaigns)

# Save marketing campaigns data to CSV
marketing_campaigns.to_csv(
    RAW_DATA_DIR / "marketing_campaigns.csv",
    index=False
)

print("\nMarketing campaigns saved successfully!")

# Customer dataset settings
NUM_CUSTOMERS = 50000

countries = geography["country"].tolist()

# Generate customer IDs
customer_ids = [
    f"C{i:06d}"
    for i in range(1, NUM_CUSTOMERS + 1)
]

# Generate realistic signup dates
signup_dates = pd.to_datetime(
    np.random.choice(
        pd.date_range("2023-01-01", "2025-12-31"),
        size=NUM_CUSTOMERS
    )
)
# Generate customer ages
ages = np.random.randint(18, 66, size=NUM_CUSTOMERS)

# Generate customer genders
genders = np.random.choice(
    ["Male", "Female", "Other"],
    size=NUM_CUSTOMERS,
    p=[0.48, 0.48, 0.04]
)

# Generate customer countries with realistic distribution
customer_countries = np.random.choice(
    countries,
    size=NUM_CUSTOMERS,
    p=[
        0.30,  # United States
        0.10,  # Canada
        0.12,  # United Kingdom
        0.18,  # India
        0.07,  # Australia
        0.08,  # Germany
        0.07,  # France
        0.08   # Japan
    ]
)

# Define cities for each country
cities_by_country = {
    "United States": ["New York", "Los Angeles", "Chicago", "San Francisco"],
    "Canada": ["Toronto", "Vancouver", "Montreal"],
    "United Kingdom": ["London", "Manchester", "Birmingham"],
    "India": ["Mumbai", "Delhi", "Bengaluru", "Ahmedabad"],
    "Australia": ["Sydney", "Melbourne", "Brisbane"],
    "Germany": ["Berlin", "Munich", "Hamburg"],
    "France": ["Paris", "Lyon", "Marseille"],
    "Japan": ["Tokyo", "Osaka", "Kyoto"]
}

# Assign a realistic city to each customer
customer_cities = [
    random.choice(cities_by_country[country])
    for country in customer_countries
]

# Assign each customer to a marketing campaign
customer_campaign_ids = np.random.choice(
    marketing_campaigns["campaign_id"],
    size=NUM_CUSTOMERS
)

# Create the customers DataFrame
customers = pd.DataFrame({
    "customer_id": customer_ids,
    "signup_date": signup_dates,
    "age": ages,
    "gender": genders,
    "country": customer_countries,
    "city": customer_cities,
    "campaign_id": customer_campaign_ids
})

# Add acquisition channel using the campaign information
campaign_channel_map = marketing_campaigns.set_index(
    "campaign_id"
)["channel"].to_dict()

customers["acquisition_channel"] = customers[
    "campaign_id"
].map(campaign_channel_map)

print("\nCustomers Data:")
print(customers.head())

# Validate customers data

print("\n--- Customer Data Validation ---")

# Check total number of customers
print("Total customers:", len(customers))

# Check for duplicate customer IDs
print("Duplicate customer IDs:", customers["customer_id"].duplicated().sum())

# Check for missing values
print("\nMissing values:")
print(customers.isnull().sum())

# Save customers data to CSV
customers.to_csv(
    RAW_DATA_DIR / "customers.csv",
    index=False
)

print("\nCustomers data saved successfully!")
NUM_SUBSCRIPTIONS = 60000

subscription_statuses = [
    "Active",
    "Cancelled"
]

# Generate subscription IDs
subscription_ids = [
    f"S{i:06d}"
    for i in range(1, NUM_SUBSCRIPTIONS + 1)
]

# Assign each subscription to a customer
subscription_customer_ids = np.random.choice(
    customers["customer_id"],
    size=NUM_SUBSCRIPTIONS,
    replace=True
)

subscription_plan_ids = np.random.choice(
    subscription_plans["plan_id"],
    size=NUM_SUBSCRIPTIONS,
    p=[0.40, 0.45, 0.15]
)

# Create a lookup for customer signup dates
signup_date_map = customers.set_index(
    "customer_id"
)["signup_date"].to_dict()

# Get the signup date for each subscription
subscription_signup_dates = pd.to_datetime(
    [
        signup_date_map[customer_id]
        for customer_id in subscription_customer_ids
    ]
)

# Generate subscription start dates
subscription_start_dates = (
    subscription_signup_dates
    + pd.to_timedelta(
        np.random.randint(
            0,
            8,
            size=NUM_SUBSCRIPTIONS
        ),
        unit="D"
    )
)

# Generate subscription statuses
subscription_status = np.random.choice(
    subscription_statuses,
    size=NUM_SUBSCRIPTIONS,
    p=[0.65, 0.35]
)

# Create end dates
subscription_end_dates = []

for start_date, status in zip(
    subscription_start_dates,
    subscription_status
):
    if status == "Cancelled":
        # Subscription lasts between 1 and 24 months
        months_active = random.randint(1, 24)

        end_date = (
            start_date
            + pd.DateOffset(months=months_active)
        )

        subscription_end_dates.append(end_date)

    else:
        # Active subscriptions do not have an end date
        subscription_end_dates.append(pd.NaT)


# Define possible cancellation reasons
cancellation_reasons = [
    "Too Expensive",
    "Not Enough Content",
    "Technical Issues",
    "Low Engagement",
    "Switched to Competitor"
]

# Assign cancellation reasons
subscription_cancellation_reasons = []

for status in subscription_status:

    if status == "Cancelled":
        reason = random.choice(cancellation_reasons)
        subscription_cancellation_reasons.append(reason)

    else:
        subscription_cancellation_reasons.append(None)

# Create the subscriptions DataFrame
subscriptions = pd.DataFrame({
    "subscription_id": subscription_ids,
    "customer_id": subscription_customer_ids,
    "plan_id": subscription_plan_ids,
    "start_date": subscription_start_dates,
    "end_date": subscription_end_dates,
    "subscription_status": subscription_status,
    "cancellation_reason": subscription_cancellation_reasons
})

# Display the first 5 subscriptions
print("\nSubscriptions Data:")
print(subscriptions.head())

# Validate subscriptions data

print("\n--- Subscription Data Validation ---")

# Check total subscriptions
print("Total subscriptions:", len(subscriptions))

# Check for duplicate subscription IDs
print(
    "Duplicate subscription IDs:",
    subscriptions["subscription_id"].duplicated().sum()
)

# Check for missing customer IDs
print(
    "Missing customer IDs:",
    subscriptions["customer_id"].isnull().sum()
)

# Check that cancelled subscriptions have an end date
cancelled_without_end_date = subscriptions[
    (subscriptions["subscription_status"] == "Cancelled")
    & (subscriptions["end_date"].isnull())
]

print(
    "Cancelled subscriptions without end date:",
    len(cancelled_without_end_date)
)


# Save subscriptions data to CSV
subscriptions.to_csv(
    RAW_DATA_DIR / "subscriptions.csv",
    index=False
)

print("\nSubscriptions data saved successfully!")

# Transaction dataset settings
NUM_TRANSACTIONS = 200000

transaction_statuses = [
    "Successful",
    "Failed",
    "Refunded"
]

# Generate transaction IDs
transaction_ids = [
    f"T{i:07d}"
    for i in range(1, NUM_TRANSACTIONS + 1)
]

# Assign each transaction to a subscription
transaction_subscription_ids = np.random.choice(
    subscriptions["subscription_id"],
    size=NUM_TRANSACTIONS,
    replace=True
)

# Create a lookup from subscription ID to customer ID
subscription_customer_map = subscriptions.set_index(
    "subscription_id"
)["customer_id"].to_dict()

# Assign the correct customer to each transaction
transaction_customer_ids = [
    subscription_customer_map[subscription_id]
    for subscription_id in transaction_subscription_ids
]


# Create a lookup from subscription ID to start date
subscription_start_date_map = subscriptions.set_index(
    "subscription_id"
)["start_date"].to_dict()

# Get the start date for each transaction
transaction_subscription_start_dates = pd.to_datetime(
    [
        subscription_start_date_map[subscription_id]
        for subscription_id in transaction_subscription_ids
    ]
)

# Generate transaction dates after subscription start
transaction_dates = (
    transaction_subscription_start_dates
    + pd.to_timedelta(
        np.random.randint(
            0,
            730,
            size=NUM_TRANSACTIONS
        ),
        unit="D"
    )
)

# Create a lookup from subscription ID to end date
subscription_end_date_map = subscriptions.set_index(
    "subscription_id"
)["end_date"].to_dict()

# Adjust transaction dates for cancelled subscriptions
adjusted_transaction_dates = []

for subscription_id, transaction_date in zip(
    transaction_subscription_ids,
    transaction_dates
):
    end_date = subscription_end_date_map[subscription_id]

    # If the subscription is cancelled and the transaction
    # happens after the end date, move it to a valid date
    if pd.notna(end_date) and transaction_date > end_date:
        transaction_date = end_date - pd.Timedelta(
            days=random.randint(0, 30)
        )

    adjusted_transaction_dates.append(transaction_date)

transaction_dates = pd.to_datetime(adjusted_transaction_dates)


# Create a lookup from subscription ID to plan ID
subscription_plan_map = subscriptions.set_index(
    "subscription_id"
)["plan_id"].to_dict()

# Create a lookup from plan ID to monthly price
plan_price_map = subscription_plans.set_index(
    "plan_id"
)["monthly_price"].to_dict()

# Get the correct plan price for each transaction
transaction_amounts = []

for subscription_id in transaction_subscription_ids:
    plan_id = subscription_plan_map[subscription_id]
    price = plan_price_map[plan_id]

    transaction_amounts.append(price)

transaction_amounts = np.array(transaction_amounts)

# Generate transaction statuses
transaction_status = np.random.choice(
    transaction_statuses,
    size=NUM_TRANSACTIONS,
    p=[0.94, 0.04, 0.02]
)

# Generate payment methods
payment_methods = np.random.choice(
    [
        "Credit Card",
        "Debit Card",
        "PayPal",
        "Digital Wallet"
    ],
    size=NUM_TRANSACTIONS,
    p=[0.45, 0.25, 0.15, 0.15]
)

# Create the transactions DataFrame
transactions = pd.DataFrame({
    "transaction_id": transaction_ids,
    "subscription_id": transaction_subscription_ids,
    "customer_id": transaction_customer_ids,
    "transaction_date": transaction_dates,
    "amount": transaction_amounts,
    "transaction_status": transaction_status,
    "payment_method": payment_methods
})

# Display the first 5 transactions
print("\nTransactions Data:")
print(transactions.head())


# Validate transactions data

print("\n--- Transaction Data Validation ---")

# Check total transactions
print("Total transactions:", len(transactions))

# Check duplicate transaction IDs
print(
    "Duplicate transaction IDs:",
    transactions["transaction_id"].duplicated().sum()
)

# Check missing values
print("\nMissing values:")
print(transactions.isnull().sum())

# Check for negative or zero amounts
invalid_amounts = transactions[
    transactions["amount"] <= 0
]

print(
    "\nTransactions with invalid amounts:",
    len(invalid_amounts)
)

# Save transactions data to CSV
transactions.to_csv(
    RAW_DATA_DIR / "transactions.csv",
    index=False
)

print("\nTransactions data saved successfully!")

# Content dataset settings
NUM_CONTENT = 5000

genres = [
    "Action",
    "Comedy",
    "Drama",
    "Thriller",
    "Sci-Fi",
    "Romance",
    "Documentary",
    "Animation"
]

content_types = [
    "Movie",
    "Series"
]

# Generate content IDs
content_ids = [
    f"CT{i:05d}"
    for i in range(1, NUM_CONTENT + 1)
]

# Generate fictional content titles
content_titles = [
    f"{fake.word().title()} {fake.word().title()}"
    for _ in range(NUM_CONTENT)
]

# Assign genres to content
content_genres = np.random.choice(
    genres,
    size=NUM_CONTENT
)

# Assign content types
content_type_values = np.random.choice(
    content_types,
    size=NUM_CONTENT,
    p=[0.60, 0.40]
)

# Generate content release years
release_years = np.random.randint(
    2010,
    2027,
    size=NUM_CONTENT
)

# Generate content duration in minutes
content_durations = []

for content_type in content_type_values:
    
    if content_type == "Movie":
        duration = random.randint(80, 180)
    else:
        # Average episode duration for a series
        duration = random.randint(20, 70)
    
    content_durations.append(duration)

# Create the content DataFrame
content = pd.DataFrame({
    "content_id": content_ids,
    "title": content_titles,
    "genre": content_genres,
    "content_type": content_type_values,
    "release_year": release_years,
    "duration_minutes": content_durations
})

# Display the first 5 rows
print("\nContent Data:")
print(content.head())

# Validate content data

print("\n--- Content Data Validation ---")

# Check total content records
print("Total content records:", len(content))

# Check duplicate content IDs
print(
    "Duplicate content IDs:",
    content["content_id"].duplicated().sum()
)

# Check missing values
print("\nMissing values:")
print(content.isnull().sum())

# Check invalid durations
invalid_durations = content[
    content["duration_minutes"] <= 0
]

print(
    "\nContent with invalid durations:",
    len(invalid_durations)
)

# Save content data to CSV
content.to_csv(
    RAW_DATA_DIR / "content.csv",
    index=False
)

print("\nContent data saved successfully!")

# User events dataset settings
NUM_EVENTS = 500000

event_types = [
    "Play",
    "Pause",
    "Complete",
    "Search",
    "Like"
]

device_types = [
    "Mobile",
    "Web",
    "Smart TV",
    "Tablet"
]

# Generate event IDs
event_ids = [
    f"E{i:07d}"
    for i in range(1, NUM_EVENTS + 1)
]

# Assign each event to a customer
event_customer_ids = np.random.choice(
    customers["customer_id"],
    size=NUM_EVENTS,
    replace=True
)

# Assign content to each user event
event_content_ids = np.random.choice(
    content["content_id"],
    size=NUM_EVENTS,
    replace=True
)

# Generate realistic event timestamps
event_start = pd.Timestamp("2023-01-01")
event_end = pd.Timestamp("2026-12-31")

event_timestamps = event_start + pd.to_timedelta(
    np.random.randint(
        0,
        (event_end - event_start).days + 1,
        size=NUM_EVENTS
    ),
    unit="D"
)

# Add random hours, minutes, and seconds
event_timestamps = (
    event_timestamps
    + pd.to_timedelta(
        np.random.randint(0, 24, size=NUM_EVENTS),
        unit="h"
    )
    + pd.to_timedelta(
        np.random.randint(0, 60, size=NUM_EVENTS),
        unit="m"
    )
    + pd.to_timedelta(
        np.random.randint(0, 60, size=NUM_EVENTS),
        unit="s"
    )
)

# Generate event types
event_type_values = np.random.choice(
    event_types,
    size=NUM_EVENTS,
    p=[0.45, 0.15, 0.20, 0.10, 0.10]
)

# Generate device types
event_device_types = np.random.choice(
    device_types,
    size=NUM_EVENTS,
    p=[0.35, 0.25, 0.30, 0.10]
)

# Generate watch duration based on event type
watch_durations = []

for event_type in event_type_values:

    if event_type == "Play":
        duration = random.randint(1, 120)

    elif event_type == "Pause":
        duration = random.randint(1, 60)

    elif event_type == "Complete":
        duration = random.randint(20, 180)

    else:
        # Search and Like events do not involve watching content
        duration = 0

    watch_durations.append(duration)
# Create the user_events DataFrame
user_events = pd.DataFrame({
    "event_id": event_ids,
    "customer_id": event_customer_ids,
    "content_id": event_content_ids,
    "event_timestamp": event_timestamps,
    "event_type": event_type_values,
    "watch_duration_minutes": watch_durations,
    "device_type": event_device_types
})

# Display the first 5 events
print("\nUser Events Data:")
print(user_events.head())

# Validate user events data

print("\n--- User Events Data Validation ---")

# Check total events
print("Total events:", len(user_events))

# Check duplicate event IDs
print(
    "Duplicate event IDs:",
    user_events["event_id"].duplicated().sum()
)

# Check missing values
print("\nMissing values:")
print(user_events.isnull().sum())

# Check for negative watch durations
invalid_watch_duration = user_events[
    user_events["watch_duration_minutes"] < 0
]

print(
    "\nEvents with negative watch duration:",
    len(invalid_watch_duration)
)

# Save user events data to CSV
user_events.to_csv(
    RAW_DATA_DIR / "user_events.csv",
    index=False
)

print("\nUser events data saved successfully!")