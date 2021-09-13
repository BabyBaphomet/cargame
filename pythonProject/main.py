import pygame, random, time, sys
from pygame import mixer
from pygame.locals import *
from random import randrange
pygame.init()
mixer.init()
mainClock = pygame.time.Clock()
win = pygame.display.set_mode((500, 700))
pygame.display.set_caption("Drivers ed")
fontg = pygame.font.SysFont(None, 40)
fontm = pygame.font.SysFont(None, 20)
def draw_text(text, font, color, win, x, y):
    textobj = font.render(text, 1 , color)
    textrect = font.render(text, 1, color)
    textrect = (x, y)
    win.blit(textobj, textrect)

def menu():

    click = False
    run = True

    while run:
        win.fill((255, 255, 255))
        mx, my = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        button_play = pygame.Rect(150, 150, 180, 35)
        button_settings = pygame.Rect(150, 200 , 180, 35)
        button_about = pygame.Rect(150, 250 , 180, 35)
        button_quit = pygame.Rect(150, 300 , 180, 35)
        if button_play.collidepoint((mx,my )):
            if click == True:
               game()
        if button_settings.collidepoint((mx,my )):
            if click == True:
               settings()
        if button_about.collidepoint((mx,my )):
            if click == True:
               about()
        if button_quit.collidepoint((mx,my )):
            if click == True:
               pygame.quit()
               sys.exit()
        pygame.draw.rect(win, (255, 245, 215),button_play)
        pygame.draw.rect(win, (255, 245, 215),button_settings)
        pygame.draw.rect(win, (255, 245, 215),button_about)
        pygame.draw.rect(win, (255, 245, 215),button_quit)
        draw_text('Play', fontg, (0,0,0), win,213,153)
        draw_text('Settings', fontg, (0,0,0), win,189,204)
        draw_text('About', fontg, (0,0,0), win,200,255)
        draw_text('Quit', fontg, (0,0,0), win,213,303)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()




        pygame.display.update()
        mainClock.tick(60)

def game():
    mixer.music.load("song.mp3")
    mixer.music.set_volume(0.1)
    mixer.music.play()
    x = 225
    z = 1
    y = 350
    enemy = pygame.transform.scale2x(pygame.image.load('cone.png'))
    newcar = pygame.transform.scale2x(pygame.image.load('car.png'))
    enemyxpos = randrange(500)
    enemyypos = 0
    enemyspeed = 10
    roadspeed = 10
    traveled = 0
    road1 = 0
    road2 = 100 + 60
    road3 = 200 + 60
    def enemyaddatloc(x, y):
        win.blit(enemy, (x, y))



   #player
    miles = 0
    width = 20
    height = 50
    vel = 10
    score = 0
    particles = []
    run = True
    while run:
        miles += 1



        if road1 >= 700:
            road1 = 0
        if road2 >= 700:
            road2 = 0
        if road3 >= 700:
            road3 = 0

        enemyypos += enemyspeed
        if enemyypos >= 700:
            enemyypos = 0
            enemyxpos = randrange(500)
        # input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and x > -5:
            x -= vel

        if keys[pygame.K_d] and x < 425:
            x += vel
        # car is the car hitbox just making it here
        car1 = pygame.Rect(x+8, y, 64, 120)
        carhitbox = pygame.draw.rect(win, (255, 0, 0), car1)
        #this is the hitbox for the cone                    x   y   sizex  sizey
        conehitbox = pygame.draw.rect(win, (255, 245, 215), pygame.Rect(enemyxpos + 10, enemyypos + 3, 45, 74))
        win.fill((68,68,71))
        pygame.draw.rect(win, (255, 245, 215), pygame.Rect(250, road1 , 20, 60))
        pygame.draw.rect(win, (255, 245, 215), pygame.Rect(250, road2 , 20, 60))
        pygame.draw.rect(win, (255, 245, 215), pygame.Rect(250, road3 , 20, 60))
        if carhitbox.colliderect((conehitbox)):
            score += 1
            enemyypos = 0
            enemyxpos = randrange(500)


    #particles
        particles.append([[x + 23, y + 115], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])

        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            particle[1][1] += 1
            pygame.draw.circle(win, (211, 211, 211), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                particles.remove(particle)

        if score == 3:
            youlose()
        #drawing stuff
        road1 += roadspeed
        road2 += roadspeed
        road3 += roadspeed
        win.blit(newcar, (x, y))
        draw_text('Points: ' + str(score), fontg, (255, 0, 0), win, 40, 650)
        draw_text('meters: ' + str(miles), fontg, (255, 0, 0), win, 48,591)
        enemyaddatloc(enemyxpos, enemyypos)
        # X IS LEFT AND RIGHT
        pygame.display.update()
        mainClock.tick(60)

def youlose():
    click = False
    run = True
    pygame.mixer.music.stop()
    mixer.music.load("crash.wav")
    mixer.music.set_volume(0.1)
    mixer.music.play()
    while run:
        win.fill((255, 255, 255))
        draw_text('You failed your drivers ed test', fontg, (0,0,0), win,50,80)
        draw_text('but you made it ' + miles2 , fontg, (0,0,0), win,50,80)
        mx, my = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        button_menu = pygame.Rect(150, 150, 180, 35)
        button_play = pygame.Rect(150, 200, 180, 35)

        if button_menu.collidepoint((mx,my )):
            if click == True:
               menu()
        if button_play.collidepoint((mx,my )):
            if click == True:
               game()
        pygame.draw.rect(win, (255, 245, 215),button_menu)
        pygame.draw.rect(win, (255, 245, 215),button_play)
        draw_text('Menu', fontg, (0,0,0), win,200,153)
        draw_text('Play Again', fontg, (0,0,0), win,172,205)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)

def settings():
    click = False
    run = True

    while run:
        win.fill((255, 255, 255))
        draw_text('settings', fontg, (0,0,0), win,50,80)
        mx, my = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        button_gamer = pygame.Rect(16,653, 180, 35)
        button_menu = pygame.Rect(150, 150, 180, 35)
        button_play = pygame.Rect(150, 200, 180, 35)

        if button_menu.collidepoint((mx,my )):
            if click == True:
               pass
        if button_play.collidepoint((mx,my )):
            if click == True:
               pass
        if button_gamer.collidepoint((mx,my )):
            if click == True:
               menu()
        pygame.draw.rect(win, (255, 245, 215),button_gamer)

        draw_text('Back', fontg, (0,0,0), win,70,657)
        pygame.draw.rect(win, (255, 245, 215),button_menu)
        pygame.draw.rect(win, (255, 245, 215),button_play)
        draw_text('Left', fontg, (0,0,0), win,200,153)
        draw_text('Right', fontg, (0,0,0), win,172,205)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)



    pygame.display.update()
    mainClock.tick(60)

def about():
    click = False
    run = True

    while run:
        win.fill((255, 255, 255))
        draw_text('about', fontg, (0,0,0), win,50,80)
        mx, my = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        button_menu = pygame.Rect(150, 150, 180, 35)
        button_gamer = pygame.Rect(16,653, 180, 35)

        if button_gamer.collidepoint((mx,my )):
            if click == True:
               menu()
        pygame.draw.rect(win, (255, 245, 215),button_gamer)

        draw_text('Back', fontg, (0,0,0), win,70,657)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)


menu()


