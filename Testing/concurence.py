import pygame

# Initialize Pygame
pygame.init()

# Set up the Pygame window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Mouse Selection and Blit")

# Load an image to be used for selection
selection_image = pygame.image.load("Testing/europe.png")

# Set up variables to keep track of the selection
selection_rect = None
selection_start = None

# Run the event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Check for mouse button down events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Start a new selection
            selection_start = event.pos
        # Check for mouse button up events
        elif event.type == pygame.MOUSEBUTTONUP:
            # End the current selection
            selection_rect = pygame.Rect(selection_start, event.pos)
            # Blit the selection image to the screen
            screen.blit(selection_image, selection_rect)

    # Get the current mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Check if the mouse button is being held down
    mouse_down = pygame.mouse.get_pressed()[0]
    if mouse_down:
        # Update the selection rect
        selection_rect = pygame.Rect(selection_start, (mouse_x, mouse_y))

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the selection rect, if it exists
    if selection_rect is not None:
        pygame.draw.rect(screen, (0, 0, 0), selection_rect, 2)

    # Update the display
    pygame.display.flip()
