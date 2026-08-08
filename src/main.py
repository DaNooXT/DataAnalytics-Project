import src.loaders.load_data as ld  
from src.cleaning.clean_clients import clean_clients 
from src.cleaning.clean_orders import clean_orders
from src.cleaning.clean_payments import clean_payments
from src.cleaning.clean_products import clean_products
from src.loaders.load_database import load_database

def main ():
    #load all tables
    df_clients = ld.load_clients()
    df_orders = ld.load_orders()
    df_payments = ld.load_payments()
    df_products = ld.load_products()

    #clean allk tables
    df_clients = clean_clients(df_clients)
    df_products = clean_products(df_products)
    df_orders = clean_orders(df_orders, df_products, df_clients)
    df_payments = clean_payments(df_payments, df_orders)

    #export clean DataFrames
    df_clients.to_csv("data/clean/clients.csv", index=False)
    df_products.to_csv("data/clean/products.csv", index=False)
    df_orders.to_csv("data/clean/orders.csv", index=False)
    df_payments.to_csv("data/clean/payments.csv", index=False)

    #load to database
    load_database(
        df_clients,
        df_products,
        df_orders,
        df_payments
    )

if __name__ == "__main__":
    main()