#!/usr/bin/env python
# coding: utf-8

# ### Image Processing
# 
# - This program will process a file of a moonboard problem, and output the sequence
# 
# 




#(7,35)
#397x611
#a moonboard grid is 11x18
# A-K, 1-18
from PIL import Image as im


#parameters
x,y = 47,60
CHECKDELTA = 19
x2,y2 = x+ CHECKDELTA, y - CHECKDELTA
RED = (255,0,0,255)
GREEN = (0,255,0,255)
BLUE = (0,0,255,255)
DELTAx = 31
DELTAy = 31
TOLERANCE = 6
SEARCH_SIZEx = 2
SEARCH_SIZEy = 2


#dictionaries
y_dict = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18"

    ]
y_dict = y_dict[::-1]
x_dict = [
    "K",
    "J",
    "I",
    "H",
    "G",
    "F",
    "E",
    "D",
    "C",
    "B",
    "A" 
]

x_dict = x_dict[::-1]

HOLD_TYPE = {
    "START": 0.5,
    "INTERMEDIATE": 0.75,
    "END": 1.0,
    "NULL": 0,
}

#debugging helper function
def draw(x,y,pixels,COLOUR):
    for i in range (x-SEARCH_SIZEx,x+SEARCH_SIZEx):
        for j in range(y-SEARCH_SIZEy,y+SEARCH_SIZEy):
            pixels[i,j] = COLOUR
            
def prettyPrint(mat):
    for i in mat:
        s = ''
        for j in i:
            s += str(j) + '\t'
        print (s)
            
#evaluate is a function the determines the type of hold in section l1,l2
#i,j are the x and y positions of check position 1, and i2 and j2 are the x and y or check position 2
#it then searches around the search positions i,j within the search size for the given dimension, and checks the colours
#if the amount of coloured pixels is above a threshold tolerance, it is then labelled to of that type of hold
def evaluate(i,j,i2,j2, l1,l2,pixels):
    c_r = 0
    c_g = 0
    c_b = 0
    for x in range(i-SEARCH_SIZEx,i+SEARCH_SIZEx):
        for y in range(j-SEARCH_SIZEy,j+SEARCH_SIZEy):
            if(pixels[x,y] == RED ):
                c_r +=1
            elif(pixels[x,y] == GREEN ):
                c_g += 1 
            elif(pixels[x,y] == BLUE ):
                c_b += 1
    for x in range(i2-SEARCH_SIZEx,i2+SEARCH_SIZEx):
        for y in range(j2-SEARCH_SIZEy,j2+SEARCH_SIZEy):
            if(pixels[x,y] == RED ):
                c_r +=1
            elif(pixels[x,y] == GREEN ):
                c_g += 1 
            elif(pixels[x,y] == BLUE ):
                c_b += 1
                
    if(c_r > TOLERANCE):
        return ((x_dict[l1]+y_dict[l2]),"END")
    if(c_b >TOLERANCE):
        return ((x_dict[l1]+y_dict[l2]),"INTERMEDIATE")
    if(c_g >TOLERANCE):
        return ((x_dict[l1]+y_dict[l2]),"START")
        
    return ((x_dict[l1]+y_dict[l2]),"NULL")

#image is a filename containing the image
def process(image):
    image = im.open(image)

    pixels = image.load()
    
    path = []
    mat = [[0 for i in range(11)] for i in range(18)]
    for j in range(16,-1,-1):
        y_i = y + j * DELTAy
        y_j = y2 + j * DELTAy
        for i in range(10,-1,-1):
            x_i = x + i * DELTAx
            x_j = x2 + i * DELTAx
            #path.append(x_dict[i]+y_dict[j])
            e = evaluate(x_i,y_i,x_j,y_j,i,j,pixels)
            mat[j][i]=HOLD_TYPE[e[1]]
            if( e[1] !="NULL"):
                path.append(e)
            #draw(x_i,y_i,pixels,RED)
            #draw(x_j,y_j,pixels,BLUE)
    image.show()
    return(path,mat)



#process("t3.png")




'''T1=[
    'F5', 
    'G6', 
    'J7', 
    'J8', 
    'E10', 
    'F11', 
    'C13',
    'D13', 
    'E15', 
    'G18'
]'''
#test1 = process("t1.png")

#t1 = [1 for i in range(len(test1)) if test1[i][0] != T1[i]]
#assert sum(t1) == 0
'''T2=[
    'G2',
    'J2',
    'G8',
    'E8',
    'F13',
    'C13',
    'C16',
    'A18',
]'''

