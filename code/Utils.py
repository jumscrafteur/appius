import pygame
TILE_SIZE = 60


def GenerateGridLayout(x, y, columnNumber, rowNumber, gapX, gapY, sizeX, sizeY):
    initialOffsetX = - (columnNumber - 1) * (gapX+sizeX) / 2
    initialOffsetY = - (rowNumber - 1) * (gapY+sizeY) / 2

    for c in range(columnNumber):
        for r in range(rowNumber):
            yield (x + initialOffsetX + c*(gapX+sizeX), y + initialOffsetY + r*(gapY+sizeY))


def cartCoToIsoCo(cartX, cartY):
    isoX = cartX - cartY
    isoY = (cartX + cartY)/2
    return isoX, isoY


def isoCoToCartCo(isoX, isoY):
    cartX = isoY + isoX/2
    cartY = isoY - isoX/2
    return cartX, cartY


def mouse_is_on_map(world, grid_pos, mouse_pos):
    mouse_on_panel = False
    for rect in [world.hud["up"].rect, world.hud["main"].rect, world.hud["fps"].rect, world.hud["pop"].rect]:
        if rect.collidepoint(mouse_pos):
            mouse_on_panel = True
    world_bounds = (0 <= grid_pos[0] < world.grid_lx) and (
        0 <= grid_pos[1] < world.grid_ly)
    if world_bounds and not mouse_on_panel:
        return True
    else:
        return False


def mouse_to_grid(x, y, scroll, offset):
    # remove camera scrolling & offset
    world_x = x - scroll.x - offset
    world_y = y - scroll.y
    # transform iso to cartesian
    cart_x, cart_y = isoCoToCartCo(world_x, world_y)
    # transform back to grid matrix
    grid_x = int(cart_x // TILE_SIZE)
    grid_y = int(cart_y // TILE_SIZE)
    return grid_x, grid_y


def zone_grid(drag_process, drag_start, drag_end, scroll, offset):
    if drag_process and drag_end != None and drag_start != None:
        x_start, y_start = drag_start
        x_end, y_end = drag_end
        grid_start_x, grid_start_y = mouse_to_grid(
            x_start, y_start, scroll, offset)
        grid_end_x, grid_end_y = mouse_to_grid(x_end, y_end, scroll, offset)
        print([grid_start_x, grid_start_y], [grid_end_x, grid_end_y])
        return [grid_start_x, grid_start_y], [grid_end_x, grid_end_y]


def get_points_in_rectangle(x1, y1, x2, y2):
    points = []
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            points.append((x, y))
    return points


def get_iso_polygon(iso_x, iso_y):
    return [
        (iso_x*TILE_SIZE, iso_y*TILE_SIZE),
        (iso_x*TILE_SIZE+TILE_SIZE, iso_y*TILE_SIZE),
        (iso_x*TILE_SIZE+TILE_SIZE, iso_y*TILE_SIZE+TILE_SIZE),
        (iso_x*TILE_SIZE, iso_y*TILE_SIZE+TILE_SIZE)
    ]
