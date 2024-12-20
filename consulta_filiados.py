import os
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime, timedelta
from sqlalchemy import create_engine

# Carregar configurações do .env
load_dotenv()

# Configurações de conexão
server = os.getenv('SERVER')
database = os.getenv('DATABASE')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

# String de conexão SQLAlchemy
conn_str = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

def buscar_filiados_dia_anterior():
    try:
        # Criar engine SQLAlchemy
        engine = create_engine(conn_str)

        # Consulta SQL
        query = '''
            SELECT DISTINCT 
                '16142' AS PLANO,
                CASE 
                    WHEN f.id_filiado_pai IS NULL THEN f.matricula 
                    ELSE p.cpf 
                END AS IDENTIFICACAO,
                p.NOME,
                '0' AS LIMITE,
                p.CPF
            FROM FILIADO f
            JOIN pessoa p ON p.id_pessoa = f.id_pessoa
            WHERE 1=1
                AND f.DT_FILIACAO >= CAST(DATEADD(DAY, -1, GETDATE()) AS DATE)
                AND f.DT_FILIACAO < CAST(GETDATE() AS DATE)
                AND p.cpf IS NOT NULL
                AND f.ativo = 1
        '''
        
        # Executar a consulta e armazenar os resultados em um DataFrame
        df = pd.read_sql(query, engine)

        if df.empty:
            print("Nenhum filiado encontrado para o dia anterior.")
            return

        # Converter IDENTIFICACAO e CPF para string e garantir zeros à esquerda
        df['IDENTIFICACAO'] = df['IDENTIFICACAO'].astype(str).str.zfill(11)
        df['CPF'] = df['CPF'].astype(str).str.zfill(11)

        # Ordenar as colunas conforme o layout
        df = df[['PLANO', 'IDENTIFICACAO', 'NOME', 'LIMITE', 'CPF']]

        # Gerar o nome do arquivo CSV no formato DROGARAIA_dd-mm-yyyy_HH-MM-SS.csv
        data_ontem = (datetime.now() - timedelta(days=1)).strftime("%d-%m-%Y_%H-%M-%S")
        nome_arquivo = f"DROGARAIA_{data_ontem}.csv"

        # Exportar para CSV com separador de ponto e vírgula
        df.to_csv(nome_arquivo, index=False, sep=';', encoding='utf-8')
        print(f"Arquivo {nome_arquivo} gerado com sucesso.")

    except Exception as e:
        print(f"Erro ao buscar dados: {e}")

if __name__ == "__main__":
    buscar_filiados_dia_anterior()
