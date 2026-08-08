import pandas as pd
import numpy as np

def clean_orders (df, df2, df3):
    df_orders = df.copy()
    df_products = df2.copy()
    df_clients = df3.copy()
    
    df_orders['quantidade'] = pd.to_numeric (
        df_orders['quantidade'],
        errors="coerce"
    )

    df_orders['data_pedido'] = pd.to_datetime (
        df_orders['data_pedido'],
        errors="coerce",
        dayfirst=False
    )

    df_orders['valor_total'] = pd.to_numeric (
        df_orders['valor_total'],
        errors='coerce'
    ).astype(float)

    df_orders['valor_total'] = (
        df_orders['valor_total']
        .fillna (
            df_orders['valor_total'].median()
        )
        .round(2)
    )

    df_orders["status"] = (
        df_orders["status"]
        .fillna("CANCELADO")
        .str.strip()
        .str.upper()
        .str.replace(
            r"(.)\1+",
            r"\1",
            regex=True
        )
    )

    df_orders['frete'] = pd.to_numeric (
        df_orders['frete'],
        errors='coerce'
    ).astype(float)

    df_orders['frete'] = (
        df_orders['frete']
        .fillna (
            df_orders['frete'].mean()
        )
        .round(2)
    )

    df_orders['status_data'] = (
        np.where (
            (df_orders['data_pedido'].isna()), 
            "PEDIDO SEM DATA", 
            "PEDIDO COM DATA"
        )
    )

    df_orders['desconto'] = df_orders['desconto'].fillna(0)

    df_orders = df_orders.dropna(subset=['quantidade'])

    df_orders = df_orders[
        df_orders["produto_id"].isin(df_products["produto_id"])
    ].copy()

    df_orders = df_orders[
        df_orders["cliente_id"].isin(df_clients["cliente_id"])
    ].copy()

    return df_orders