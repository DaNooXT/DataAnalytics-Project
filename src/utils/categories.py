import pandas as pd

category_rules = {
    "MOUSE": [
        "MOUSE"
    ],
    
    "TECLADO": [
        "TECLADO"
    ],
    
    "HEADSET": [
        "HEADSET",
        "FONE"
    ],
    
    "MONITOR": [
        "MONITOR"
    ],
    
    "SSD": [
        "SSD"
    ],
    
    "HD": [
        "HD"
    ],
    
    "MEMÓRIA": [
        "MEMÓRIA",
        "MEMORIA"
    ],
    
    "PLACA DE VÍDEO": [
        "RTX",
        "RX",
        "PLACA VIDEO",
        "PLACA DE VÍDEO"
    ],
    
    "PROCESSADOR": [
        "RYZEN",
        "CORE I",
        "INTEL"
    ],
    
    "PLACA MÃE": [
        "PLACA MÃE",
        "PLACA MAE"
    ],
    
    "FONTE": [
        "FONTE"
    ],
    
    "GABINETE": [
        "GABINETE"
    ],
    
    "IMPRESSORA": [
        "IMPRESSORA"
    ],
    
    "WEBCAM": [
        "WEBCAM"
    ],
    
    "NOTEBOOK": [
        "NOTEBOOK"
    ]
}

def define_category (product):
    if pd.isna(product):
        return "Sem Categoria"
    for category, keywords in category_rules.items():

        for keyword in keywords:

            if keyword in product:
                return category

    return "Outros"