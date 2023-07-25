import pygame
from math import cos,sin,radians
from time import sleep as delay

pygame.init()

side = 600

screan = pygame.display.set_mode((side+100,side))
pygame.display.set_caption("3D Cube")
Mode = True
black = (0,0,0)
angle = 0
time = 0.05
cube_size = 0
time_frame = 0

def drawing(angle_deg,cube_size):
    orig_points = [
    [-1,-1, 1],
    [1,-1,1],
    [1,1,1],
    [-1,1,1],
    [-1,-1,-1],
    [1,-1,-1],
    [1,1,-1],
    [-1,1,-1]
    ]

    points = [[0 for j in range(2)] for i in range(8)]
    rotated_3d_points = [[0 for j in range(3)] for i in range(8)]
    z_offset = -3.5
    color = (255,255,255)

    for i in range(8):
        rotated_3d_points [i][0] = orig_points [i][0] * cos(radians(angle_deg)) - orig_points [i][2] * sin(radians(angle_deg))
        rotated_3d_points [i][1] = orig_points [i][1]
        rotated_3d_points [i][2] = orig_points [i][0] * sin(radians(angle_deg)) + orig_points [i][2] * cos(radians(angle_deg)) + z_offset

        points[i][0] = round(round((side+100) / 2) + rotated_3d_points [i][0] / rotated_3d_points [i][2] * cube_size)
        points[i][1] = round(round(side / 2) + rotated_3d_points [i][1] / rotated_3d_points [i][2] * cube_size)   
    
    
    pygame.draw.lines(screan,color,True,points[:4])  #back cube
    pygame.draw.lines(screan,color,True,points[4:])  #Front cube
    
    for j in range(4):
        pygame.draw.line(screan,color,(points[j][0],points[j][1]),(points[j+4][0],points[j+4][1]))
    '''
    for i in range(4):
        pygame.draw.line(screan,color,(0,0),points[i],i+1)
    '''


    return rotated_3d_points,points


while Mode:
    if (angle < 90-3):
        angle += 3
    else:
        angle = 0

    time_frame += 1
    if time_frame < 0:
        time_frame = 0
    cube_size = (side-50) + sin(time_frame * 0.2)*(side//8.5)

    screan.fill(black)
    drawing(angle,cube_size)
    delay(time)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Mode = False
    pygame.display.flip()
pygame.quit()