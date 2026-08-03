#faca um prog em python que abra e reproduza o audio de um arquivo mp3

# Som
import pygame
pygame.init()
pygame.mixer.music.load('jjk.mp3')
pygame.mixer.music.play()
pygame.event.wait()
