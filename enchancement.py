import cv2

img = cv2.imread('img.png', 1) # 1 Untuk color, 0 untuk greyscale
cv2.imshow('image', img)
x = cv2.waitKey(0)

if x == 27:
    cv2.destroyAllWindows()
elif x == ord('s'):
    cv2.imread('img_copy.png', 0)
    cv2.imwrite('img_copy.png', img)
    cv2.destroyAllWindows()