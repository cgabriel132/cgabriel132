# Import Library
import cv2

def main():

    image_filename = '/home/gabriel/Documents/Aula5/images/atlascar2.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_thresholded = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)

    print(image.shape)
    print(image_gray.shape)
    print(image_thresholded.shape)

    cv2.imshow('Atlas Car', image)  # Display the image
    cv2.imshow('Atlas Car but depressed', image_gray)
    cv2.imshow('Atlas Car but depressed', image_thresholded)
    cv2.waitKey(0) # wait for a key press before proceeding



if __name__ == "__main__":
    main()