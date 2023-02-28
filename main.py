# Importações necessárias
import os, pickle, hashlib
import tkinter as tk
from tkinter import filedialog 

# Selecionando a pasta com o Tkinter
def seleciona_pasta (title = 'Selecione a pasta...', initialdir = '.'):
    """Seleciona a pasta com o Tkinter"""
    root=tk.Tk()
    root.withdraw() # Esconde a janela root do Tkinter
    pasta_escolhida = filedialog.askdirectory(title = title, initialdir = initialdir)
    return pasta_escolhida

# Entra com a pasta onde se encontram os arquivos dos quais serão extraídos os hashs
pasta_principal = seleciona_pasta()
print(f'Pasta escolhida: {pasta_principal}')
print('Aguarde...')

# Relaciona os arquivos da pasta e da subpasta
arquivos = os.walk(pasta_principal)

# Gera a lista de hashs para a pasta selecionada
lista_hashes = []
for dirpath, dirname, files in arquivos:
    for file in files:
        try:
            arquivo = os.path.join(dirpath, file)
            hash = hashlib.sha1(open(arquivo, 'rb').read()).hexdigest()   
            lista_hashes.append(hash) 
        except:
            print(f'Não encontrado: {dirpath}/{file}')

# Grava a lista de hashs em arquivo texto para futura comparação

with open('lista_hashes.pickle', 'wb') as arquivo:
    pickle.dump(lista_hashes, arquivo)

print(f'Arquivos lidos: {len(lista_hashes)}')
print(f'Arquivos únicos: {len(set(lista_hashes))}')
n_repetidos = len(lista_hashes) - len(set(lista_hashes))
print(f'Arquivos repetidos: {n_repetidos}')
print('Programa concluído!')