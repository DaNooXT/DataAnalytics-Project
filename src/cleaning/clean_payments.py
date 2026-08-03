import pandas as pd
import numpy as np

def clean_payments (df):
    df_payments = df.copy()

        
    df_payments['parcelas'] = (
        pd.to_numeric (
            df_payments['parcelas'],
            errors="coerce",
        )
        .fillna(0)
        .astype(int)
    )

    df_payments['valor_pago'] = pd.to_numeric (
        df_payments['valor_pago'],
        errors="coerce"
    ).astype(float)

    df_payments['valor_pago'] = np.where (
            (df_payments['valor_pago'] < 0),
            np.nan,
            df_payments['valor_pago']
    )

    df_payments['valor_pago'] = (
        df_payments['valor_pago']
        .fillna(
            df_payments['valor_pago'].median()
        )
    )

    df_payments['data_pagamento'] = pd.to_datetime (
        df_payments['data_pagamento'],
        errors='coerce',
        dayfirst=False
    )

    df_payments['forma_pagamento'] = (
        df_payments['forma_pagamento']
        .fillna("CANCELADO")
        .str.strip()
        .str.upper()
        .str.replace (
            r"(.)\1+",
            r"\1",
            regex=True
        )
    )

    df_payments['bandeira_cartao'] = (
        df_payments['bandeira_cartao']
        .str.strip()
        .str.upper()
        .fillna("SEM BANDEIRA")
    )

    df_payments['status_data'] = (
        np.where (
            (df_payments['data_pagamento'].isna()),
            "SEM DATA",
            "COM DATA"
        )
    )

    df_payments['status'] = (
        df_payments['status']
        .fillna("CANCELADO")
    )

    return df_payments