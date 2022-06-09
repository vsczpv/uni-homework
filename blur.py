#suavização

#
# Suavização se trata sobre um eufemismo da real operação ocorrendo aqui, o "Blur".
#
# Efeito Blur é borrar a imagem, existem vários métodos de borrar uma imagem.
#

import cv2
import numpy as np

# Abrir a imagem de teste

img_in = cv2.imread('cheems.png',0)

# ::Box Blur::
#
# O box blur trabalha envolta da média de pixels
# Para cada pixel, crie uma matriz NxN com N sendo natural ímpar, com o pixel
# sendo o elemento central, e coloque todos os pixel vizinhos nas posições à
# volta. Então, calcule a somatória dessa matriz e substitua o pixel original
# pela média da somatória. Note que para próximos pixels não se deve usar os
# valores já substituidos, porém os originais.
#
# Aqui é implementado usando a função cv2.filter2D(), que aplica um "kernel",
# uma matriz que delimita os pesos da somatóra, com o kernel é criado pela função
# np.ones(), que cria um kernel 5x5, contendo o numero 1 em todas as casas.
#
# https://en.wikipedia.org/wiki/Box_blur

kernel = np.ones((5,5),np.float32)/25
img_out_1 = cv2.filter2D(img_in,-1,kernel)

# cv2.blur() aparenta ser uma função que implementa o blur anterior
#
# https://www.geeksforgeeks.org/python-opencv-cv2-blur-method/

img_out_2 = cv2.blur(img_in,(5,5))

# ::Blur Gaussiano::
#
# Similar ao Box Blur, porém a matriz de peso (kernel), invéz de ser populada
# completamente pelo numero 1, é calculada atravez da função de Gauss.
#
# Não entendi bulhufas, vá interrogar meu professor de Álgebra se quiser uma
# resposta mais substancial.
#
# https://en.wikipedia.org/wiki/Gaussian_blur

img_out_3 = cv2.GaussianBlur(img_in,(5,5),0)

# ::Blur Mediano::
#
# O Blur Mediano usa do conceito de um mediano, o "valor do meio".
#
# Tenha um dataset 1D, uma array = {5, 2, 7, 8, 3, 5, 9}
# Primeiro, rearreange ela para ficar em ordem crescente
# {5, 2, 7, 8, 3, 5, 9} -> {2, 3, 5, 5, 7, 8, 9}
# Então, pegue o valor do meio.      ↑
# O Mediano é 5.
#
# Para uma array par, pegue os dois valores do meio e calcule a média:
# {2, 3, 7, 12} -> (3 + 7) / 2 = 5
#
# Aplique este conceito à uma matriz 2D, e use como um filtro de blur.
#
# https://en.wikipedia.org/wiki/Median_filter
# https://en.wikipedia.org/wiki/Median

img_out_4 = cv2.medianBlur(img_in,5)

# Mostrar as imagens

cv2.imshow('in', img_in)
cv2.imshow('out1', img_out_1)
cv2.imshow('out2', img_out_2)
cv2.imshow('out3', img_out_3)
cv2.imshow('out4', img_out_4)
cv2.waitKey(0)

'''
cv2_imshow(img_in)
cv2_imshow(img_out_1)
cv2_imshow(img_out_2)
cv2_imshow(img_out_3)
cv2_imshow(img_out_4)
'''
