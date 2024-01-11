import turtle
tao = turtle.Pen() # ดึงความสามารถการใช้ปากกา
tao.shape('turtle') # แปลงร่างเป็นเต่า
def Rectangle():
    ''' ฟังก์ชันนี้เอาไว้วาดรูปสี่เหลี่ยม'''
    for i in range(4):
        tao.forward(100)
        tao.left(90)

        
def Go(x,y):
    '''ฟังก์ชันนี้ไว้เลื่อนตำแหน่ง'''
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

Go(-100,0)
Rectangle()
Go(0,0)
Rectangle()
Go(100,0)
Rectangle()
Go(0,-100)
Rectangle()
Go(0,-200)
Rectangle()
Go(0,-300)
Rectangle()
