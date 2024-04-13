
import pygame  # Importing pygame library

pygame.init()  # Initializing pygame

# Setting up some useful constants
WIDTH = 800
HEIGHT = 600
colorWHITE = (255, 255, 255)

# Creating the main display screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Creating a base layer for easy screen updates
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill(colorWHITE)
screen.fill(colorWHITE)
pygame.display.set_caption("Paint")

# Creating a clock object to control frame rate
clock = pygame.time.Clock()

# Boolean to track left mouse button press
LMBpressed = False
THICKNESS = 5  # Thickness of drawing lines

# Variables to track current and previous mouse positions
currX = 0
currY = 0

prevX = 0
prevY = 0

# Drawing mode (rectangle, circle, eraser)
mode = "rectangle"
color_mode = "red"  # Initial drawing color

# Function to calculate a rectangle based on mouse positions
def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

# Game loop status
done = False

# Main game loop
while not done:

    # Check for keyboard events
    pressed = pygame.key.get_pressed()
    shift_held = pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]

    for event in pygame.event.get():
        if LMBpressed:
            screen.blit(base_layer, (0, 0))  # Refresh the screen if left mouse button is pressed
        if event.type == pygame.QUIT:
            done = True  # Exit the game loop if the window is closed

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Record previous mouse position when left mouse button is pressed
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]

        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                # Update current mouse position during mouse motion
                currX = event.pos[0]
                currY = event.pos[1]

                # Draw based on the selected mode (rectangle, circle, eraser)
                if mode == "rectangle":
                    pygame.draw.rect(screen, color_mode, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                if mode == "circle":
                    pygame.draw.circle(screen, color_mode, (prevX, prevY), abs(currX - prevX), THICKNESS)
                if mode == "eraser":
                    pygame.draw.circle(screen, (255, 255, 255), (currX, currY), THICKNESS)
                    base_layer.blit(screen, (0, 0))  # Update base layer for eraser mode

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # Record current mouse position when left mouse button is released
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]

            # Draw based on the selected mode when mouse button is released
            if mode == "rectangle":
                pygame.draw.rect(screen, color_mode, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                base_layer.blit(screen, (0, 0))  # Update base layer after drawing rectangle
            if mode == "circle":
                pygame.draw.circle(screen, color_mode, (prevX, prevY), abs(currX - prevX), THICKNESS)
                base_layer.blit(screen, (0, 0))  # Update base layer after drawing circle

        if event.type == pygame.KEYDOWN:
            # Handle key press events
            if event.key == pygame.K_UP:
                THICKNESS += 1  # Increase line thickness
            if event.key == pygame.K_DOWN:
                THICKNESS -= 1  # Decrease line thickness
            if event.key == pygame.K_ESCAPE:
                done = True  # Exit the game loop on ESC key press

            # Change drawing mode based on key press (rectangle, circle, eraser)
            if event.key == pygame.K_c:
                mode = "circle"
            if event.key == pygame.K_r:
                mode = "rectangle"
            if event.key == pygame.K_e:
                mode = "eraser"

            # Change drawing color based on key press (red, blue, green, black)
            if event.key == pygame.K_r and shift_held:
                color_mode = "RED"
            if event.key == pygame.K_b and shift_held:
                color_mode = "BLUE"
            if event.key == pygame.K_g and shift_held:
                color_mode = "GREEN"
            if event.key == pygame.K_p and shift_held:
                color_mode = "BLACK"

            # Update drawing color based on the selected color mode
            if color_mode == "RED":
                color = (255, 0, 0)
            if color_mode == "BLUE":
                color = (0, 0, 255)
            if color_mode == "GREEN":
                color = (0, 255, 0)
            if color_mode == "BLACK":
                color = (255, 255, 255)

    pygame.display.flip()  # Update the display
    clock.tick(10000000)  # Cap the frame rate to avoid excessive CPU usage