import pygame
import random
import math
from pygame import mixer

pygame.init()


def vaenlane(): #et me saaks kutsuda vaenlast esile ekraanil
    if suund == "vasakule":
        screen.blit(vaenlane_pilt_vasak, (vaenlaneX, vaenlaneY))
    elif suund == "paremale":
        screen.blit(vaenlane_pilt_parem, (vaenlaneX, vaenlaneY))

def vaenlane_puffer():
    screen.blit(vaenlane_pilt_puffer, (vaenlane_pufferX, vaenlane_pufferY))

vaenlased = []
        
vaenlaste_arv = 5
for i in range(vaenlaste_arv):
    v = {
    'x': random.randint(20, 1225),
    'y': random.randint(60, 200),
    'suund': 'vasak'
  }
    vaenlased.append(v)
    
def update_enemies():
  for v in vaenlased:
    if v['suund'] == 'vasak':
      v['x'] -= vel_vaenlane
    else:
      v['x'] += vel_vaenlane

    if v['x'] <= 20:
      v['suund'] = 'parem'
    elif v['x'] >= 1170:
      v['suund'] = 'vasak'
      
def draw_enemies():
  for v in vaenlased:
    if v['suund'] == 'vasak':
      screen.blit(vaenlane_pilt_vasak, (v['x'], v['y']))
    else:
      screen.blit(vaenlane_pilt_parem, (v['x'], v['y']))

def mängija():
    screen.blit(mängija_pilt, [x, y, 100, 10])

def kuul():
    pygame.draw.circle(screen, BLACK, [x_bullet,y_bullet], 5) #joonistame KUULI [left, top]

def onKokkupõrge(vaenlased, x_bullet, y_bullet, suund):
    for v in vaenlased:
        index = vaenlased.index(v) #leiame järjendi indeksi, mille sõnastikuga me hetkel töötame
        #kontrollime y-koordinaati
        if y_bullet >= v["y"] - 25 and y_bullet <= v["y"] + 25:
            #kontrollime x-koordinaati ja suunda
            if suund == 'paremale':
                if x_bullet >= v["x"] - 55 and x_bullet <= v["x"] + 55: #kontrollib vahemikke
                    vaenlased[index]["x"] = random.randint(20, 1225)  #muudame kala x koordinaati
                    vaenlased[index]["y"] = random.randint(60, 200) #ja y koordinaati
                    return True
            elif suund == 'vasakule':
                if x_bullet >= v["x"] - 55 and x_bullet <= v["x"] + 110:
                    vaenlased[index]["x"] = random.randint(20, 1225)
                    vaenlased[index]["y"] = random.randint(60, 200)
                    return True
    return False


def näita_skoori(x, y):
    skoor = väiksem_font.render("SCORE " + str(skoor_väärtus), True, WHITE)
    screen.blit(skoor, (x, y))


#logo
logo = pygame.image.load("logo.PNG")
pygame.display.set_icon(logo)

#VÄRVID
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)

#FONT
suurem_font = pygame.font.Font("ARCADECLASSIC.TTF", 70) 
väiksem_font = pygame.font.Font("ARCADECLASSIC.TTF", 32)


#MÄNGIJA
mängija_pilt = pygame.image.load("canon.png")
mängija_pilt = pygame.transform.scale(mängija_pilt, (100, 100))
x = random.randint(10, 1185)
y = 700
vel = 10

#KALAVAENLANE
vaenlane_pilt_vasak = pygame.image.load("fishleft.png") #laeb vaenlase pildi
vaenlane_pilt_vasak = pygame.transform.scale(vaenlane_pilt_vasak, (100, 50)) #teeb vaenlase suuremaks (x,y)

vaenlane_pilt_parem = pygame.image.load("fishright.png") #laeb vaenlase pildi
vaenlane_pilt_parem = pygame.transform.scale(vaenlane_pilt_parem, (100, 50)) #teeb vaenlase suuremaks

vaenlaneX = random.randint(20, 1225) #vaenlase asukoht x-teljel
vaenlaneY = random.randint(60, 200) #vaenlase asukoht y-teljel

vel_vaenlane = 3
suund = 'vasakule' #määrab ära suuna, kuhu vaenlane läheb


#TEINE VAENLANE
vaenlane_pilt_puffer = pygame.image.load("puffer.png") #laeb vaenlase pildi
vaenlane_pilt_puffer = pygame.transform.scale(vaenlane_pilt_puffer, (100, 100)) #teeb vaenlase suuremaks (x,y)

vaenlane_pufferX = x
vaenlane_pufferY = 10

vel_puffer = 2

#skoor
skoor_väärtus = 0
tekstX = 10
tekstY = 10

#KUUL
x_bullet = x
y_bullet = y
bullet_goes_flying = False
has_bullet_been_pressed = True
vel_kuul = 20


#HÄÄL
mixer.init()
pew = pygame.mixer.Sound("peww.mp3")
ai = pygame.mixer.Sound("ai.mp3")


#sets the screen size and title
screen = pygame.display.set_mode([1300, 800])
pygame.display.set_caption("FishBlaster X")

#taust
taust = pygame.image.load("Background_scaled.png").convert()

#game running loop (vajalik selleks, et kui ära sureme, siis saame uuesti mängida
game_is_open = False
#main game running loop
running = False
#death screen running loop
death_screen = False
#start screen running loop
start_screen = True

while start_screen:
    
    screen.fill(BLACK) #teeme ekraani mustaks
    screen.blit(taust, (0, 0))
    
    for event in pygame.event.get(): #user does something
        if event.type == pygame.QUIT: #kui me paneme ekraani kinni, siis lõpetab tsükli
            start_screen = False
            
            
    #PEALKIRJA KUJUTAMINE
    tiitel = suurem_font.render("FISHBLASTER  X", 1, WHITE)
    screen.blit(tiitel, (430, 100))
    
    #NUPP
    pygame.draw.rect(screen, BLACK, (467, 270, 400, 200)) #(x,y,width,height)
    tekst = suurem_font.render("START", 1, WHITE)
    screen.blit(tekst, (580, 330))
    
    #HIIR
    hiirx, hiiry = pygame.mouse.get_pos() #hiire koordinaadid
    if pygame.mouse.get_pressed()[0] == 1: #kui hiire vasakut klahvi vajutati
        if hiirx >= 467 and hiirx <= 867 and hiiry >= 270 and hiiry <= 470: #kui hiire koordinaadid on samad, mis nupu omad
            start_screen = False #lõpetab tsükli
            running = True #läheb main mängu loopi
            game_is_open = True
            
    
    pygame.display.update()  

#game running loop
while game_is_open:
    #main loop
    while running:
        
        pygame.time.delay(10) #time delay 
        
        for event in pygame.event.get(): #user does something
            if event.type == pygame.QUIT: #kui me paneme ekraani kinni, siis lõpetab tsükli
                running = False
                game_is_open = False
        
        
        screen.fill(BLACK) #teeme ekraani mustaks
        #taustapildi kujutamine
        screen.blit(taust, (0, 0))   
        
        
        
        #SKOORI NÄITAMINE
        näita_skoori(tekstX, tekstY)
        
        #KALA VAENLASE LIIKUMINE
        update_enemies()
        
        #TEISE VAENLASE LIIKUMINE
        if skoor_väärtus >= 5: #ilmub ekraanile ainult siis, kui mängija on vähemalt 5 punkti kogunud
            #Siin liigub vaenlane mängija poole
            if round(vaenlane_pufferX, 0) >= float(x-2) and round(vaenlane_pufferX, 0) <= float(x+2): #kui pufferi x koordinaat on umbes võrdne mängija omaga, siis x koordinaadiga ei juhtu midagi
                pass
            else:
                if float(x) > round(vaenlane_pufferX, 0): #kui mängija x koordinaat on suurem kui vaenlane oma
                    vaenlane_pufferX += vel_puffer #siis vaenlase koordinaat suureneb
                elif float(x) < round(vaenlane_pufferX, 0): #kui väiksem
                    vaenlane_pufferX -= vel_puffer #siis väheneb
            
            if y > vaenlane_pufferY:  #samamoodi y-koordinaatidega
                vaenlane_pufferY += vel_puffer
            
        #kui vaenlane peaks jõudma ekraani alla, siis ta "spawnib" uuesti sisse ekraani üleval
        if vaenlane_pufferY >= 700:
            vaenlane_pufferY = 0
            vel_puffer += 0.2
            
            
        
        #NUPUVAJUTUSED, MILLE ABIGA MÄNGIJA LIIGUB JA KUUL LENDAB
        keys = pygame.key.get_pressed() #salvestame key inputti, et ükski vahele ei jääks
        
        #MÄNGIJA LIIKUMINE
        if keys[pygame.K_LEFT] and x > 10: #left-arrow-key'ga muutub x-i kordinaat 10 korda väiksemaks, objekt liigub vasakule, aga ei lähe ekraani seest välja
            x -= vel

        elif keys[pygame.K_RIGHT] and x < 1185: #right-arrow-key'ga sama asi
            x += vel
        
        #KUULI LENDAMINE
        if keys[pygame.K_UP]: #kui me vajutame up-key'i
            bullet_goes_flying = True #siis kuul läheb lendama
            if has_bullet_been_pressed == True: #kui muutuja on True (ta on alguses True)
                x_bullet = x + 50 #siis annama kuulile koordinaadi kätte
                has_bullet_been_pressed = False #enam ei ole vajutatud. Seda muutujat on vaja, et ta üks kord annaks kuulile koordinaadi ette
                pygame.mixer.Sound.play(pew) #paneme selle siia, mitte kohe algusesse selleks, et ta ütleks pew ainult üks kord

        if bullet_goes_flying == True: #kui kuul on lendamas
            kuul()
            y_bullet -= vel_kuul #muudame kuuli kiirust
            if y_bullet < 0:
                has_bullet_been_pressed = True
                bullet_goes_flying = False
                y_bullet = y
                
        #kuuli kokkupõrge kalaga
        kokkupõrge = onKokkupõrge(vaenlased, x_bullet, y_bullet, suund)
        if kokkupõrge:
            skoor_väärtus += 1
            y_bullet *= -1
            
        
        #SUREMINE (kui vaenlane puudutab mängijat ehk tema koordinaate)
        if vaenlane_pufferY >= y-70 and vaenlane_pufferX >= x-2 and vaenlane_pufferX <= x+2:
            pygame.mixer.Sound.play(ai) #teeb ai häält
            running = False #läheb mängutsüklist välja
            death_screen = True #death-screeni tsüklisse
            mängija_alive = False
            
            
        #VAENLASTE JA MÄNGIJA LISAMINE
        mängija()
        draw_enemies() 
        if skoor_väärtus >= 5:    
            vaenlane_puffer()
        
        
        pygame.display.update() #updatib ekraani

    while death_screen:
        
        screen.fill(BLACK) #teeme ekraani mustaks
        #taustapildi kujutamine
        screen.blit(taust, (0, 0))
        
        
        #TEKSTI KUJUTAMINE
        tiitel = suurem_font.render("YOU DIED", 1, WHITE)
        screen.blit(tiitel, (510, 100))
        
        #NUPP
        pygame.draw.rect(screen, BLACK, (425, 270, 450, 200)) #(x,y,width,height)
        tekst = suurem_font.render("START AGAIN", 1, WHITE)
        screen.blit(tekst, (450, 330))
        
        #HIIR
        hiirx, hiiry = pygame.mouse.get_pos() #hiire koordinaadid
        if pygame.mouse.get_pressed()[0] == 1: #kui hiire vasakut klahvi vajutati
            if hiirx >= 425 and hiirx <= 825 and hiiry >= 270 and hiiry <= 470: #kui hiire koordinaadid on samad, mis nupu omad
                death_screen = False #lõpetab tsükli
                running = True #läheb main mängu loopi
                skoor_väärtus = 0 #restardime score'i, mängija ja vaenlaste koordinaadid ehk muudame kõikide asukohad ära
                x = random.randint(10, 1185)
                vaenlane_pufferY = 10 #paneme pufferi tagasi ekraani üles
                vaenlane_pufferX = x
                vel_puffer = 2
                for v in vaenlased:
                    v["x"] = random.randint(20, 1225)
                    v["y"] = random.randint(60, 200)
                
               
        
        
        for event in pygame.event.get(): #user does something
            if event.type == pygame.QUIT: #kui me paneme ekraani kinni, siis lõpetab tsükli
                death_screen = False
                game_is_open = False
                
        pygame.display.update()

pygame.quit()
