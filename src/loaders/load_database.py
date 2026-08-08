from src.database import engine
import pandas as pd

def load_database (
        df_clients,
        df_products,
        df_orders,
        df_payments
):
    
    df_clients.to_sql (
        "clients",
        engine,
        if_exists="append",
        index=False
    )

    df_products.to_sql (
        "products",
        engine,
        if_exists="append",
        index=False
    )

    df_orders.to_sql (
        "orders",
        engine,
        if_exists="append",
        index=False
    )

    df_payments.to_sql (
        "payments",
        engine,
        if_exists="append",
        index=False
    )

    return print (
        "Successfuly load"
    )