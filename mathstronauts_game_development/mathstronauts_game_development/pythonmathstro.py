import pgzrun
import random

user_name = input("create a user name 7 letters or less in length, \nthen press enter: ")

WIDTH = 1000
HEIGHT = 600
SCOREBOX_HEIGHT = 50

score = 0

junk_speed = 5
sat_speed = 3
debris_speed = 7
laser_speed = -7

BACKGROUND_IMG = "background"
PLAYER_IMG = "my_ship"
JUNK_IMG = "junk"
SATELLITE_IMG = "satalite"
DEBRIS_IMG = "tesla_roadster"
LASER_IMG = "laser_red"

player = Actor(PLAYER_IMG)
player.midright = (WIDTH -15, HEIGHT/2)

junks = []
for i in range(5):
    junk = Actor(JUNK_IMG)
    x_pos = random.randint (-1000, -50)
    y_pos = random.randint (SCOREBOX_HEIGHT + 20, HEIGHT - junk.height - 20)
    junk.pos = (x_pos, y_pos)
    junks.append(junk)

debris = Actor(DEBRIS_IMG)
x_deb = random.randint (-1000, -100)
y_deb = random.randint (SCOREBOX_HEIGHT + 20, HEIGHT - debris.height - 20)
debris.topright = (x_deb, y_deb)

satellite = Actor(SATELLITE_IMG)
x_sat = random.randint (-1000, -100)
y_sat = random.randint (SCOREBOX_HEIGHT + 20, HEIGHT - satellite.height - 20)
satellite.topright = (x_sat, y_sat)

lasers = []

sounds.spacelife.play(-1)

def update():
    if score >= -50:
        updateplayer()
        updatejunk()
        secretkey()
        updatesatellite()
        updatedebris()
        updatelasers()
    
def draw():
    screen.clear()
    screen.blit(BACKGROUND_IMG, (0, 0))
    player.draw()
    for junk in junks:
        junk.draw()
    satellite.draw()
    debris.draw()
    for laser in lasers:
        laser.draw()

    if score < - 50:
        game_over = "GAME OVER"
        screen.draw.text(game_over, center=(WIDTH/2, HEIGHT/2), fontsize=100, color="red", owidth=0.9, ocolor="green")
        sounds.spacelife.stop()

    show_score = "Score: " + str(score)
    screen.draw.text(show_score, topleft=(750, 7), fontsize=50,color='green')
    show_name = "player: " + user_name
    screen.draw.text(show_name, topleft=(450, 7), fontsize=50,color='green')

def updateplayer():
    if keyboard.up == 1:
        player.y += -5
    if keyboard.w == 1:
        player.y += -5
    elif keyboard.down == 1:
        player.y += 5
    elif keyboard.s == 1:
        player.y += 5
    if player.top < SCOREBOX_HEIGHT:
        player.top = SCOREBOX_HEIGHT
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT
    if keyboard.space or keyboard.left or keyboard.a == 1:
        laser = Actor(LASER_IMG)
        laser.midright = (player.midleft)
        fireLasers(laser)

def updatejunk(): 
    global score
    for junk in junks:
        junk.x += junk_speed
        collision = player.colliderect(junk)
        if junk.left > WIDTH or collision == 1:
            x_pos = random.randint (-1000, -50)
            y_pos = random.randint (SCOREBOX_HEIGHT + 20, HEIGHT - junk.height - 20)
            junk.topleft = (x_pos, y_pos)
        if collision == 1:
            sounds.collect_pep.play()
            score += 1
            if (score >+ 20 and score%5==0):
                junk = Actor(JUNK_IMG)
                x_pos = random.randint (-1000, -50)
                y_pos = random.randint (SCOREBOX_HEIGHT + 20, HEIGHT - junk.height - 20)
                junk.pos = (x_pos, y_pos)
                junks.append(junk)

def updatesatellite():
    global score
    satellite.x += sat_speed
    collision = player.colliderect(satellite)

    if satellite.left > WIDTH or collision == 1:
        x_sat = random.randint (-1000, -50)
        y_sat = random.randint(SCOREBOX_HEIGHT + 20, HEIGHT - satellite.height - 20)
        satellite.topright = (x_sat, y_sat)
        satellite.image = SATELLITE_IMG

    if collision == 1:
        score += -5

def updatedebris():
    global score
    debris.x += debris_speed
    collision = player.colliderect(debris)

    if debris.left > WIDTH or collision == 1:
        x_deb = random.randint (-1000, -50)
        y_deb = random.randint(SCOREBOX_HEIGHT + 20, HEIGHT - debris.height - 20)
        debris.topright = (x_deb, y_deb)

    if collision == 1:
        score += -3

def updatelasers():
    global score
    for laser in lasers:
        laser.x += laser_speed
        if laser.right < 0:
            lasers.remove(laser)
        if satellite.colliderect(laser) == 1:
            lasers.remove(laser)
            satellite.image = "explosion02"
            sounds.explosion.play()
            clock.schedule(remove_explosion, 1)
            score += -5
        if debris.colliderect(laser) == 1:
            lasers.remove(laser)
            debris.image = "explosion02"
            sounds.explosion.play()
            clock.schedule(remove_d_explosion, 1)
            score += 7

player.laserActive = 1

def makeLaserActive():
    global player
    player.laserActive = 1

def fireLasers(laser):
    if player.laserActive == 1: 
        player.laserActive = 0
        clock.schedule(makeLaserActive, 0.2) 
        sounds.laserfire03.play()
        lasers.append(laser)

def remove_explosion():
    x_sat = random.randint(-500, -50)
    y_sat = random.randint(SCOREBOX_HEIGHT, HEIGHT - satellite.height)
    satellite.topright = (x_sat, y_sat)
    satellite.image = SATELLITE_IMG

def remove_d_explosion():
    x_deb = random.randint(-500, -50)
    y_deb = random.randint(SCOREBOX_HEIGHT, HEIGHT - debris.height)
    debris.topright = (x_deb, y_deb)
    debris.image = DEBRIS_IMG

def secretkey():
    #somthing I added
    global score
    if keyboard.q == 1:
        score += 100
    elif keyboard.e == 1:
        score -= 100
    #somthing I added

pgzrun.go() #end of code
