import pygame
import cv2 as cv
import numpy as np
import random

pygame.init()

cap = cv.VideoCapture(0)

noiseth=800

dis_width = 600
dis_height = 400

white = (255, 255, 255) 
blue=(0,0,255)
red=(255,0,0)
black=(0,0,0)
green=(0,255,0)
yellow = (255, 255, 102)
hurdel_color =(0, 253, 253)



dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Snake game by IvLab')

clock = pygame.time.Clock()
snake_speed=10

snake_block = 10

font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 35)

def hurdel_1():
    pygame.draw.rect(dis, hurdel_color, [150, 200, 300, 50])
    pygame.draw.rect(dis, hurdel_color, [150, 150, 50, 50])
    pygame.draw.rect(dis, hurdel_color, [400, 250, 50, 50])

def hurdel_2():
    pygame.draw.rect(dis, hurdel_color, [150, 200, 300, 50])
    

def hurdel_3():
    pygame.draw.rect(dis, hurdel_color, [150, 150, 50, 50])

hurdel = [hurdel_1, hurdel_2, hurdel_3]

hur=hurdel[random.randint(0,2)]
   
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [50, 150])


def gameLoop():
    game_over=False
    game_close=False

    #initial position of snake
    x=0
    y=0
    

    x1_change = 0       
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
   

    while not game_over:

        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

                    if event.key == pygame.K_c:
                        gameLoop()


        _, frame = cap.read()
        frame = cv.flip( frame, 1 )

        new_h = 400
        new_w = 600
        resize = cv.resize(frame, (new_w, new_h))
        
        _, thresh1 = cv.threshold(resize, 120, 255, cv.THRESH_BINARY)

        # Convert BGR to HSV
        hsv = cv.cvtColor(thresh1, cv.COLOR_BGR2HSV)
       
    

        lower_range  = np.array([110,50,50])
        upper_range = np.array([130,255,255])


        mask = cv.inRange(hsv, lower_range, upper_range)
        #masking HSV value selected color becomes black
        res = cv.bitwise_and(resize, resize, mask=mask)
        cv.imshow("res",res)

        rec=cv.rectangle(resize,(200,100), (400,300), (0,255,0), 3)

        # Find Contours
        contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        cv.drawContours(mask, contours, 0, (0,255,0), 3)
        
        if contours and cv.contourArea(max(contours, key = cv.contourArea)) > noiseth:
                    
            c = max(contours, key = cv.contourArea) 
            M= cv.moments(c)   
            xc = int(M['m10']/M['m00'])
            yc = int(M['m01']/M['m00'])
            
            
            if xc>400:
                print("right")                        #xc,yc are center of stylus
                x1_change = snake_block
                y1_change = 0
            if xc<200:
                print("left")
                x1_change = -snake_block
                y1_change = 0
            if yc<100:
                print("up")
                y1_change = -snake_block
                x1_change = 0
            if yc>300:
                print("down")
                y1_change = snake_block
                x1_change = 0

    
            
        cv.imshow('frame',resize)
        cv.imshow("mask",mask)
 
        if x >= dis_width or x < 0 or y >= dis_height or y < 0:
            game_close = True

      
        if hur==hurdel_1:
            if ((150<=x<=200) and (150<=y<=200)) or ((150<=x<=450) and (200<=y<=250)) or ((400<=x<=450) and (250<=y<=300)):
                game_close = True


        if hur==hurdel_2:
            if ((150<=x<450) and (200<=y<250)):
                game_close = True

           

        if hur==hurdel_3:
            if ((150<=x<200) and (150<=y<200)):
                game_close = True

           
        #if food is in hurdels then draw new food 
        if hur == hurdel_1:
            while ((100<=foodx<500) and (100<=foody<150)):
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        if hur == hurdel_2:
            while ((300<=foodx<400) and (100<=foody<300)):
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        if hur == hurdel_2:
            while ((100<=x<400) and (200<=y<250)):
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0


        
        x += x1_change
        y += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])


        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_List.append(snake_Head)
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for i in snake_List[:-1]:
            if i == snake_Head:
                game_close = True
        
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
        hur()
        pygame.display.update()
        pygame.display.flip()

        k = cv.waitKey(5) & 0xFF
        if k == 27:
            game_over=True
        
    cv.destroyAllWindows()
    pygame.quit()
    quit()
    

gameLoop()

