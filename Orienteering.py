"""
This program is a simulation of orienteering game that uses A* algorithm to find the path between points which
include all the control points between the paths.

"""

# Author: Prasanna Bhope

from PIL import Image, ImageDraw
import math
import sys


def calc_heuristic(start,end):
    #We will be taking the speed as maximum i.e 12m/s to calculate the heuristic of every pixel from goal
    # irrespective of the elevation. This function will return time.
    return calc_time(calc_distance(start,end),12)

def calc_path(pixel_speed,pixel_elev,path,height,width):
    if len(path) == 0:
        return [0]
    opened = []
    closed = []
    f_n = {}
    total_time = 0
    i = 0
    check_time = 0
    while(len(path) != 0):
        start = path[0]
        goal = path[1]

        opened.append(start)

        while(start != goal):
            if goal == opened[0]:
                opened.append(goal)
                break
            children = listOfNeighbours(start,height,width)
            if (len(children) == 0):
                break
            for child in children:
                if(len(children) == 1):
                    break
                if child not in opened:
                    num = float((calc_3Ddistance(pixel_elev,start,child)))
                    check_time = (calc_time(num,pixel_speed.get(start)))
                    time_cost = total_time + check_time
                    heuristic = calc_heuristic(child,goal)
                    f_n.update({child:time_cost + heuristic})
                else:
                    continue
            key = []
            temp = min(f_n.values())
            for key,value in f_n.items():
                if temp == value:
                    n = float((calc_3Ddistance(pixel_elev,start,key)))
                    total_time = total_time + calc_time(n,pixel_speed.get(start))
                    opened.append(key)
                    del_key = key
            f_n.pop(del_key)
            start = opened[-1]
        path.pop(0)
        if(len(path) == 1):
            break
        start = path[0]
        goal = path[1]
    return (opened)


def calc_time(distance, speed):
    if speed == 0:
        return -999
    return distance/speed

def calc_3Ddistance(pixel_eval,start,end):
    z1 = float(pixel_eval.get(start))
    z2 = float(pixel_eval.get(end))
    if z1 or z2 == None:
        return -999
    # print(z1,z2)
    num = float(math.sqrt((math.pow((z2 - z1), 2)) + (math.pow((end[1] - start[1], 2))+(math.pow((end[0] - start[0]), 2)))))
    return num

def listOfNeighbours(pixel,height,width):
    row = pixel[0]
    col = pixel[1]
    alist = []
    if row < 0 or col < 0 or col > width or row > height:
        return [0]
    if row == 0 and col == 0:
        alist.append((row,col+1))
        alist.append((row+1,col))
        alist.append((row+1,col+1))
    elif row == height-1 and col == width - 1:
        alist.append((row-1,col))
        alist.append((row,col-1))
        alist.append((row-1,col-1))
    elif row == 0 and col != 0:
        alist.append((row,col+1))
        alist.append((row,col-1))
        alist.append((row+1,col))
        alist.append((row+1,col-1))
        alist.append((row+1,col+1))
    elif row != 0 and col == 0:
        alist.append((row-1,col))
        alist.append((row,col+1))
        alist.append((row+1,col))
        alist.append((row-1,col+1))
        alist.append((row+1,col+1))
    else:
        alist.append((row - 1, col))
        alist.append((row + 1, col))
        alist.append((row, col + 1))
        alist.append((row, col - 1))
        alist.append((row - 1, col - 1))
        alist.append((row + 1, col - 1))
        alist.append((row - 1, col + 1))
        alist.append((row + 1, col + 1))
    for word in alist:
        if (0 > word[0] > 395 or 0 > word[1] > 500):
            alist.remove(word)
    return (alist)


def calc_distance(start,end):
    num = math.sqrt((math.pow((end[1]-start[1]),2))+ (math.pow((end[0]-start[0]),2)))
    return num

def elevation_list(filename):
    elevation_list = []
    with open(filename) as f:
        for line in f:
            check = line.split()
            fincheck = check[:len(check) - 5]
            for word in fincheck:
                elevation_list.append(float(word))
    return elevation_list

def inputPath(filename):
    inputFile = []
    with open(filename) as f:
        for line in f:
            check = line.split()
            for word in check:
                inputFile.append((word))
    return inputFile

def winterMap(pix_val,height,width):
    for p in range(len(pix_val)):
        if pix_val[p] == (255, 255, 255):
            pix_val[p] = 8
        elif pix_val[p] == (255, 192, 0):
            pix_val[p] = 5
        elif pix_val[p] == (248, 148, 18):
            pix_val[p] = 10
        elif pix_val[p] == (2, 208, 60):
            pix_val[p] = 4
        elif pix_val[p] == (2, 136, 40):
            pix_val[p] = 4
        elif pix_val[p] == (5, 73, 24):
            pix_val[p] = 1
        elif pix_val[p] == (0, 0, 255):
            pix_val[p] = -1
        elif pix_val[p] == (71, 51, 3):
            pix_val[p] = 12
        elif pix_val[p] == (0, 0, 0):
            pix_val[p] = 9
        elif pix_val[p] == (205, 0, 101):
            pix_val[p] = 0
        elif pix_val[p] == (165, 242, 243):
            pix_val[p] = 2


def readImage():
    im = Image.open(sys.argv[1],'r')
    rgb_image = im.convert('RGB')
    width, height = im.size
    pix_val = list(rgb_image.getdata())
    if sys.argv[4] == 'summer' or sys.argv[4] == 'Summer' or sys.argv[4] == 'SUMMER':
        for p in range(len(pix_val)):
            if pix_val[p] == (255,255,255):
                pix_val[p] = 8
            elif pix_val[p] == (255,192,0):
                pix_val[p] = 5
            elif pix_val[p] ==(248,148,18) :
                pix_val[p] = 10
            elif pix_val[p] ==(2,208,60):
                pix_val[p] = 6
            elif pix_val[p] ==(2,136,40):
                pix_val[p] = 4
            elif pix_val[p] ==(5,73,24):
                pix_val[p] = 1
            elif pix_val[p] ==(0,0,255):
                pix_val[p] = 2
            elif pix_val[p] ==(71,51,3):
                pix_val[p] = 12
            elif pix_val[p] ==(0,0,0):
                pix_val[p] = 9
            elif pix_val[p] == (205,0,101):
                pix_val[p] = 0
    elif sys.argv[4] == 'fall' or sys.argv[4] == 'Fall' or sys.argv[4] == 'FALL':
        for p in range(len(pix_val)):
            if pix_val[p] == (255,255,255):
                pix_val[p] = 8
            elif pix_val[p] == (255,192,0):
                pix_val[p] = 5
            elif pix_val[p] ==(248,148,18) :
                pix_val[p] = 10
            elif pix_val[p] ==(2,208,60):
                pix_val[p] = 4
            elif pix_val[p] ==(2,136,40):
                pix_val[p] = 4
            elif pix_val[p] ==(5,73,24):
                pix_val[p] = 1
            elif pix_val[p] ==(0,0,255):
                pix_val[p] = 2
            elif pix_val[p] ==(71,51,3):
                pix_val[p] = 12
            elif pix_val[p] ==(0,0,0):
                pix_val[p] = 9
            elif pix_val[p] == (205,0,101):
                pix_val[p] = 0

    elif sys.argv[4] == 'winter' or sys.argv[4] == 'Winter' or sys.argv[4] == 'WINTER':
        winterMap(pix_val,height,width)
    i = 0
    j = 0
    pixel_xy = []
    pixel_speed = {}
    for col in range(height):
        for row in range(width):
            pixel_xy.append((row,col))
            pixel_speed.update({pixel_xy[j]:pix_val[j]})
            j = j +1
    eval = elevation_list(sys.argv[2])
    pixel_elev = {}
    for i in range(len(eval)):
        pixel_elev.update({pixel_xy[i]:eval[i]})

    pathList = inputPath(sys.argv[3])
    path = []
    i =0
    while i < (len(pathList)):
        path.append((int(pathList[i]),int(pathList[i+1])))
        i = i+2

    res = calc_path(pixel_speed,pixel_elev,path,height,width)
    for x in range(len(res)):
        im.putpixel( res[x], (103, 65, 114))

    im.save(sys.argv[5])
    im.show()




if __name__ == '__main__':
    readImage()



"""
Open land : Speed = 10 m/s
Rough meadow: Speed = 5 m/s
Easy movement forest: steep? Speed = 6 m/s :: Speed = 8 m/s  For Fall: 4m/s
Slow run forest: Speed = 6 m/s
Walk forest = 4 m/s
Impassible vegetation: Speed = 3 m/s
Lake/Swamp/Marsh: Speed = 2 m/s
Paved Road: Speed = 12 m/s
Footpath: 9 m/s
Out of Bounds: 0 m/s
Icy surface = 2 m/s
"""
