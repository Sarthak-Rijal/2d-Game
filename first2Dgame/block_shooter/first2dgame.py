

import pygame
import sys
import time
import random

pygame.init()

wwidth    = 800
wheight   = 500
screen    = pygame.display.set_mode((wwidth,wheight))
clock     = pygame.time.Clock()
FPS       = 60

#pics
GUN_MAN   = "gun.png"
BANG_BANG = "bang.png"
#audio
SHOT_SOUND = pygame.mixer.Sound("shot_sound.wav")
RELOAD = pygame.mixer.Sound("reload.wav")


WHITE    = (255,255,255)
RED      = (225,0,0)
NAVYBLUE = (60,60,100)
BLUE     = (0,0,255)
GREY     = (84,84,84)
BLACK    = (0,0,0)

#Character position

TOP_POS=(85,155)
MIDDLE_POS = (60,285)
END_POS=(35,315)

#bullet/enemy location
B_TOP    = (154,166)
B_MIDDLE = (129,246)
B_END    = (104,326)

SIZ_X = 35
SIZ_Y = 65

RE_POS = 800
DEAD_LINE = 130
#Position Evaluator        
def pos(pos_x):
    if pos_x == 85:
        return B_TOP[0],B_TOP[1]
    elif pos_x == 60:
        return B_MIDDLE[0],B_MIDDLE[1]
    elif pos_x == 35:
        return B_END[0],B_END[1]
#Hit check
def hit_check(bullet_x,bullet_y, hit_list_x, hit_list_y):
    h_x = 0
    h_y = 0
    for i in range(6):
        if bullet_y <= hit_list_y[i]+SIZ_Y and bullet_y >= hit_list_y[i]:
            if bullet_x >= hit_list_x[i] and bullet_x <= hit_list_x[i]+SIZ_X:
                        h_x,h_y = hit_list_x[0], hit_list_y[i]

    if h_x != 0:
        for i in range(6):
            if h_y <= hit_list_y[i]+SIZ_Y and h_y >= hit_list_y[i]:
                for i in range(6):
                    if h_x <= hit_list_x[i]+SIZ_X and h_x >= hit_list_x[i]:
                        return True

def crash(msg,color):
    font = pygame.font.Font("freesansbold.ttf",55)
    text = font.render(msg,True,color)
    screen.blit(text,[wheight/2,wwidth/2])


def game_loop():
    #loading external things
    MAN  = pygame.image.load(GUN_MAN).convert_alpha()
    BANG = pygame.image.load(BANG_BANG).convert_alpha()
    #Initial character position
    character_strt_pos_x = 60
    character_strt_pos_y = 235
    #The bang starting pos
    bang_strt_pos_x   = 123
    bang_strt_pos_y   = 237
    
    pos_change_x      = 25
    pos_change_y      = 80
    #The shot starting posioion
    shot_x = 129
    shot_y = 246
    #Bullet dimention
    B_H = 3
    B_W = 10
    #shot_count starts off the shooting
    shot_count = 0
    shot_speed = 25
    #Isolates where the bullet will go
    iso_a = 1
    iso_b = 1
    iso_c = 1
    iso_d = 1
    iso_e = 1
    #the 5 ammo objects because i cant do object oriented programming right now
    ammo_a=0
    ammo_b=0
    ammo_c=0
    ammo_d=0
    ammo_e=0

    #enemy
    ENEMY_POS_M = [random.randrange(750,850),229]
    ENEMY_POS_T = [random.randrange(750,850),144]
    ENEMY_POS_E = [random.randrange(750,850),314]
    ENEMY_POS_M_ = [random.randrange(700,wwidth),229]
    ENEMY_POS_T_ = [random.randrange(700,wwidth),144]
    ENEMY_POS_E_ = [random.randrange(700,wwidth),314]

    #Random enemy pos
    low = 144
    high = 314
    count =  85
    

    
    e_speed = 2
    
    
    #counting shots
    CONT_SHOT_T = 0
    CONT_SHOT_M = 0
    CONT_SHOT_E = 0
    
    
    
    
  
    #Game loop
    while True:
        #sets up the background, barrier and how the x and y pos will change
        change_x = 0
        change_y = 0
        screen.fill(NAVYBLUE)
        pygame.draw.polygon(screen, GREY, [(158,221),(138,171),(77,348),(97,428)])
        pygame.draw.polygon(screen, BLACK, [(77,348),(97,428),(77,428)])
        screen.blit(MAN,(character_strt_pos_x,character_strt_pos_y))

                         
        
        
               
        #Finds Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Resets the Iso values and the bullet objects 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if shot_count > 4:
                        RELOAD.play()
                        time.sleep(1)
                        RELOAD.stop()
                        shot_count = 0
                        iso_a = 1
                        iso_b = 1
                        iso_c = 1
                        iso_d = 1
                        iso_e = 1
                    
                        ammo_a = 0
                        ammo_b =0
                        ammo_c=0
                        ammo_d=0
                        ammo_e=0
                    
                #Moves character up
                if event.key == pygame.K_UP:
                    if character_strt_pos_x == TOP_POS[0] and character_strt_pos_y == TOP_POS[1]:
                        change_x, change_y = 0,0
                    else:
                        change_x += pos_change_x
                        change_y -=pos_change_y
                #Starts of the shooting with shot_count. Displays the bang
                if event.key == pygame.K_SPACE:
                    shot_count += 1

                    if character_strt_pos_x == TOP_POS[0] and shot_count <= 5:
                        screen.blit(BANG,( bang_strt_pos_x + pos_change_x , bang_strt_pos_y - pos_change_y))
                        SHOT_SOUND.play()
                        CONT_SHOT_T += 1
                        print CONT_SHOT_T
                    elif character_strt_pos_x == MIDDLE_POS[0] and shot_count<=5:
                        screen.blit(BANG,( bang_strt_pos_x, bang_strt_pos_y))
                        SHOT_SOUND.play()
                        CONT_SHOT_M += 1
                        print CONT_SHOT_M
                    elif character_strt_pos_x == END_POS[0]and shot_count<=5:
                        screen.blit(BANG,( bang_strt_pos_x - pos_change_x , bang_strt_pos_y + pos_change_y))
                        SHOT_SOUND.play()
                        CONT_SHOT_E += 1
                        print CONT_SHOT_E

                #moves the character down
                if event.key == pygame.K_DOWN:
                    if character_strt_pos_x == END_POS[0] and character_strt_pos_y == END_POS[1]:
                        change_x, change_y = 0,0
                    else:
                        change_x -= pos_change_x
                        change_y += pos_change_y
        #updates the character posiotion
        character_strt_pos_x += change_x
        character_strt_pos_y += change_y

        #starts off each bullet object
        if shot_count==1:
            ammo_a = 1
            #isolates the path the bullet will take so it doesnt move with the
            #character
            if iso_a == 1:
                a_x,a_y = pos(character_strt_pos_x)
                iso_a = 0
        if shot_count==2:
            ammo_b = 1
            if iso_b == 1:
                b_x,b_y = pos(character_strt_pos_x)
                iso_b = 0
        if shot_count==3:
            ammo_c = 1
            if iso_c == 1:
                c_x,c_y = pos(character_strt_pos_x)
                iso_c = 0
        if shot_count==4:
            ammo_d = 1
            if iso_d == 1:
                d_x,d_y = pos(character_strt_pos_x)
                iso_d = 0
        if shot_count==5:
            ammo_e = 1
            if iso_e == 1:
                e_x,e_y = pos(character_strt_pos_x)
                iso_e = 0
    
        

        #Firing of the bullets           
        if ammo_a == 1 and a_x<wwidth:
            a_x += shot_speed
            pygame.draw.rect(screen,RED,[a_x,a_y,B_W,B_H])
            bullet_pos_x,bullet_pos_y = pos(character_strt_pos_x)
            if bullet_pos_y == B_TOP[1]:
                if hit_check(a_x,a_y,E_lst_x,E_lst_y) == True:
                    if CONT_SHOT_T % 2 == 1:
                        ENEMY_POS_T_[0] = RE_POS
                        a_x = 5000
                
                    elif CONT_SHOT_T % 2 == 0:
                        ENEMY_POS_T[0] = RE_POS
                        a_x = 5000

            if bullet_pos_y == B_MIDDLE[1]:
                if hit_check(a_x,a_y,E_lst_x,E_lst_y) == True:
                    if CONT_SHOT_M % 2 == 1:
                        ENEMY_POS_M_[0] = RE_POS
                        a_x = 5000
                
                    elif CONT_SHOT_M % 2 == 0:
                        ENEMY_POS_M[0] = RE_POS
                        a_x = 5000

            if bullet_pos_y == B_END[1]:
                if hit_check(a_x,a_y,E_lst_x,E_lst_y) == True:
                    if CONT_SHOT_E % 2 == 1:
                        ENEMY_POS_E_[0] = RE_POS
                        a_x = 5000
                
                    elif CONT_SHOT_E % 2 == 0:
                        ENEMY_POS_E[0] = RE_POS
                        a_x = 5000
            
            
                
                                
                        
                
        if ammo_b == 1 and b_x<wwidth:
            b_x += shot_speed
            pygame.draw.rect(screen,RED,[b_x,b_y,B_W,B_H])
            bullet_pos_x,bullet_pos_y = pos(character_strt_pos_x)

            if bullet_pos_y == B_TOP[1]:
                if hit_check(b_x,b_y,E_lst_x,E_lst_y) == True:
                    if CONT_SHOT_T % 2 == 1:
                        ENEMY_POS_T_[0] = RE_POS
                        b_x = 5000
                
                    elif CONT_SHOT_T % 2 == 0:
                        ENEMY_POS_T[0] = RE_POS
                        b_x = 5000

            if bullet_pos_y == B_MIDDLE[1]:
                if hit_check(b_x,b_y,E_lst_x,E_lst_y) == True:
                    if CONT_SHOT_M % 2 == 1:
                        ENEMY_POS_M_[0] = RE_POS
                        b_x = 5000
                
                    elif CONT_SHOT_M % 2 == 0:
                        ENEMY_POS_M[0] = RE_POS
                        b_x = 5000

            if bullet_pos_y == B_END[1]:
                if hit_check(b_x,b_y,E_lst_x,E_lst_y) == True:
                    if CONT_SHOT_E % 2 == 1:
                        ENEMY_POS_E_[0] = RE_POS
                        b_x = 5000
                
                    elif CONT_SHOT_E % 2 == 0:
                        ENEMY_POS_E[0] = RE_POS
                        b_x = 5000

        if ammo_c == 1 and c_x<wwidth:
            c_x += shot_speed
            pygame.draw.rect(screen,RED,[c_x,c_y,B_W,B_H])
            bullet_pos_x,bullet_pos_y = pos(character_strt_pos_x)

            if bullet_pos_y == B_TOP[1]:
                if hit_check(c_x,c_y,E_lst_x,E_lst_y) == True:
                    if CONT_SHOT_T % 2 == 1:
                        ENEMY_POS_T_[0] = RE_POS
                        c_x = 5000
                
                    elif CONT_SHOT_T % 2 == 0:
                        ENEMY_POS_T[0] = RE_POS
                        c_x = 5000

            if bullet_pos_y == B_MIDDLE[1]:
                if hit_check(c_x,c_y,E_lst_x,E_lst_y) == True:
                    if CONT_SHOT_M % 2 == 1:
                        ENEMY_POS_M_[0] = RE_POS
                        c_x = 5000
                
                    elif CONT_SHOT_M % 2 == 0:
                        ENEMY_POS_M[0] = RE_POS
                        c_x = 5000

            if bullet_pos_y == B_END[1]:
                if hit_check(c_x,c_y,E_lst_x,E_lst_y) == True:
                    if CONT_SHOT_E % 2 == 1:
                        ENEMY_POS_E_[0] = RE_POS
                        c_x = 5000
                
                    elif CONT_SHOT_E % 2 == 0:
                        ENEMY_POS_E[0] = RE_POS
                        c_x = 5000

        if ammo_d == 1 and d_x<wwidth:
            d_x += shot_speed
            pygame.draw.rect(screen,RED,[d_x,d_y,B_W,B_H])
            bullet_pos_x,bullet_pos_y = pos(character_strt_pos_x)

            if bullet_pos_y == B_TOP[1]:
                if hit_check(d_x,d_y,E_lst_x,E_lst_y) == True:
                    if CONT_SHOT_T % 2 == 1:
                        ENEMY_POS_T_[0] = RE_POS
                        d_x = 5000
                
                    elif CONT_SHOT_T % 2 == 0:
                        ENEMY_POS_T[0] = RE_POS
                        d_x = 5000

            if bullet_pos_y == B_MIDDLE[1]:
                if hit_check(d_x,d_y,E_lst_x,E_lst_y) == True:
                    if CONT_SHOT_M % 2 == 1:
                        ENEMY_POS_M_[0] = RE_POS
                        d_x = 5000
                
                    elif CONT_SHOT_M % 2 == 0:
                        ENEMY_POS_M[0] = RE_POS
                        d_x = 5000

            if bullet_pos_y == B_END[1]:
                if hit_check(d_x,d_y,E_lst_x,E_lst_y) == True:
                    if CONT_SHOT_E % 2 == 1:
                        ENEMY_POS_E_[0] = RE_POS
                        d_x = 5000
                
                    elif CONT_SHOT_E % 2 == 0:
                        ENEMY_POS_E[0] = RE_POS
                        d_x = 5000

        if ammo_e == 1 and e_x<wwidth:
            e_x += shot_speed
            pygame.draw.rect(screen,RED,[e_x,e_y,B_W,B_H])
            bullet_pos_x,bullet_pos_y = pos(character_strt_pos_x)

            if bullet_pos_y == B_TOP[1]:
                if hit_check(e_x,e_y,E_lst_x,E_lst_y) == True:
                    if CONT_SHOT_T % 2 == 1:
                        ENEMY_POS_T_[0] = RE_POS
                        e_x = 5000
                
                    elif CONT_SHOT_T % 2 == 0:
                        ENEMY_POS_T[0] = RE_POS
                        e_x = 5000

            if bullet_pos_y == B_MIDDLE[1]:
                if hit_check(e_x,e_y,E_lst_x,E_lst_y) == True:
                    if CONT_SHOT_M % 2 == 1:
                        ENEMY_POS_M_[0] = RE_POS
                        e_x = 5000
                
                    elif CONT_SHOT_M % 2 == 0:
                        ENEMY_POS_M[0] = RE_POS
                        e_x = 5000

            if bullet_pos_y == B_END[1]:
                if hit_check(e_x,e_y,E_lst_x,E_lst_y) == True:
                    if CONT_SHOT_E % 2 == 1:
                        ENEMY_POS_E_[0] = RE_POS
                        e_x = 5000
                
                    elif CONT_SHOT_E % 2 == 0:
                        ENEMY_POS_E[0] = RE_POS
                        e_x = 5000


        
        #Enemy pos change
        
        ENEMY_POS_T_[0] -=e_speed
        ENEMY_POS_M_[0] -=e_speed
        ENEMY_POS_E_[0] -=e_speed
        ENEMY_POS_T[0]  -=e_speed
        ENEMY_POS_M[0]  -=e_speed
        ENEMY_POS_E[0]  -=e_speed
        #Enemy position

        E_lst_x =[ENEMY_POS_T_[0],ENEMY_POS_M_[0],ENEMY_POS_E_[0],ENEMY_POS_T[0],ENEMY_POS_M[0],ENEMY_POS_E[0]]
        E_lst_y =[ENEMY_POS_T_[1],ENEMY_POS_M_[1],ENEMY_POS_E_[1],ENEMY_POS_T[1],ENEMY_POS_M[1],ENEMY_POS_E[1]] 

        #Enemy objects 
        pygame.draw.rect(screen,BLACK,[ENEMY_POS_T_[0],ENEMY_POS_T_[1],SIZ_X,SIZ_Y])
        pygame.draw.rect(screen,BLACK,[ENEMY_POS_M_[0],ENEMY_POS_M_[1],SIZ_X,SIZ_Y])
        pygame.draw.rect(screen,BLACK,[ENEMY_POS_E_[0],ENEMY_POS_E_[1],SIZ_X,SIZ_Y])
        pygame.draw.rect(screen,BLACK,[ENEMY_POS_T[0],ENEMY_POS_T[1],SIZ_X,SIZ_Y])
        pygame.draw.rect(screen,BLACK,[ENEMY_POS_M[0],ENEMY_POS_M[1],SIZ_X,SIZ_Y])
        pygame.draw.rect(screen,BLACK,[ENEMY_POS_E[0],ENEMY_POS_E[1],SIZ_X,SIZ_Y])

        for enemies in E_lst_x:
            if enemies < DEAD_LINE:
                crash("GAME OVER",(255,0,0))
                pygame.display.update()
                time.sleep(2)
                game_loop()
        
        

            
        
        #update and FPS
        pygame.display.update()
        clock.tick(FPS)

game_loop()
