# %% [markdown]
# # Importando bibliotecas

# %%
import cv2
import numpy
import matplotlib.pyplot as plt

# %% [markdown]
# Lendo imagens usando o OpenCV

# %%
#lendo imagem na escala cinza
img_cinza = cv2.imread("./assets/imagem1.jpg", 0)
#printando a imagem
print(img_cinza)
# dimensões da imagem
print(img_cinza.shape)
# data type da imagem
print(img_cinza.dtype)


# %% [markdown]
# Mostrando a imagem através do matplotlib

# %%
plt.imshow(img_cinza)

# %% [markdown]
# A imagem é mostrada com cor pois o matplotlib possui um color map, podemos setá-lo para usar cinza.

# %%
plt.imshow(img_cinza, cmap="gray")

# %% [markdown]
# Trabalhando com cores.
# 
# Ler e mostrar uma imagem com cores

# %%
img_color = cv2.imread("./assets/imagem2.png", 1)
# dimensão da image
print(img_color.shape)
# data type da imagem
print(img_color.dtype)

# %% [markdown]
# 3 é o número de canais

# %% [markdown]
# ## Display imagem

# %%
plt.imshow(img_color)

# %% [markdown]
# Open CV utiliza um método diferente de armazenamento da informação do canal de cor. Para imagens RGB o openCV utiliza canal BGR, matplot lib espera um RGB mas recebe um BGR do openCV

# %%
img_color_com_canal_reservado = img_color[:,:,::-1]
plt.imshow(img_color_com_canal_reservado)


