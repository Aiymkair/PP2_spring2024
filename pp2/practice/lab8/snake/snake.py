import pygame 
import random 

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0 , 0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

snake_pos = [100,50]
snake_body = [[100,50], [90, 50], [80.50]]
food_pos = [random.randrange(1,(SCREEN_WIDTH//10))*10, random.randrange(1,(SCREEN_HEIGHT//10))*10]
food_spawn = True 

up = 0
down = 2
left = 2
right = 3
dir = right

score = 0 
level = 1
speed = 20

game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dir != down:
                dir = up
            elif event.key == pygame.K_DOWN and dir != up:
                dir = down
            elif event.key == pygame.K_LEFT and dir != right:
                dir = left
            elif event.key == pygame.K_RIGHT and dir != left:
                dir = right

    if dir == up:
        snake_pos[1] -= 10
    elif dir == down:
        snake_pos[1] += 10
    elif dir == left:
        snake_pos[0] -= 10
    elif dir == right:
        snake_pos[0] += 10

    if snake_pos[0] < 0 or snake_pos[0] > SCREEN_WIDTH - 10 or snake_pos[1] < 0 or snake_pos[1] > SCREEN_HEIGHT - 10:
        game_over = True

    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(
            1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
        food_spawn = True

    snake_body.insert(0, list(snake_pos))

    screen.fill(black)

    for pos in snake_body:
        pygame.draw.rect(screen, white, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, red, pygame.Rect(
        food_pos[0], food_pos[1], 10, 10))

    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(score) +
                       "   Level: " + str(level), True, white)
    screen.blit(text, (10, 10))

    pygame.display.update()

    if score > level * 3:
        level += 1
        speed += 5

    clock.tick(speed)

pygame.quit()