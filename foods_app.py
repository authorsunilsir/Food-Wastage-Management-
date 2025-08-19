
import streamlit as st
import pandas as pd
import sqlite3

st.title("Local Food Wastage Management System")

# Database connection (using a relative path assuming the db is in the same repo)
conn = sqlite3.connect("food_wastage.db")

# Display provider data
st.header("Food Providers")
providers_df = pd.read_sql_query("SELECT * FROM providers", conn)
st.dataframe(providers_df)

# Display food listings
st.header("Food Listings")
food_listings_df = pd.read_sql_query("SELECT * FROM food_listings", conn)
st.dataframe(food_listings_df)

# Display claims data
st.header("Claims")
claims_df = pd.read_sql_query("SELECT * FROM claims", conn)
st.dataframe(claims_df)

# Display receivers data
st.header("Receivers")
receivers_df = pd.read_sql_query("SELECT * FROM receivers", conn)
st.dataframe(receivers_df)

# Example Query: City with highest number of providers
st.header("City with Highest Number of Providers")
query_highest_providers_city = """
    SELECT City, COUNT(*) AS Provider_Count
    FROM providers
    GROUP BY City
    ORDER BY Provider_Count DESC
    LIMIT 1;
"""
highest_providers_city_df = pd.read_sql_query(query_highest_providers_city, conn)
st.dataframe(highest_providers_city_df)


# Example Query: Top 10 most claimed food listings
st.header("Top 10 Most Claimed Food Listings")
query_top_claimed_foods = """
    SELECT
        fl.Food_Name,
        COUNT(c.Claim_ID) AS TotalClaims
    FROM
        food_listings fl
    JOIN
        claims c ON fl.Food_ID = c.Food_ID
    GROUP BY
        fl.Food_Name
    ORDER BY
        TotalClaims DESC
    LIMIT 10;
"""
top_claimed_foods_df = pd.read_sql_query(query_top_claimed_foods, conn)
st.dataframe(top_claimed_foods_df)

# Example Query: Number of claims by status
st.header("Distribution of Claims by Status")
query_claims_status = """
    SELECT
        Status,
        COUNT(*) AS NumberOfClaims
    FROM
        claims
    GROUP BY
        Status;
"""
claims_status_df = pd.read_sql_query(query_claims_status, conn)
st.dataframe(claims_status_df)


# Close the database connection
conn.close()

