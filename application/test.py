import cv2
import time
import numpy as np

def transmit(msg):
    for i in range(len(msg)):
        x = msg[-(i + 1)]
        if x == '1':
            pass
            display(1)
        else:
            pass
            display(0)
        display("Green")
        cv2.waitKey(200)

def display(col):
    global red_img
    global blue_img
    global green_img
    global win
    cv2.namedWindow('display', cv2.WINDOW_FULLSCREEN)
    if col == 1:
        cv2.imshow('display', red_img)
        cv2.waitKey(1000)
        print("Displaying red")
    elif col == 0:
        cv2.imshow('display', blue_img)
        cv2.waitKey(1000)
        print("Displaying blue")
    else:
        cv2.imshow('display', green_img)
        cv2.waitKey(500)


def sep():
    cv2.namedWindow('display', cv2.WINDOW_FULLSCREEN)
    cv2.imshow('display', red_img)
    cv2.waitKey(500)
    cv2.imshow('display', blue_img)
    cv2.waitKey(500)
    print("Displaying seps")


def end():
    cv2.namedWindow('display', cv2.WINDOW_FULLSCREEN)
    cv2.imshow('display', green_img)
    cv2.waitKey(1000)
    print("Displaying green")


def start():

	cv2.namedWindow('display', cv2.WINDOW_FULLSCREEN)
	cv2.imshow('display', black_img)
	cv2.waitKey(10000)
	print("Displaying black")


if __name__ == '__main__':

    red_img = cv2.imread("red.jpg")
    blue_img = cv2.imread("blue.jpg")
    green_img = cv2.imread("green.jpg")
    black_img = np.zeros(red_img.shape)
    print("Transmitting test message 101")
    start()
    transmit("101")
    sep()
