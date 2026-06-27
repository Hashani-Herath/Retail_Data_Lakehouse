{{ config(materialized='table') }}

SELECT 
    order_id,
    customer_id,
    order_timestamp as order_date
FROM read_parquet('../retail_lakehouse/data_lake/silver_orders.parquet')