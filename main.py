import time

import numpy as np
import pygame

screenSize = [300, 300]
squareSize = [100, 100]

def drawGrid():
    font = pygame.font.SysFont("Snap ITC", 40)
    for i in range(3):
        for j in range(3):
            if grid[j][i] != 0:
                nameText = font.render(str(grid[j][i]), True, (0, 0, 255))
                drawPos = np.add(np.multiply([i, j], squareSize),
                                 np.floor_divide(np.subtract(squareSize,40), 2))
                screen.blit(nameText, drawPos)
    #lst = []
    #for i in range(0, 8):
     #   ele = int(input())

      #  lst.append(ele)  # adding the element

    #print(lst)

class Frame:
    def __init__(self, f):
        self.frame = f
    def __hash__(self):
        return hash(str(self.frame))
    def __eq__(self, other):
        if self.frame[0] != other.frame[0]:
            return False
        for i in range(3):
            for j in range(3):
                if self.frame[1][i][j] != other.frame[1][i][j]:
                    return False
        return True
    def __ne__(self, other):
        return not self.__eq__(other)
    def __repr__(self):
        return str(self.frame)

def drawLines():
    for i in range(dimensions[1] - 1): #the for is 5 time [(600/100)-1]
        pygame.draw.line(screen, (0, 0, 0), (0, squareSize[1] + (i * squareSize[1])),
                         (screenSize[0], squareSize[1] + (i * squareSize[1])));#(screen,color,start point,end point)


    for i in range(dimensions[0] - 1):
        pygame.draw.line(screen, (0, 0, 0), (squareSize[0] + (i * squareSize[0]), 0),
                         (squareSize[0] + (i * squareSize[0]), screenSize[1]));




def drawThings():
    screen.fill((255, 255, 255))
    drawLines()
    drawGrid()
    pygame.display.update()

def checkRunning():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True



def optionsGenerator(state):
    ret = []
    if state[1][0][0] == 0:
        ret.append([state[0]+1,[ [ state[1][0][1], state[1][0][0], state[1][0][2] ], state[1][1], state[1][2] ] ])
        ret.append([state[0]+1,[ [ state[1][1][0], state[1][0][1], state[1][0][2] ], [ state[1][0][0], state[1][1][1], state[1][1][2]], state[1][2] ] ])


    elif state[1][0][1] == 0:
        ret.append([state[0] + 1, [[state[1][0][1], state[1][0][0], state[1][0][2]], state[1][1], state[1][2]]])
        ret.append([state[0] + 1, [[state[1][0][0], state[1][0][2], state[1][0][1]], state[1][1], state[1][2]]])
        ret.append([state[0] + 1,[[state[1][0][0], state[1][1][1], state[1][0][2]], [state[1][1][0], state[1][0][1], state[1][1][2]],state[1][2]]])


    elif state[1][0][2] == 0:
        ret.append([state[0] + 1, [[state[1][0][0], state[1][0][1], state[1][1][2]],[state[1][1][0], state[1][1][1], state[1][0][2]], state[1][2]]])
        ret.append([state[0] + 1,[state[1][0], [state[1][1][0], state[1][1][2], state[1][1][1]], state[1][2]]])


    elif state[1][1][0] == 0:
        ret.append([state[0] + 1,[[state[1][1][0], state[1][0][1], state[1][0][2]], [state[1][0][0], state[1][1][1], state[1][1][2]],state[1][2]]])
        ret.append([state[0] + 1,[state[1][0], [state[1][1][1], state[1][1][0], state[1][1][2]],state[1][2]]])
        ret.append([state[0] + 1,[state[1][0], [state[1][2][0], state[1][1][1], state[1][1][2]], [state[1][1][0],state[1][2][1],state[1][2][2]]]])

    elif state[1][1][1] == 0:
        ret.append([state[0] + 1, [[state[1][0][0], state[1][1][1], state[1][0][2]],[state[1][1][0], state[1][0][1], state[1][1][2]], state[1][2]]])
        ret.append([state[0] + 1, [state[1][0], [state[1][1][1], state[1][1][0], state[1][1][2]], state[1][2]]])
        ret.append([state[0] + 1, [state[1][0], [state[1][1][0], state[1][1][2], state[1][1][1]], state[1][2]]])
        ret.append([state[0] + 1, [state[1][0], [state[1][1][0], state[1][2][1], state[1][1][2]],[state[1][2][0], state[1][1][1], state[1][2][2]]]])

    elif state[1][1][2] == 0:
        ret.append([state[0] + 1, [[state[1][0][0], state[1][0][1], state[1][1][2]],[state[1][1][0], state[1][1][1], state[1][0][2]], state[1][2]]])
        ret.append([state[0] + 1, [state[1][0], [state[1][1][0], state[1][1][2], state[1][1][1]], state[1][2]]])

    elif state[1][2][0] == 0:
        ret.append([state[0] + 1, [state[1][0], [state[1][2][0], state[1][1][1], state[1][1][2]],[state[1][1][0], state[1][2][1], state[1][2][2]]]])
        ret.append([state[0] + 1, [state[1][0], state[1][1],[state[1][2][1], state[1][2][0], state[1][2][2]]]])

    elif state[1][2][1] == 0:
        ret.append([state[0] + 1, [state[1][0], [state[1][1][0], state[1][2][1], state[1][1][2]],[state[1][2][0], state[1][1][1], state[1][2][2]]]])
        ret.append([state[0] + 1, [state[1][0], state[1][1],[state[1][2][1], state[1][2][0], state[1][2][2]]]])
        ret.append([state[0] + 1, [state[1][0], state[1][1], [state[1][2][0], state[1][2][2], state[1][2][1]]]])

    elif state[1][2][2] == 0:
        ret.append([state[0] + 1, [state[1][0], [state[1][1][0], state[1][1][1], state[1][2][2]],[state[1][2][0], state[1][2][1], state[1][1][2]]]])
        ret.append([state[0] + 1, [state[1][0], state[1][1], [state[1][2][0], state[1][2][2], state[1][2][1]]]])

    return ret

def h(frame): #manhaten distance
    ret = 0
    for i in range(3):
        for j in range(3):
            if frame[1][i][j] == 1:
                ret += abs(i) + abs(j)
            elif frame[1][i][j] == 2:
                ret += abs(i) + abs(j-1)
            elif frame[1][i][j] == 3:
                ret += abs(i) + abs(j-2)
            elif frame[1][i][j] == 4:
                ret += abs(i-1) + abs(j)
            elif frame[1][i][j] == 5:
                ret += abs(i-1) + abs(j-1)
            elif frame[1][i][j] == 6:
                ret += abs(i-1) + abs(j-2)
            elif frame[1][i][j] == 7:
                ret += abs(i-2) + abs(j)
            elif frame[1][i][j] == 8:
                ret += abs(i-2) + abs(j-1)
    return ret

def calCost(frame):
    f = frame[0] + h(frame) # f = g + h
    return f


if __name__ == '__main__':
    pygame.init()
    running = True
    dimensions = np.floor_divide(screenSize,squareSize)  # gives the small result of dived operation ابعاد الشبكة
    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("A* test")
    grid = [[4, 1, 0], [2, 6, 3], [7, 5, 8]]

    startFrame = [0, grid] #first احتمال
    frameList = [startFrame] #الاحتمالات الغير مدروسة
    dict = {} # بحط فيه كل احتمال مين ولده ...حيثkey مين الاحتمال و  value  مين جابو
    while True:
        j = 0 # index الفريم الاقل تكلفة
        mn = calCost(frameList[0])
        for i in range(len(frameList)):
            if calCost(frameList[i]) < mn:
                mn = calCost(frameList[i])
                j = i
        bestFrame = frameList.pop(j)
        if h(bestFrame) == 0:
            lastFrame = bestFrame
            break
        newFrames = optionsGenerator(bestFrame)
        print(optionsGenerator(bestFrame))
        for frame in newFrames:
            dict[Frame(frame)] = Frame(bestFrame) #creat path of frame
            frameList.append(frame)

    frameList = [] #use dictionary to find the path
    temp = Frame(lastFrame)
    while temp != Frame(startFrame):
        frameList.append(temp.frame)
        temp = dict[temp]

    frameList.append(startFrame)
    frameList.reverse()

    for frame in frameList:  #امشي عل grid  واطبعها frame
        grid = frame[1]
        running = checkRunning()
        drawThings()
        time.sleep(1)