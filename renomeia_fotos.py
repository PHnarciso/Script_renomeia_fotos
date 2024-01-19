import os
import csv

def renomear_arquivos(caminho_pasta, arquivo_csv):
    
    with open(arquivo_csv, 'r') as f:
        leitor_csv = csv.reader(f)
        dados_csv = list(leitor_csv)

    # Verifica se arquivo csv possui duas colunas
    if len(dados_csv[0]) < 2:
        print("Erro: O CSV deve conter pelo menos duas colunas.")
        return

    # Lista apenas arquivos com extensão .JPG na pasta
    arquivos_na_pasta = sorted([arquivo for arquivo in os.listdir(caminho_pasta) if arquivo.endswith('.JPG')])

    if len(arquivos_na_pasta) != len(dados_csv):
        print("Erro: A quantidade de arquivos na pasta não corresponde à quantidade de linhas no CSV.")
        return

    for i, nome_arquivo in enumerate(arquivos_na_pasta):
        caminho_antigo = os.path.join(caminho_pasta, nome_arquivo)
        novo_nome = dados_csv[i][1] + '.JPG'  # Usa o nome da segunda coluna no CSV

        try:
            os.rename(caminho_antigo, os.path.join(caminho_pasta, novo_nome))
            print(f"Arquivo renomeado: {nome_arquivo} -> {novo_nome}")
        except Exception as e:
            print(f"Erro ao renomear arquivo {nome_arquivo}: {e}")

# Exemplo de uso
caminho_pasta = '/'  # Substitua pelo caminho real da sua pasta
arquivo_csv = '/'  # Substitua pelo nome do seu arquivo CSV


renomear_arquivos(caminho_pasta, arquivo_csv)
