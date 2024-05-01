import pygame


pygame.init()
i = 0
songs = ["song1.mp3",
         "song2.mp3",
         "song3.mp3"]
pygame.mixer.music.load(songs[i])
pygame.mixer.music.play(0)

screen = pygame.display.set_mode((200, 120))
pygame.display.set_caption("Music Player")
gameon = True
print(len(songs))
while gameon:

    screen.fill((255, 255, 255))
    f = pygame.font.Font(None, 20)
    text1 = f.render('PAUSEE - Space', True, (0, 0, 0))
    screen.blit(text1, (10, 30))

    text2 = f.render('Next - arrow to right', True, (0, 0, 0))
    screen.blit(text2, (10, 60))

    text3 = f.render('Previous - arrow to left', True, (0, 0, 0))
    screen.blit(text3, (10, 90))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # pause on space
                pygame.mixer.music.pause()
            if event.key == pygame.K_u:  # unpause
                pygame.mixer.music.unpause()
            if event.key == pygame.K_RIGHT:  # next
                if i < len(songs)-1:
                    i += 1
                    pygame.mixer.music.load(songs[i])
                    pygame.mixer.music.play(0)
            if event.key == pygame.K_LEFT:  # prev
                if i > 0:
                    i -= 1
                    pygame.mixer.music.load(songs[i])
                    pygame.mixer.music.play(0)
        if event.type == pygame.QUIT:
            gameon = False
    pygame.display.flip()