import pandas as pd
import numpy as np

def clean_clients (df):
    df_clients = df.copy()

    df_clients["idade"] = pd.to_numeric(
        df_clients["idade"],
        errors="coerce"
    )

    df_clients.loc[
        df_clients["idade"] <= 0,
        "idade"
    ] = np.nan


    df_clients["idade"] = df_clients["idade"].fillna(
        df_clients["idade"].median()
        )

    today = pd.Timestamp.today()
    df_clients["data_cadastro"] = (
        pd.to_datetime(
            df_clients["data_cadastro"], 
            errors="coerce", 
            dayfirst=False
            )
        )

    df_clients = df_clients[
        df_clients["data_cadastro"] <= today
        ]

    df_clients["data_cadastro"] = df_clients["data_cadastro"].dt.strftime("%y-%m-%d")

    df_clients["email"] = df_clients['email'].fillna("Invalido")

    EMAIL_REGEX = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    df_clients["email"] = np.where(
        (df_clients["email"].str.fullmatch(EMAIL_REGEX)),
        df_clients["email"],
        "invalido"
    )

    df_clients["telefone"] = df_clients['telefone'].fillna("Invalido")

    PHONE_REGEX = r"\(\d{2}\)\d{5}-\d{4}"
    df_clients["telefone"] = np.where(
        (df_clients["telefone"].str.fullmatch(PHONE_REGEX, na=False)),
        df_clients["telefone"],
        "Invalido"
        )

    df_clients["cidade"] = df_clients['cidade'].fillna("Invalido")

    return df_clients