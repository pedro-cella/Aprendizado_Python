import time
import pygame
print("====== DESAFIO 21 ======")
print("Sobre o programa: Faca um programa em Python que abra e reproduza", end='')
print(" o audio de um arquivo MP3")
pygame.init()
pygame.mixer.music.load('/home/pedro/Documentos/Eu/Future/Python/Curso_em_Video/Python3-Mundo1/Exercicios/ex021.py/musica.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)