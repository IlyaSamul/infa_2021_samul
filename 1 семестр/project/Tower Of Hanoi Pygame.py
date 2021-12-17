import pygame, sys, time
from pygame import mixer
from pygame.locals import*

pygame.init()
mixer.init()
pygame.display.set_caption("Towers of Hanoi")
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

game_done = False
framerate = 60

def music(name):
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()

steps = 0
n_disks = 3
disks = []
towers_midx = [120, 320, 520]
pointing_at = 0
floating = False
floater = 0
g_mode = 0

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
gold = (239, 229, 51)
blue = (78,162,196) 
grey = (170, 170, 170)
green = (77, 206, 145)
img = pygame.image.load('1.bmp')

global frm
to = [[],"2"]
aux = [[],"1"]
moveText = ""

def blit_text(screen, text, midtop, aa=True, font=None, font_name = None, size = None, color=(255,0,0)):
    if font is None:
        font = pygame.font.SysFont(font_name, size)
    font_surface = font.render(text, aa, color)
    font_rect = font_surface.get_rect()
    font_rect.midtop = midtop
    screen.blit(font_surface, font_rect)

def choosing_screen():
    global screen, n_disks, game_done
    menu_done = False
    while not menu_done:
        screen.fill(white)
        blit_text(screen, 'Ханойская башня', (323,122), font_name='sans serif', size=90, color=grey)
        blit_text(screen, 'Ханойская башня', (320,120), font_name='sans serif', size=90, color=gold)
        blit_text(screen, 'Используйте стрелки, чтобы выбрать сложность:', (320, 220), font_name='sans serif', size=30, color=black)
        blit_text(screen, str(n_disks), (320, 260), font_name='sans serif', size=40, color=blue)
        blit_text(screen, 'Нажмите ENTER, чтобы продолжить', (320, 320), font_name='sans_serif', size=30, color=black)
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    menu_done = True
                    game_done = True
                if event.key == pygame.K_RETURN:
                    menu_done = True
                if event.key in [pygame.K_RIGHT, pygame.K_UP]:
                    n_disks += 1
                    if n_disks > 9:
                        n_disks = 9
                if event.key in [pygame.K_LEFT, pygame.K_DOWN]:
                    n_disks -= 1
                    if n_disks < 1:
                        n_disks = 1
            if event.type == pygame.QUIT:
                menu_done = True
                game_done = True
        pygame.display.flip()
        clock.tick(60)

def menu_screen():
    global screen, n_disks, game_done, g_mode
    menu_done = False
    while not menu_done:
        screen.fill(white)
        blit_text(screen, 'Ханойская башна', (323,122), font_name='sans serif', size=90, color=grey)
        blit_text(screen, 'Ханойская башня', (320,120), font_name='sans serif', size=90, color=gold)
        
        blit_text(screen, 'Нажмите ', (212,205), font_name='sans serif', size=30, color=black)
        blit_text(screen, '1', (263,202), font_name='sans serif', size=35, color=blue)
        blit_text(screen, 'для авто-игры', (345,205), font_name='sans serif', size=30, color=black)

        blit_text(screen, 'Нажмите ', (212,255), font_name='sans serif', size=30, color=black)
        blit_text(screen, '2', (263,252), font_name='sans serif', size=35, color=blue)
        blit_text(screen, 'для игры', (320,255), font_name='sans serif', size=30, color=black)


    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    g_mode = 1
                    choosing_screen = True
                    menu_done = True

                if event.key == pygame.K_2:
                    g_mode = 2
                    choosing_screen = True
                    menu_done = True
                    
                
        pygame.display.flip()
        clock.tick(60)

def game_over():
    global screen, steps
    screen.fill(white)
    screen.blit(img,(0,0))
    min_steps = 2**n_disks-1
    blit_text(screen, 'Готово!', (320, 200), font_name='sans serif', size=72, color=gold)
    blit_text(screen, 'Готово!', (322, 202), font_name='sans serif', size=72, color=gold)
    blit_text(screen, 'Количество шагов: '+str(steps), (320, 360), font_name='mono', size=30, color=black)
    blit_text(screen, 'Минимальное количество шагов: '+str(min_steps), (320, 390), font_name='mono', size=30, color=red)
    if min_steps==steps:
        blit_text(screen, 'Вы сделали минимальное количество шагов!', (320, 300), font_name='mono', size=26, color=green)
    pygame.display.flip()
    time.sleep(4)
    reset(); 

def draw_towers():
    global screen
    for xpos in range(40, 460+1, 200):
        pygame.draw.rect(screen, green, pygame.Rect(xpos, 400, 160 , 20))
        pygame.draw.rect(screen, grey, pygame.Rect(xpos+75, 200, 10, 200))
    blit_text(screen, 'Старт', (towers_midx[0], 403), font_name='mono', size=14, color=black)
    blit_text(screen, 'Финиш', (towers_midx[2], 403), font_name='mono', size=14, color=black)

def make_disks():
    global n_disks, disks
    disks = []
    height = 20
    ypos = 397 - height
    mod23 = 0
    if (n_disks <= 6):
        mod23 = 23 + (6-n_disks) * 10
        width = n_disks * mod23 
    else:
        mod23 = 23 - (n_disks - 6) * 3
        width = n_disks * mod23
    for i in range(n_disks):
        disk = {}
        disk['rect'] = pygame.Rect(0, 0, width, height)
        disk['rect'].midtop = (120, ypos)
        disk['val'] = n_disks-i
        disk['tower'] = 0
        disks.append(disk)
        ypos -= height+3
        width -= mod23


def draw_disks():
    global screen, disks
    for disk in disks:
        pygame.draw.rect(screen, blue, disk['rect'])
        blit_text(screen, str(disk['val']), disk['rect'].midtop, font_name='mono', size=14, color=black)
    return

def move_right():
    global pointing_at,floating,floater,disks,towers_midx

    pointing_at = (pointing_at+1)%3
    if floating:
        disks[floater]['rect'].midtop = (towers_midx[pointing_at], 100)
        disks[floater]['tower'] = pointing_at

def move_left():
    global pointing_at,floating,floater,disks,towers_midx

    pointing_at = (pointing_at-1)%3
    if floating:
        disks[floater]['rect'].midtop = (towers_midx[pointing_at], 100)
        disks[floater]['tower'] = pointing_at

def move_up():
    global pointing_at,floating,floater,disks,towers_midx
    
    for disk in disks[::-1]:
        if disk['tower'] == pointing_at:
            floating = True
            floater = disks.index(disk)
            disk['rect'].midtop = (towers_midx[pointing_at], 100)
            break

def move_down():
    global pointing_at,floating,floater,disks,towers_midx,steps
    
    for disk in disks[::-1]:
        if disk['tower'] == pointing_at and disks.index(disk)!=floater:
            if disk['val']>disks[floater]['val']:
                floating = False
                disks[floater]['rect'].midtop = (towers_midx[pointing_at], disk['rect'].top-23)
                steps += 1
            break
    else: 
        floating = False
        disks[floater]['rect'].midtop = (towers_midx[pointing_at], 400-23)
        steps += 1


def draw_ptr():
    ptr_points = [(towers_midx[pointing_at]-7 ,440), (towers_midx[pointing_at]+7, 440), (towers_midx[pointing_at], 433)]
    pygame.draw.polygon(screen, red, ptr_points)
    return

def check_won():
    global disks
    over = True
    for disk in disks:
        if disk['tower'] != 2:
            over = False
    if over:
        time.sleep(0.2)
        game_over()

def reset():
    global steps,pointing_at,floating,floater,frm,disks,g_mode,to,aux,moveText
    pygame.mixer.music.stop()
    steps = 0
    disks = []
    pointing_at = 0
    floating = False
    floater = 0
    g_mode = 0
    frm = [list(range(n_disks,0,-1)),"0"]
    to = [[],"2"]
    aux = [[],"1"]
    moveText = ""
    
    menu_screen()
    if(g_mode == 1):
        choosing_screen()
        make_disks()
        frm = [list(range(n_disks,0,-1)),"0"]
        music("mus1.mp3")
        autoplay()
    if(g_mode == 2):
        choosing_screen()
        make_disks()
        music("mus2.mp3")


def hanoiAuto(n,frmT,auxT,toT):
    global moveText
    if n==0:
        return
    hanoiAuto(n-1,frmT,toT,auxT)
    toT[0].append(frmT[0].pop())
    moveText = "Передвижение диска " + str(n) + " от башни " + frmT[1] + " к башне " + toT[1]
    movedisk(frmT,auxT,toT)
    hanoiAuto(n-1,auxT,frmT,toT)

def movedisk(frm,aux,to):
    if((int(frm[1]) - pointing_at) != 0 and not floating): adjustPtr(frm)
    move_up()
    refreshAutoMode()
    if ((abs(int(frm[1]) - int(to[1])))!= 0): move_left_right(frm,to)
    move_down()
    refreshAutoMode()

def adjustPtr(fromTower):
    if((int(fromTower[1]) - pointing_at) > 0 ):
        for i in range(int(fromTower[1]) - pointing_at):
            move_right()
    else:
        for i in range(abs(int(fromTower[1]) - pointing_at)):
            move_left()
    refreshAutoMode()

def move_left_right(fromTower,ToTower):
    for i in range(abs(int(fromTower[1]) - int(ToTower[1]))):
        if (fromTower[1] < ToTower[1] and floating):
            move_right()
        if (fromTower[1] > ToTower[1] and floating):
            move_left()
        refreshAutoMode()    

def autoplay():
    hanoiAuto(n_disks,frm,aux,to)

def refreshAutoMode():
    screen.fill(white)
    draw_towers()
    draw_disks()
    draw_ptr()
    time.sleep(0.4)
    blit_text(screen, 'Шаги: '+str(steps), (320, 20), font_name='mono', size=30, color=black)
    pygame.display.flip()
    clock.tick(framerate)

menu_screen()
if(g_mode == 1):
    choosing_screen()
    screen.blit(img,(0,0))
    make_disks()
    frm = [list(range(n_disks,0,-1)),"0"]
    music("mus1.mp3")
    autoplay()
if(g_mode == 2):
    choosing_screen()
    make_disks()
    music("mus2.mp3")

while not game_done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                reset()
            if event.key == pygame.K_RIGHT and g_mode == 2:
                pointing_at = (pointing_at+1)%3
                if floating:
                    disks[floater]['rect'].midtop = (towers_midx[pointing_at], 100)
                    disks[floater]['tower'] = pointing_at
            if event.key == pygame.K_LEFT and g_mode == 2:
                pointing_at = (pointing_at-1)%3
                if floating:
                    disks[floater]['rect'].midtop = (towers_midx[pointing_at], 100)
                    disks[floater]['tower'] = pointing_at
            if event.key == pygame.K_UP and not floating and g_mode == 2:
                for disk in disks[::-1]:
                    if disk['tower'] == pointing_at:
                        floating = True
                        floater = disks.index(disk)
                        disk['rect'].midtop = (towers_midx[pointing_at], 100)
                        break
            if event.key == pygame.K_DOWN and floating and g_mode == 2:
                for disk in disks[::-1]:
                    if disk['tower'] == pointing_at and disks.index(disk)!=floater:
                        if disk['val']>disks[floater]['val']:
                            floating = False
                            disks[floater]['rect'].midtop = (towers_midx[pointing_at], disk['rect'].top-23)
                            steps += 1
                        break
                else: 
                    floating = False
                    disks[floater]['rect'].midtop = (towers_midx[pointing_at], 400-23)
                    steps += 1
            if event.key == pygame.K_SPACE and g_mode == 2:
                waiting = true
                
    screen.fill(white)
    draw_towers()
    draw_disks()
    draw_ptr()
    blit_text(screen, 'Шаги: '+str(steps), (320, 20), font_name='mono', size=30, color=black)
    pygame.display.flip()
    if not floating:check_won()
    clock.tick(framerate)
pygame.quit()
sys.exit()
