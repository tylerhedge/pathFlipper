import json
import os
import math

middle = 8.27
def mirror (x):
    if x <= middle:
        return (2*middle) - x
    else: 
        return middle - (x-middle)


def mirrorAngle (theta):
    theta *= (math.pi/180)
    y = math.sin(theta)
    x = -math.cos(theta)
    return math.atan2(y, x)*(180/math.pi)


print('enter the file location of the path you want to mirror')
path = r"{}".format(input())


while not os.path.exists(path):
    print('the file path you have entered does not exist. Please enter a valid file path')
    path = r"{}".format(input())

print('Please enter the name of file you want to mirror not including the file extension')
filePath = r"{}".format((path + '\\' + input() + '.path'))

print(filePath)
while not os.path.exists(filePath):
    print('the file you have entered does not exist. \nPlease enter a valid file name')
    filePath = r"{}".format((input() + path))

print('Please enter the name of the new path not including the file extension')
newName = r"{}".format(input() + '.path')
f = open(filePath)
f = f.read()

y = json.loads(f)

for points in y["waypoints"]:
    points["anchorPoint"]['x'] = mirror(points["anchorPoint"]['x'])
    if points["prevControl"] != None:
        points["prevControl"]['x'] = mirror(points["prevControl"]['x'])
    if points['nextControl'] != None:
        points['nextControl']['x'] = mirror(points['nextControl']['x'])
    points['holonomicAngle'] = mirrorAngle(points['holonomicAngle'])

with open(path + '\\' + newName, "w" ) as write:
    json.dump( y , write )