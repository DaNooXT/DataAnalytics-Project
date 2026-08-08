# DataAnalytics Project

Projeto de ETL e preparação de dados para análise analítica, com foco em normalização, limpeza e persistência de tabelas de clientes, produtos, pedidos e pagamentos.

## Visão Geral

Este repositório implementa um pipeline de dados que lê arquivos CSV crus localizados em `data/raw`, aplica regras de limpeza em cada domínio, exporta os DataFrames tratados para `data/clean` e os carrega em um banco relacional configurado por variável de ambiente.

A arquitetura está organizada em módulos separados por responsabilidade:

- `src/main.py` — orquestra o pipeline completo.
- `src/loaders/load_data.py` — carrega as bases brutas em memória.
- `src/cleaning/` — módulos responsáveis pela validação, correção e enriquecimento dos dados.
- `src/loaders/load_database.py` — persiste os DataFrames tratados no banco.
- `src/database.py` — cria a engine SQLAlchemy.
- `src/utils/` — utilitários de normalização.

## Fluxo do Projeto

1. Leitura dos CSVs brutos.
2. Limpeza e enriquecimento por tabela.
3. Exportação dos clean DataFrames para CSV.
4. Persistência em banco relacional.

## Estrutura de Diretórios

```text
DataAnalytics-Project/
├── data/
│   ├── raw/          # base de entrada sem tratamento
│   └── clean/        # exportação final em CSV
├── notebooks/        # experimentos e exploração
├── src/
│   ├── cleaning/     # funções de cleansing
│   ├── loaders/      # loaders de dados e banco
│   └── utils/        # auxiliares
└── README.md
```

## Requisitos

O projeto depende de bibliotecas como `pandas`, `numpy`, `sqlalchemy`, `python-dotenv` e `psycopg2` para integração com PostgreSQL.

Você pode instalar as dependências em um ambiente virtual com:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

No Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Configuração do Banco

O projeto lê a URL do banco a partir de uma variável de ambiente `DATABASE_URL`, definida no arquivo `.env`:

```env
DATABASE_URL=postgresql+psycopg2://usuario:senha@host:5432/nome_do_banco
```

Essa URL é carregada por `src/loaders/load_env.py` e utilizada para montar a engine SQLAlchemy definida em `src/database.py`.

## Como Executar

Depois de instalar as dependências e configurar o banco, execute:

```bash
python -m src.main
```

Isso produzirá as tabelas limpas em `data/clean` e tentará carregar cada uma no banco via `to_sql`.

## Tabelas Processadas

- `clients`
- `products`
- `orders`
- `payments`

## Observações

- Os arquivos em `data/raw` são a entrada do pipeline.
- Os CSVs em `data/clean` são o estado transformado e pronto para uso analítico.
- A lógica de limpeza está modularizada para facilitar manutenção e evolução do ETL.
