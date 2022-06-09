# %% [markdown]
# ## Trabalho 1
# Trabalho 1 da Disciplina de Processamento Digital de Imagens
# 
# Aluno: Matheus Pereira dos Santos<br>
# RA: 1748823

# %% [markdown]
# Realizando o import das bibliotecas necessárias.

# %%
import cv2
import numpy
import matplotlib.pyplot as pyplot
from PIL import Image
from IPython.display import Image

# %% [markdown]
# Realizando a leitura da imagem, usando a biblioteca opencv, printando a imagem em forma de matriz de pixels e após em sua forma "original".

# %%
# leitura da imagem na escala cinza
imagem_teste = cv2.imread("./imagem.PNG", cv2.IMREAD_GRAYSCALE)
# usando a função print para exibir a matrix pixel equivalente na escala cinza
print(imagem_teste)
# usando o pyplot para realizar a renderização imagem
pyplot.imshow(imagem_teste, cmap='gray')

# %% [markdown]
# A) Invertendo os valores de intensidade da imagem, tal qual 255 passa a ser 0, 254 passa a ser 1, assim por diante.

# %%
matriz_de_saida = [] # inciando a matriz de saída
# a matriz de entrada será a matri de pixel resultante da leitura da imagem
matriz_de_entrada = imagem_teste
# criando a função que irá realizar o calculo
def inversa(value):
    return 255 - value

for linha in matriz_de_entrada:
    linha_com_inversa = []
    for elemento in linha:
        linha_com_inversa.append(inversa(elemento))
    matriz_de_saida.append(linha_com_inversa)
    linha_com_inversa = []
    

# imprimindo a matriz pixel de saída com print
# print("matriz de entrada >>>\n")
# print(matriz_de_entrada)

# print("matriz de saída >>>\n")
# print(matriz_de_saida)
#Prints escondidos por poluirem muito o documento

# comparando as duas imagens, de entrada e a de saída após o calculo
pyplot.figure(figsize=[20,5])
pyplot.subplot(141); pyplot.imshow(matriz_de_entrada, cmap='gray');pyplot.title("Imagem de Entrada");
pyplot.subplot(142); pyplot.imshow(matriz_de_saida, cmap='gray');pyplot.title("Imagem de Saída");

# %% [markdown]
# B) Os Valores de intensidade da imagem presentes nas colunas pares são trocados com os valores de intensidade das colunas ímpares.

# %%
# primeiro definimos a função que faz essa troca de valores
def troca_par_impar(matriz):
    nova_matriz = []
    for linha in matriz:
        nova_linha = numpy.zeros(len(linha))
        for i in range(len(linha)):
            if i % 2 == 0 and i in range(len(linha)):
                nova_linha[i] = linha[i+1]
                nova_linha[i+1] = linha[i]
        nova_matriz.append(nova_linha)
    return nova_matriz

matriz_saida = troca_par_impar(matriz_de_entrada)
pyplot.figure(figsize=[50,25])
pyplot.subplot(141); pyplot.imshow(matriz_de_entrada, cmap='gray'); pyplot.title('Imagem de entrada');
pyplot.subplot(142); pyplot.imshow(matriz_saida, cmap='gray'); pyplot.title('Imagem de saída');


# %%
# primeiro definimos a função que irá trocar as linhas
def troca_linhas(matriz_original):
    linhas_impares= matriz_original[::2,:]
    linhas_pares = matriz_original[1::2,:]
    
    novo = [0] * (len(linhas_pares)+len(linhas_impares))
    print(len(linhas_impares))
    print(len(linhas_pares))
    
    i = 0
    while i < len(novo):
        if(i % 2 == 0):
            novo[i] = linhas_impares[i]
            novo[i+1] = linhas_pares[i]
        i+=1
    return novo

    # return [linhas_pares, linhas_impares]

# chamando a função que muda as linhas pares e impares
matriz_saida = troca_linhas(matriz_de_entrada)
# [par, impar] = troca_linhas(matriz_de_entrada)
pyplot.figure(figsize=[40,20])
pyplot.subplot(141); pyplot.imshow(matriz_de_entrada, cmap='gray'); pyplot.title('Imagem de entrada')
pyplot.subplot(142); pyplot.imshow(matriz_saida, cmap='gray'); pyplot.title('Imagem de saida')
# pyplot.subplot(142); pyplot.imshow(par, cmap='gray'); pyplot.title('Imagem de saida')
# pyplot.subplot(143); pyplot.imshow(impar, cmap='gray'); pyplot.title('Imagem de saida')
            

# %% [markdown]
# C) os valores de intensidade da imagem presentes nas linhas pares são trocados com os valores de
# intensidade das linhas ímpares


