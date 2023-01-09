import pygame

# Set up the Pygame window
window_size = (600, 600)
screen = pygame.display.set_mode(window_size)

# Set up the grid of squares
square_size = 50
grid_size = (12, 12)
grid = [[0 for x in range(grid_size[0])] for y in range(grid_size[1])]

# Set up the starting point and the ending point
start_point = (0, 0)
end_point = (11, 11)

# Use the A* algorithm to find the shortest path
# between the starting point and the ending point
path = find_path(grid, start_point, end_point)

# Draw the road on the screen
for i in range(len(path) - 1):
    start_pos = (path[i][0] * square_size, path[i][1] * square_size)
    end_pos = (path[i + 1][0] * square_size, path[i + 1][1] * square_size)
    pygame.draw.line(screen, (0, 0, 0), start_pos, end_pos, 5)

# Update the display
pygame.display.flip()
