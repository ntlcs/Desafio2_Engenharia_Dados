import pandas as pd
from sqlalchemy import create_engine

# Defina seu arquivo CSV como fonte de dados
csv_file_path = 'caminho/arquivo.csv'

# Leia o CSV para um DataFrame do pandas
df = pd.read_csv(csv_file_path)

# Etapa de Transformação: Limpeza dos Dados
# Vamos assumir que você deseja lidar com valores ausentes preenchendo-os com a média
df.fillna(df.mean(), inplace=True)

# Etapa de Transformação: Formatação
# Vamos converter uma coluna para o formato datetime, por exemplo
df['data'] = pd.to_datetime(df['data'], format='%Y-%m-%d')

# Etapa de Transformação: Criação de novas colunas
# Vamos criar uma nova coluna calculada
df['nova_coluna'] = df['coluna_existente'] * 2

# Etapa de Carga: Salvar no banco de dados (SQLite neste exemplo)
database_path = 'caminho/banco.db'
engine = create_engine(f'sqlite:///{database_path}')
df.to_sql('nome_da_tabela', engine, index=False, if_exists='replace')

print("ETL concluído e dados carregados no banco de dados.")
