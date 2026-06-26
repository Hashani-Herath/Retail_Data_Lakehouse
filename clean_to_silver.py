from pathlib import Path

import duckdb

# Initialize a free local DuckDB database file
conn = duckdb.connect("retail_lakehouse.db")

base_dir = Path(__file__).resolve().parent / "retail_lakehouse" / "data_lake"
customers_csv = base_dir / "raw_customers.csv"
orders_csv = base_dir / "raw_orders.csv"
silver_customers = base_dir / "silver_customers.parquet"
silver_orders = base_dir / "silver_orders.parquet"

print("Step 1: Reading Bronze CSV files and moving to Silver Layer...")

# Use DuckDB to clean data on the fly and save as highly compressed Parquet format
conn.execute(f"""
    COPY (
        SELECT 
            customer_id::VARCHAR as customer_id,
            TRIM(name) as customer_name,
            COALESCE(
                try_strptime(CAST(signup_date AS VARCHAR), '%Y-%m-%d')::DATE,
                try_strptime(CAST(signup_date AS VARCHAR), '%d/%m/%Y')::DATE,
                DATE '1900-01-01'
            ) as signup_date
        FROM read_csv_auto('{customers_csv.as_posix()}')
    ) TO '{silver_customers.as_posix()}' (FORMAT 'PARQUET');
""")

conn.execute(f"""
    COPY (
        SELECT 
            order_id::VARCHAR as order_id,
            customer_id::VARCHAR as customer_id,
            order_date::TIMESTAMP as order_timestamp
        FROM read_csv_auto('{orders_csv.as_posix()}')
        WHERE order_id IS NOT NULL  -- Remove broken data rows
    ) TO '{silver_orders.as_posix()}' (FORMAT 'PARQUET');
""")

print("✔ Success! Silver cleaned Parquet files created inside data_lake/ folder.")
conn.close()