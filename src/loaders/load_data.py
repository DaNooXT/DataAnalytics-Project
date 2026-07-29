import pandas as pd

def load_clients ():
    df_clients = pd.read_csv("data/raw/clients.csv")
    return df_clients

def load_orders ():
    df_orders = pd.read_csv("data/raw/orders.csv")
    return df_orders

def load_payments ():
    df_payments = pd.read_csv("data/raw/payments.csv")
    return df_payments

def load_products ():
    df_products = pd.read_csv("data/raw/products.csv")
    return df_products