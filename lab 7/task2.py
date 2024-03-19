import pygame
pygame.init()

music_files = [
    "music/21 Savage, Travis Scott, Metro Boomin – née-nah.mp3",
    "music/Travis Scott, Drake – MELTDOWN.mp3",
    "music/Travis Scott, The Weeknd – Pray 4 Love.mp3"
]

current_music_index = 0
pygame.mixer.music.load(music_files[current_music_index])
pygame.mixer.music.play()

W, H = 500, 300
sc = pygame.display.set_mode((W, H))

clock = pygame.time.Clock()
FPS = 60

flPause = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                current_music_index = (current_music_index + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_music_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_p:
                current_music_index = (current_music_index - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_music_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_SPACE:
                flPause = not flPause
                if flPause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
    pygame.display.update()

    clock.tick(FPS)
