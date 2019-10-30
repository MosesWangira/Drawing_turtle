import turtle

def square(brad):
     for i in range(4):
        brad.forward(100)
        brad.right(90)
             
             
def draw_shape():
    window = turtle.Screen()
    window.title("moses")
    window.bgcolor("red")


    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(5)
    for i in range(36):
        square(brad)
        brad.right(10)
    
    #moses = turtle.Turtle()
    #moses.shape("turtle")
    #moses.color("blue")
    #moses.speed(1)

    #moses.circle(100)

    

    window.exitonclick()
    
    

draw_shape()
