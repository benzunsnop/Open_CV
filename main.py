import cv2
import sys
import numpy as np
import math

GAUSSIAN_SMOOTH_FILTER_SIZE = (5, 5)
ADAPTIVE_THRESH_BLOCK_SIZE = 19
ADAPTIVE_THRESH_WEIGHT = 9

imgOriginalScene=cv2.imread('run.jpg')


if imgOriginalScene is None:
    print("\nError: image not read from file \n\n")
else:
    print("\nSuccess: it ok \n")
    cv2.imshow('1.imgOriginalScene',imgOriginalScene)
    cv2.waitKey(50)

    a = int(input("Enter Number 1"))
    cv2.waitKey(20)

if a == 1:
    print('Original Dimensions : ', imgOriginalScene.shape)

    scale_percent = 150  # percent of original size
    width = int(imgOriginalScene.shape[1] * scale_percent / 100)
    height = int(imgOriginalScene.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    resized = cv2.resize(imgOriginalScene, dim, interpolation=cv2.INTER_AREA)

    print('Resized Dimensions : ', resized.shape)

    cv2.imshow("2.Resized image", resized)
    cv2.waitKey(20)
    b = int(input("Enter Number 2"))
    cv2.waitKey(20)

if b == 2:
    imgHSV = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
    imgHue, imgSatur, imgValue = cv2.split(imgHSV)
    cv2.imshow('3.GrayScale', imgValue)
    cv2.waitKey(50)

    c = int(input("Enter Number 3"))
    cv2.waitKey(20)

if c == 3:
    imgBlur = cv2.GaussianBlur(imgValue,GAUSSIAN_SMOOTH_FILTER_SIZE, 2)
    cv2.imshow('4.Blur',imgBlur)
    cv2.waitKey(50)

    d = int(input("Enter Number 4"))
    cv2.waitKey(20)

if d == 4:
    imgThresh = cv2.adaptiveThreshold(imgBlur, 255.0, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, ADAPTIVE_THRESH_BLOCK_SIZE, ADAPTIVE_THRESH_WEIGHT)
    cv2.imshow('5.imgThresh',imgThresh)
    cv2.waitKey(20)

    e = int(input("Enter Number 5"))
    cv2.waitKey(20)

if e == 5:
    _,contours,_ = cv2.findContours(imgThresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    print("Number of contours = " + str(len(contours)))
    imgCon = cv2.drawContours(imgThresh,contours,-1,(0,0,0),1)
    cv2.imshow('6.imgCon',imgCon)
    cv2.waitKey(0)

