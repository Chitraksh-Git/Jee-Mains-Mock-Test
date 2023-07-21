import pygame
import sys
from pygame.locals import *
import datetime
from datetime import timedelta
import pandas as pd

pygame.init()

WIDTH,HEIGHT = 800, 600
DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('JEE MAIN MOCK TEST')

font60 = pygame.font.SysFont("Arial",60)
font40 = pygame.font.SysFont("Arial",40)
font30 = pygame.font.SysFont("Arial",30)

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#EVENTS
START_SCREEN = pygame.USEREVENT + 1
TEST_MODE = pygame.USEREVENT + 2

class Button():
    def __init__(self, x, y, width, height, buttonText='Button',textcolor=BLACK,fillcolor=GREEN):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text= buttonText
        self.surf=pygame.Surface((width,height))
        self.rect=self.surf.get_rect(center=(self.x,self.y))
        self.textcolor = textcolor
        self.fillcolor = fillcolor

    def draw(self):
        rtext = font40.render(self.text,1,self.textcolor)
        self.surf.fill(self.fillcolor)
        DISPLAY.blit(self.surf,self.rect)
        DISPLAY.blit(rtext,self.rect)
        
              
def draw_start_screen():  
    DISPLAY.fill(BLACK) # Changed the background color to black
    
    jee_text=font60.render('JEE MAINS MOCK TEST',1,WHITE) # Changed the text color to white
    jee_textrect=jee_text.get_rect(center=(WIDTH/2,100)) # Changed the y coordinate to 100
    DISPLAY.blit(jee_text,jee_textrect)

    choose_duration_text = font40.render('CHOOSE DURATION OF YOUR EXAM:',1,WHITE) # Changed the text color to white
    choose_duration_textrect=choose_duration_text.get_rect(center=(WIDTH/2,200)) # Changed the y coordinate to 200
    DISPLAY.blit(choose_duration_text,choose_duration_textrect)
    
    min30 = Button((WIDTH)/2,300,150,70,'30 mins') # Changed the width and height of the button to make it smaller
    min60 = Button((WIDTH)/2,375,150,70,'60 mins') # Changed the width and height of the button to make it smaller and the y coordinate to arrange it vertically
    min90 = Button((WIDTH)/2,450,150,70,'90 mins') # Changed the width and height of the button to make it smaller and the y coordinate to arrange it vertically
    
    buttonlist=[min30,min60,min90]
    
    for button in buttonlist:
         button.draw()

    return buttonlist

def draw_question_screen(duration_mins,curr_que_no,elapsed_time):
     DISPLAY.fill('Black')
     dict_num_ques = {30:15,60:30,90:45}
     NUM_QUES = dict_num_ques[duration_mins]
     #print(NUM_QUES)

     ques_num_text = font30.render(f'QUES:{curr_que_no}/{NUM_QUES}',1,"white")
     DISPLAY.blit(ques_num_text,(0,0))

     time_remaining = duration_mins*60*1000 - elapsed_time
     formatted_rem_time = format_time(time_remaining)

     time_remaining_text = font30.render('TIME: '+formatted_rem_time,1,'White')
     DISPLAY.blit(time_remaining_text,(640,0))
     
     pygame.display.update()
     return curr_que_no

def format_time(time_ms):
     seconds_total = time_ms//1000
     hours = seconds_total//3600
     mins = (seconds_total//60)%60
     seconds = seconds_total%60
     formatted_time = f'{hours}:{mins}:{seconds}'

     return formatted_time

def main():
    
    CLOCK=pygame.time.Clock()
    FPS=60
    state = 'START_SCREEN'
    pygame.event.post(pygame.event.Event(START_SCREEN))
    test_start_time = 0
    elapsed_time = 0
    run = True
    
    while run:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run=False
                    pygame.quit()
                    sys.exit()
                
                if event.type == START_SCREEN:
                    buttonlist = draw_start_screen()
                
                if event.type == MOUSEBUTTONDOWN and state == 'START_SCREEN':
                    i = 30
                    for button in buttonlist:
                         if button.rect.collidepoint(event.pos):
                              duration = i 
                              #print(i)
                              pygame.display.update()
                              pygame.event.post(pygame.event.Event(TEST_MODE))
                         else:
                             i += 30
                
                if event.type == TEST_MODE:
                     state = 'TEST_MODE'
                     curr_que_no = 1
                     test_start_time = pygame.time.get_ticks()
                
                if state == 'TEST_MODE':
                     curr_que_no = draw_question_screen(duration,curr_que_no,elapsed_time)

                if test_start_time:
                     elapsed_time = pygame.time.get_ticks() - test_start_time
                

        CLOCK.tick(FPS)
        pygame.display.update()



if __name__ == '__main__':
     main()
