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
        # print([grid_start_x, grid_start_y], [grid_end_x, grid_end_y])
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

# 1 North #2 South #3 West #4 East


def get_nearby_tile(grid, direction):
    x, y = grid
    match direction:
        case "north":
            return x, y-1
        case "south":
            return x, y+1
        case "west":
            return x-1, y
        case "east":
            return x+1, y


def get_surrounding_coordinate(grid):
    grid_n = get_nearby_tile(grid, "north")
    grid_s = get_nearby_tile(grid, "south")
    grid_w = get_nearby_tile(grid, "west")
    grid_e = get_nearby_tile(grid, "east")

    return {"north": grid_n, "south": grid_s, "west": grid_w, "east": grid_e}


def set_neighborhood_likeliness(tile, world_grid):
    print("changement being called")
    print(f"this.grid{tile.grid}")
    nearby = get_surrounding_coordinate(tile.grid)
    # print(
    #     f"neaby :: N :{nearby['north']}, S:{nearby['south']}, W:{nearby['west']}, E:{nearby['east']}")
    cord_north = nearby["north"]
    cord_south = nearby["south"]
    cord_west = nearby["west"]
    cord_east = nearby["east"]
    # north
    # print(f"type :: N:{world_grid[cord_north[0]][cord_north[1]]}, S:{world_grid[cord_south[0]][cord_south[1]]},\
    #                 W:{world_grid[cord_west[0]][cord_west[1]]},E:{world_grid[cord_east[0]][cord_east[1]]}")
    if 0 <= cord_north[0] <= 39 and 0 <= cord_north[1] <= 39:
        if type(tile) == type(world_grid[cord_north[0]][cord_north[1]]):
            tile.north = True
        elif type(tile) != type(world_grid[cord_north[0]][cord_north[1]]):
            tile.north = False
    elif cord_north[1] < 0:
        tile.north = True
        # south
    if 0 <= cord_south[0] <= 39 and 0 <= cord_south[1] <= 39:
        if type(tile) == type(world_grid[cord_south[0]][cord_south[1]]):
            tile.south = True
        elif type(tile) != type(world_grid[cord_south[0]][cord_south[1]]):
            tile.south = False
    elif cord_south[1] > 39:
        tile.south = True
    # west
    if 0 <= cord_west[0] <= 39 and 0 <= cord_west[1] <= 39:
        if type(tile) == type(world_grid[cord_west[0]][cord_west[1]]):
            tile.west = True
        elif type(tile) != type(world_grid[cord_west[0]][cord_west[1]]):
            tile.west = False
    elif cord_west[0] < 0:
        tile.west = True
    # east
    if 0 <= cord_east[0] <= 39 and 0 <= cord_east[1] <= 39:
        if type(tile) == type(world_grid[cord_east[0]][cord_east[1]]):
            tile.east = True
        elif type(tile) != type(world_grid[cord_east[0]][cord_east[1]]):
            tile.east = False
    elif cord_east[0] > 39:
        tile.east = True

    # print(
    #     f"after change n{tile.north},s{tile.south},w{tile.west},e{tile.east}")


def road_shifting_util(road):
    n = road.north
    s = road.south
    w = road.west
    e = road.east

    # defaut

    if n and s and w and e:
        return "ALL"
    elif n and not s and not w and not e:
        return "S"
    elif not n and s and not w and not e:
        return "N"
    elif not n and not s and w and not e:
        return "E"
    elif not n and not s and not w and e:
        return "W"
    elif n and s and not w and not e:
        return "S-N"
    elif not n and not s and w and e:
        return "W-E"
    elif n and not s and not w and e:
        return "N&E"
    elif not n and s and not w and e:
        return "S&E"
    elif not n and s and w and not e:
        return "W&S"
    elif n and not s and w and not e:
        return "W&N"
    elif n and s and not w and e:
        return "N_S_E"
    elif n and s and w and not e:
        return "N_W_S"
    elif n and not s and w and e:
        return "W_N_E"
    elif not n and s and w and e:
        return "W_S_E"
    elif not n and not s and not w and not e:
        print("S default")
        return "S"


def get_iso_polygon(iso_x, iso_y):
    return [
        (iso_x*TILE_SIZE, iso_y*TILE_SIZE),
        (iso_x*TILE_SIZE+TILE_SIZE, iso_y*TILE_SIZE),
        (iso_x*TILE_SIZE+TILE_SIZE, iso_y*TILE_SIZE+TILE_SIZE),
        (iso_x*TILE_SIZE, iso_y*TILE_SIZE+TILE_SIZE)
    ]


def get_ratio(big, small):
    return small/big
