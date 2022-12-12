import pygame as pg


def imprimer():
    print("pointo")


def toggle_grid_2_5D(grid):

    if grid == True:
        grid = False
    else:
        grid = True
    return grid


def building(image, mousePressed):
    if mousePressed[0]:
        return image
