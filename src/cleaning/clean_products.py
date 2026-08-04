import pandas as pd
import numpy as np
from utils.categories import define_category

def clean_products (df):
    df_products = df.copy()

    df_products['preco'] = pd.to_numeric (
            df_products['preco'],
            errors='coerce'
    )

    df_products = df_products[df_products['preco'] > 0]

    df_products['preco'] = (
        df_products['preco']
        .fillna (
            df_products['preco'].median()
        )
    )

    df_products['estoque'] = (
        pd.to_numeric (
            df_products['estoque'],
            errors='coerce'
        )
        .fillna(0)
        .astype(int)
    )

    df_products['estoque'] = np.where (
        (df_products['estoque'] < 0),
        0,
        df_products['estoque']
    )

    df_products = df_products[df_products['estoque'] != 0]

    df_products['data_cadastro'] = pd.to_datetime (
        df_products['data_cadastro'],
        errors='coerce',
        dayfirst=False
    )

    today = pd.Timestamp.today()
    df_products['data_cadastro'] = np.where (
        ((df_products['data_cadastro'] > today) | (df_products['data_cadastro'].isna())),
        pd.NaT,
        df_products['data_cadastro']
    )

    df_products['status_data'] = np.where (
        (df_products['data_cadastro'].isna()),
        "SEM DATA",
        "COM DATA"
    )

    df_products['nome'] = (
        df_products['nome']
        .str.strip()    
        .str.upper()
        .dropna()     
    )

    df_products['categoria'] = (
        df_products['categoria']
        .str.strip()    
        .str.upper()     
        .dropna()
    )

    df_products['categoria'] = (
        df_products['nome']
        .apply(define_category)
    )

    return df_products