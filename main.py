# Importações necessárias
import os, pickle, hashlib
import tkinter as tk
from tkinter import filedialog 

# Seleciona a pasta de pesquisa com o Tkinter
def seleciona_pasta (title = 'Selecione a pasta...', initialdir = '.'):
    """Seleciona a pasta com o Tkinter"""
    root=tk.Tk()
    root.withdraw() # Esconde a janela root do Tkinter
    pasta_escolhida = filedialog.askdirectory(title = title, initialdir = initialdir)
    return pasta_escolhida

pasta_principal = seleciona_pasta()
print(f'Pasta escolhida: {pasta_principal}')
print('Aguarde...')

# Relaciona os arquivos da pasta e da subpasta com os.walk()
arquivos = os.walk(pasta_principal)

# Gera a lista de hashes para a pasta selecionada
lista_hashes = []
for dirpath, dirname, files in arquivos:
    for file in files:
        try:
            arquivo = os.path.join(dirpath, file)
            hash = hashlib.sha1(open(arquivo, 'rb').read()).hexdigest()   
            lista_hashes.append(hash) 
        except:
            print(f'Não encontrado: {dirpath}/{file}')

# Grava a lista de hashes em arquivo pickle
with open('lista_hashes.pickle', 'wb') as arquivo:
    pickle.dump(lista_hashes, arquivo)

# Calcula a quantidade de arquivos repetidos
n_repetidos = len(lista_hashes) - len(set(lista_hashes))

print(f'\nArquivos lidos: {len(lista_hashes)}')
print(f'Arquivos únicos: {len(set(lista_hashes))}')
print(f'Arquivos repetidos: {n_repetidos}\n')
print('Programa concluído!')