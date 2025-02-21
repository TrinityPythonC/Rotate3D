from tkinter import *
import datetime
import math

mainwin = Tk()
mainwin.geometry("800x600")
mainwin.configure(bg="black")

drawcanvas = Canvas(mainwin, width = 800, height = 600, bg = "black")
drawcanvas.place(x=0,y=0)

fontmedium = ("Arial",45)
fontsmall = ("Arial",24)
fonttiny = ("Arial",18)

Points3D = []
centrex,centrey = 200,300

def addpoint(x,y,z,str1,str2):
    Points3D.append([x,y,z,str1,str2])

def MultMatrix(M1,M2):
    sum = [0,0,0]
    for j in range(3):
      for i in range(3):
        sum[j] = sum[j] + M1[j][i]*M2[i]
    return sum
    
def DoRot_x():
    drawcanvas.delete("all")
    RotMatrix = MatrixRot_x(math.pi/16)
    for pt in Points3D:
       [pt[0], pt[1], pt[2]] = MultMatrix(RotMatrix,[pt[0],pt[1],pt[2]])  
    DrawPoints()


def DoRot_y():
    drawcanvas.delete("all")
    RotMatrix = MatrixRot_y(math.pi/16)
    for pt in Points3D:
       [pt[0], pt[1], pt[2]] = MultMatrix(RotMatrix,[pt[0],pt[1],pt[2]])  
    DrawPoints()

def DoRot_z():
    drawcanvas.delete("all")
    RotMatrix = MatrixRot_z(math.pi/16)
    for pt in Points3D:
       [pt[0], pt[1], pt[2]] = MultMatrix(RotMatrix,[pt[0],pt[1],pt[2]])  
    DrawPoints()



def DrawPoints():
    drawcanvas.delete("all")
    for pt in Points3D:
        drawcanvas.create_text(centrex+pt[0]*100,centrey+pt[1]*100,text=pt[3], fill= "yellow")
        for pt2 in Points3D:
            if pt[3] in pt2[4]:
               drawcanvas.create_line(centrex+pt[0]*100,centrey+pt[1]*100,centrex+pt2[0]*100,centrey+pt2[1]*100,fill="blue",width=3)

def MakeCube():
    global Points3D
    Points3D = []
    addpoint(0,0,0,"A", "B")  # point A -> B
    addpoint(1,0,0,"B", "D")  # point B -> D
    addpoint(0,1,0,"C", "A")   # point C -> A
    addpoint(1,1,0,"D", "C")   # Point D -> C
    addpoint(0,0,1,"E", "AF")  
    addpoint(1,0,1,"F", "B") 
    addpoint(0,1,1,"G", "C")   
    addpoint(1,1,1,"H", "DG")   
    DrawPoints()



         

def MatrixRot_x(phi):
    return [[1,0,0],[0,math.cos(phi),-math.sin(phi)],[0,math.sin(phi),math.cos(phi)]]

def MatrixRot_y(phi):
    return [[math.cos(phi),0,-math.sin(phi)],[0,1,0],[math.sin(phi),0,math.cos(phi)]]

def MatrixRot_z(phi):
    return [[math.cos(phi),-math.sin(phi),0],[math.sin(phi),math.cos(phi),0],[0,0,1]]


btnRot_x = Button(mainwin,text="Rotation about x-axis",font=fontsmall,command=DoRot_x, bg="black",fg="orange")
btnRot_x.place(x=400,y=10)

btnRot_y = Button(mainwin,text="Rotation about y-axis",font=fontsmall,command=DoRot_y, bg="black",fg="orange")
btnRot_y.place(x=400,y=100)

btnRot_z = Button(mainwin,text="Rotation about z-axis",font=fontsmall,command=DoRot_z, bg="black",fg="orange")
btnRot_z.place(x=400,y=200)

btnCube_x = Button(mainwin,text="Make cube",font=fontsmall,command=MakeCube, bg="black",fg="orange")
btnCube_x.place(x=20,y=10)


mainwin.mainloop()
