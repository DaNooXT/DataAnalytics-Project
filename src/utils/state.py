import pandas as pd

state_rules = {
    "AC": [
        "AC",
        "ACRE"
    ],

    "AL": [
        "AL",
        "ALAGOAS"
    ],

    "AP": [
        "AP",
        "AMAPA",
        "AMAPÁ"
    ],

    "AM": [
        "AM",
        "AMAZONAS"
    ],

    "BA": [
        "BA",
        "BAHIA"
    ],

    "CE": [
        "CE",
        "CEARA",
        "CEARÁ"
    ],

    "DF": [
        "DF",
        "DISTRITO FEDERAL"
    ],

    "ES": [
        "ES",
        "ESPIRITO SANTO",
        "ESPÍRITO SANTO"
    ],

    "GO": [
        "GO",
        "GOIAS",
        "GOIÁS"
    ],

    "MA": [
        "MA",
        "MARANHAO",
        "MARANHÃO"
    ],

    "MT": [
        "MT",
        "MATO GROSSO"
    ],

    "MS": [
        "MS",
        "MATO GROSSO DO SUL"
    ],

    "MG": [
        "MG",
        "MINAS GERAIS"
    ],

    "PA": [
        "PA",
        "PARA",
        "PARÁ"
    ],

    "PB": [
        "PB",
        "PARAIBA",
        "PARAÍBA"
    ],

    "PR": [
        "PR",
        "PARANA",
        "PARANÁ"
    ],

    "PE": [
        "PE",
        "PERNAMBUCO"
    ],

    "PI": [
        "PI",
        "PIAUI",
        "PIAUÍ"
    ],

    "RJ": [
        "RJ",
        "RIO DE JANEIRO"
    ],

    "RN": [
        "RN",
        "RIO GRANDE DO NORTE"
    ],

    "RS": [
        "RS",
        "RIO GRANDE DO SUL",
        "RGS",
        "R.G.S"
    ],

    "RO": [
        "RO",
        "RONDONIA",
        "RONDÔNIA"
    ],

    "RR": [
        "RR",
        "RORAIMA"
    ],

    "SC": [
        "SC",
        "SANTA CATARINA"
    ],

    "SP": [
        "SP",
        "SAO PAULO",
        "SÃO PAULO"
    ],

    "SE": [
        "SE",
        "SERGIPE"
    ],

    "TO": [
        "TO",
        "TOCANTINS"
    ]
}


def normalize_state(state):

    if pd.isna(state):
        return "SEM ESTADO"

    state = str(state).strip().upper()

    state = (
        state
        .replace("Á","A")
        .replace("Ã","A")
        .replace("Â","A")
        .replace("É","E")
        .replace("Ê","E")
        .replace("Í","I")
        .replace("Ó","O")
        .replace("Ô","O")
        .replace("Ú","U")
        .replace("Ç","C")
    )

    for uf, names in state_rules.items():

        for name in names:

            if name in state:
                return uf

    return "INVALIDO"