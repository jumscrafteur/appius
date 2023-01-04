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


def can_place_tile(world, grid_pos, mouse_pos):
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


def mouse_to_grid(x, y, scroll):
    # remove camera scrolling & offset
    world_x = x - scroll.x
    world_y = y - scroll.y
    # transform iso to cartesian
    cart_x, cart_y = isoCoToCartCo(world_x, world_y)
    # transform back to grid matrix
    grid_x = int(cart_x // TILE_SIZE)
    grid_y = int(cart_y // TILE_SIZE)
    return grid_x, grid_y


def get_iso_polygon(iso_x, iso_y):
    return [
        (iso_x*TILE_SIZE, iso_y*TILE_SIZE),
        (iso_x*TILE_SIZE+TILE_SIZE, iso_y*TILE_SIZE),
        (iso_x*TILE_SIZE+TILE_SIZE, iso_y*TILE_SIZE+TILE_SIZE),
        (iso_x*TILE_SIZE, iso_y*TILE_SIZE+TILE_SIZE)
    ]
