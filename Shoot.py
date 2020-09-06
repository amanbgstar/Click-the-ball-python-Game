from random import randint

ball=Actor("ball")

def draw():
    screen.clear()
    ball.draw()


def on_mouse_down(pos):
    
    if ball.collidepoint(pos):
        
        print('Good Shot')
        
        place_ball()
    
    
        

       
         
    else:
        print('Game over ')
        quit()

    
def place_ball():
    ball.x = randint(10, 800)
    ball.y = randint(10, 600)

place_ball()

