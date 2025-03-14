import pygame
import os

pygame.init()
pygame.mixer.init()

music_folder = "music/"
playlist = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]

if not playlist:
    print("No .mp3 files in folder")
    exit()

current_track = 0
pygame.mixer.music.load(os.path.join(music_folder, playlist[current_track]))

keyPlayPause = pygame.K_SPACE
keyStop = pygame.K_s
keyNext = pygame.K_n
keyPrev = pygame.K_p

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    pygame.mixer.music.load(os.path.join(music_folder, playlist[current_track]))
    play_music()

def prev_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    pygame.mixer.music.load(os.path.join(music_folder, playlist[current_track]))
    play_music()

play_music()

running = True
paused = False

print("Press 'SPACE' to play/pause")
print("PRess 'S' to stop")
print("Press 'N' to skip current track")
print("Press 'P' to play previous track")
print("Press 'ESC' to quit")

screen = pygame.display.set_mode((900, 450))



while running:
    screen.fill((255, 255, 255))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == keyPlayPause:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                else:
                    pygame.mixer.music.unpause()
                    paused = False

            elif event.key == keyStop:
                stop_music()

            elif event.key == keyNext:
                next_track()

            elif event.key == keyPrev:
                prev_track()

            elif event.key == pygame.K_ESCAPE:
                running = False

pygame.quit()
