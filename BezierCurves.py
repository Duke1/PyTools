#! python3
# coding=utf-8
__author__ = 'Duke'

import requests
import json

host = "http://120.26.211.239:6060"
phone = '13511111116'

PC = 0.551915024494
WINDOW_SIZE = 24


# 顺时针
def circleBezierCurves():
    radius = 3.5
    strokeWidth = 2

    # 中心点坐标
    cx = WINDOW_SIZE/2
    cy = WINDOW_SIZE/2

    #
    C = PC*radius

    # point1-point2
    print ("M {fx},{fy} ".format(fx=cx, fy=cy-radius))
    print ("C {fx1},{fy1} {fx2},{fy2} {ex},{ey} ".format(fx1=cx+C, fy1=cy-radius,fx2=cx+radius,fy2=cx-C,ex=cx+radius,ey=cy))
    #point2 - point3
    print ("C {fx1},{fy1} {fx2},{fy2} {ex},{ey} ".format(fx1=cx+radius, fy1=cy+C,fx2=cx+C,fy2=cy+radius,ex=cx,ey=cy+radius))
    #point3 - pint 4
    print ("C {fx1},{fy1} {fx2},{fy2} {ex},{ey} ".format(fx1=cx-C, fy1=cy+radius,fx2=cx-radius,fy2=cy+C,ex=cx-radius,ey=cy))
    #point4-point1
    print ("C {fx1},{fy1} {fx2},{fy2} {ex},{ey} ".format(fx1=cx-radius, fy1=cy-C,fx2=cx-C,fy2=cy-radius,ex=cx,ey=cy-radius))

def rectClip():

    # 中心点坐标
    cx = WINDOW_SIZE/2
    cy = WINDOW_SIZE/2

    half_width = 3

    print ("M {fx},{fy} ".format(fx=cx-half_width, fy=cy-half_width))
    print ("L {fx},{fy} ".format(fx=cx+half_width, fy=cy-half_width))
    print ("L {fx},{fy} ".format(fx=cx+half_width, fy=cy+half_width))
    print ("L {fx},{fy} ".format(fx=cx-half_width, fy=cy+half_width))
    print ("L {fx},{fy} ".format(fx=cx-half_width, fy=cy-half_width))


if __name__ == "__main__":
    circleBezierCurves()
    print ("\r\n\r\n\r\n")
    rectClip()
