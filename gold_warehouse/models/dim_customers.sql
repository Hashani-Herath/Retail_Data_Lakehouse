{{ config(materialized='table') }}

SELECT 
    customer_id,
    customer_name,
    signup_date
FROM read_parquet('../retail_lakehouse/data_lake/silver_customers.parquet')