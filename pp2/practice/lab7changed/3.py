import pygame 
pygame.init()


clock = pygame.time.Clock()

w,h = 600,600
screen = pygame.display.set_mode((w,h))

x = w/2
y = h/2

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    keys = pygame.key.get_pressed()
    

    if keys[pygame.K_RIGHT]: 
        if x > w-25:
            x = x
        else: x += 1

    if keys[pygame.K_LEFT]:
        if x < 25:
            x = x 
        else : x -= 1

    if keys[pygame.K_DOWN]:
        if y > h-25:
            y = y 
        else : y += 1
    if keys[pygame.K_UP]:
        if y < 25:
            y = y 
        else : y -= 1



    screen.fill((250, 250, 250))

    #obj = pygame.draw.circle(screen, (250, 40, 100), (x,y), 25 )
    obj = pygame.draw.circle(screen, (250, 0, 0), (x,y), 25 )
    pygame.display.flip()
    clock.tick(1000)