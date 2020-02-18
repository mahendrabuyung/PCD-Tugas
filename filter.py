import numpy as np
import cv2
import random
import glob
import math


cap = cv2.VideoCapture(0)

frames_per_seconds = 30
save_path='saved-media/filter.mp4'


def apply_invert(frame):
    return cv2.bitwise_not(frame)

def verify_alpha_channel(frame):
    try:
        frame.shape[3] # 4th position
    except IndexError:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    return frame


def apply_color_overlay(frame, intensity=0.2, blue = 0, green = 0, red = 0):
    frame = verify_alpha_channel(frame)
    frame_h, frame_w, frame_c = frame.shape
    color_bgra = (blue, green, red, 1)
    overlay = np.full((frame_h, frame_w, 4), color_bgra, dtype='uint8')
    cv2.addWeighted(overlay, intensity, frame, 1.0, 0, frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    return frame

def apply_sepia(frame, intensity=0.7):
    blue = 20
    green = 66
    red = 112
    frame = apply_color_overlay(frame, intensity=intensity, blue=blue, green=green, red=red)
    return frame


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()


    sepia = apply_sepia(frame.copy())
    cv2.imshow('sepia', sepia)

    #Dominan merah
    red_color = apply_color_overlay(frame.copy(), intensity=.5, red=230, blue=10)
    cv2.imshow('red_color', red_color)

    #Invert pixel menjadi negatif
    invert = apply_invert(frame)
    cv2.imshow('invert', invert)

    #cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()