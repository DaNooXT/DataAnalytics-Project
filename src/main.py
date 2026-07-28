import loaders.load_data as ld     

def main ():
    load_analysis_clients = ld.load_clients()
    df_analysis_orders = ld.load_orders()
    df_analysis_payments = ld.load_payments()
    df_analysis_products = ld.load_products()

if __name__ == "__main__":
    main()