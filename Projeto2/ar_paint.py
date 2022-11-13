import argparse
import math
import cv2
import numpy as np
import json
from time import ctime, time
from colorama import Fore, Back, Style

global whiteboard
global frame_painting
global width_frame, height_frame
global original
width_canvas = 400
height_canvas = 800

draw_square = False
draw_circle = False
mouse_toggle = False
what_to_draw = None

painting_color = (0, 0, 0)
previous_point = (0, 0)
previous_point_hp = (0, 0)
previous_mouse_point = (0, 0)
global previous_point_shape
x_previous = 0
y_previous = 0
radius = 10
alpha = 1

# Function for the Functioning Modes
def Modes(usp, vs, mouse):
    if usp == False and vs == False and mouse == False:
        return 'normal_mode'

    elif usp == True and vs == False and mouse == False:
        return 'usp_mode'

    elif usp == True and vs == False and mouse == True:
        return 'usp_w_mouse_mode'

    elif usp == False and vs == True and mouse == False:
        return 'vs_mode'

    elif usp == False and vs == False and mouse == False:
        return 'np_mode'

    elif usp == False and vs == False and mouse == True:
        return 'pn_w_mouse_mode'

# Function for the Drawing Mouse
def Mouse(cursor, xposition, yposition, flags, param):
    # Call of Global Variables
    global previous_mouse_point

    # Calls the function when mouse_toggle is set to True and mouse is moving
    if cursor == cv2.EVENT_MOUSEMOVE and mouse_toggle == True:

        # Draws line with the mouse position
        if previous_mouse_point == (0, 0):
            previous_mouse_point = (xposition, yposition)

        aux = (previous_point[0] - xposition, previous_point[1] - yposition)
        if math.sqrt(aux[0] ** 2 + aux[1] ** 2) > 200:
            cv2.circle(param, (xposition, yposition), radius, painting_color, -1)
        else:
            cv2.line(img=param,
                     pt1=previous_mouse_point,
                     pt2=(xposition, yposition),
                     color=painting_color,
                     thickness=radius)
        previous_mouse_point = (xposition, yposition)

# Function for each Shape Drawing
def Shapes(cursor, xposition, yposition, flags, param):
    # Calling global variables
    global previous_point_shape, cX, cY, circle_radius, what_to_draw

    whiteboard_copy = param.copy()
    if draw_square == True or draw_circle == True:
        if previous_point_shape == (0, 0):
            previous_point_shape = (xposition, yposition)

        (cX, cY) = (xposition, yposition)
        if draw_square:
            cv2.rectangle(whiteboard_copy, previous_point_shape, (cX, cY), painting_color, radius)  # Square move animation
        elif draw_circle:
            aux = (cX - previous_point_shape[0], cY - previous_point_shape[1])
            circle_radius = math.sqrt(aux[0] ** 2 + aux[1] ** 2)
            cv2.circle(whiteboard_copy, previous_point_shape, int(circle_radius), painting_color, radius)
        cv2.imshow('Painting Shapes', whiteboard_copy)

    elif draw_square == False and what_to_draw == ord('s'):
        cv2.rectangle(param, previous_point_shape, (cX, cY), painting_color, radius)  # Fix the square on whiteboard
        what_to_draw = None
        return
    elif draw_circle == False and what_to_draw == ord('a'):
        cv2.circle(param, previous_point_shape, int(circle_radius), painting_color, radius)
        what_to_draw = None
        return

# Creating a menu
def menu():
    print("         -- Command List --\n")
    print("> To Clear     " + "       -> PRESS 'c'")
    print("> To Save      " + "       -> PRESS 'w'")
    print("> To see the menu     " + "-> PRESS 'z'")    
    print("> Red Paint    " + Back.RED + "      " + Style.RESET_ALL + " -> PRESS " + Fore.RED + "'r'" + Fore.RESET)
    print("> Green Paint  " + Back.GREEN + "      " + Style.RESET_ALL + " -> PRESS " + Fore.GREEN + "'g'" + Fore.RESET)
    print("> Blue Paint   " + Back.BLUE + "      " + Style.RESET_ALL + " -> PRESS " + Fore.BLUE + "'b'" + Fore.RESET)
    print("> Orange Paint " + Back.LIGHTRED_EX + "      " + Style.RESET_ALL + " -> PRESS " + Fore.LIGHTRED_EX + "'o'" + Fore.RESET)
    print("> Erase        " + Back.WHITE + "      " + Style.RESET_ALL + " -> PRESS 'e'")
    print("> Thicker Brush " + "      -> PRESS '+'")
    print("> Thinner Brush " + "      -> PRESS '-'")
    print("> Square Shape  " + "      -> PRESS 's'")
    print("> Circle Shape  " + "      -> PRESS 'a'")
    print("> Mouse Mode On " + "      -> PRESS 'm'")
    print("> Mouse Mode Off " + "     -> PRESS 'n'")
    print("> To quit       " + "      -> PRESS 'q'\n")

def main():
    # Defining Global variables
    global radius, painting_color, previous_point, mouse_toggle, frame_painting, previous_point_shape
    global alpha, draw_square, draw_circle, what_to_draw
    global width_canvas, height_canvas, width_frame
    global whiteboard, previous_point_hp, height_frame
    count = 0  # Counter to print the menu after x iterations

    # Parser arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('-j', '--json_file', type=str, required=True, help='Full path to json file.')
    parser.add_argument('-usp', '--use_shake_prevention', action='store_true', help='To use shake prevention.')
    parser.add_argument('-vs', '--video_stream', action='store_true', help='To draw on displayed frame')
    parser.add_argument('-m', '--mirror_image', action='store_true', help='Mirror the image captured by camera')

    args = vars(parser.parse_args())

    # Printing the welcome menu
    print("\nAR_Paint \n\n Project done by: \n"+
        "\n Carlos Cardoso"+
        "\n Beatriz Cruzeiro"+
        "\n João Cruz"+
        " \n\nPSR, Universidade de Aveiro, November 2022.\n")

    menu()

    # Creating the boards
    window_whiteboard = "Paint"
    window_segmented = "Segmented Image"
    window_original_frame = "Original Frame"

    # Open json file
    thresh = open(args['json_file'])
    ranges = json.load(thresh)
    thresh.close()

    # Canvas size with one video capture
    video = cv2.VideoCapture(0)
    _, frame = video.read()
    width_frame, height_frame, channel = frame.shape

    if args['video_stream']:
        whiteboard = np.ones((width_frame, height_frame, channel), np.uint8)
        painting_color = (255, 0, 0)
    else:
        whiteboard = np.ones((width_frame, height_frame, channel), np.uint8) * 255

  
    while True:
        # Reading each frame of the video capture
        _, frame = video.read()

        if args['mirror_image']:
            frame = cv2.flip(frame, 1)
        
        mode = Modes(args['use_shake_prevention'], args['video_stream'], mouse_toggle)

        # Frame copies for overlays and new windows
        frame_for_segmentation = frame.copy()

        # Convert dictionary into np.arrays to define minimum thresholds
        min_thresh = np.array([ranges['limits']['B']['min'], ranges['limits']['G']['min'], ranges['limits']['R']['min']])

        # Convert dictionary into np.arrays to define maximum thresholds
        max_thresh = np.array([ranges['limits']['B']['max'], ranges['limits']['G']['max'], ranges['limits']['R']['max']])

        # Segmented mask with json
        mask_segmented = cv2.inRange(frame_for_segmentation, min_thresh, max_thresh)

        # Finding all the contours in the mask segmented
        contours, hierarchy = cv2.findContours(mask_segmented, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Counter >0 it calculates one with maximum area
        if len(contours) != 0:
            c = max(contours, key = cv2.contourArea)
            area = cv2.contourArea(c)

            # Starts painting only if it is bigger than the threshold defined
            if area > 500:
                # Extract coordinates of bounding box
                x, y, w, h = cv2.boundingRect(c)

                # Draw a green rectangle around the drawer object
                cv2.rectangle(frame_for_segmentation, (x, y), (x + w + 20, y + h + 20), (0, 255, 0), -1)
                frame = cv2.addWeighted(frame_for_segmentation, 0.2, frame, 0.8, 0)

                # Calculate the controid and draw the red cross there
                centroid = (int(x + w / 2), int(y + h / 2))
                cv2.drawMarker(frame, centroid, color = (0, 0, 255), markerType= cv2.MARKER_CROSS, thickness=3)

                # Draw on the image
                if previous_point == (0, 0):
                    previous_point = centroid
                
                # Shake prevention without mouse functionality
                if mode == 'usp_mode':
                    aux = (previous_point[0] - centroid[0], previous_point[1] - centroid[1])
                    if math.sqrt(aux[0] ** 2 + aux[1] ** 2) > 200:
                        cv2.circle(whiteboard, centroid, radius, painting_color, -1)
                    else:
                        cv2.line(img = whiteboard, pt1 = previous_point, pt2 = centroid, color = painting_color, thickness = radius)
                    previous_point = centroid
                
                # Draw only with the moving mouse functionality
                elif mode == 'usp_w_mouse_mode':
                    cv2.setMouseCallback(window_whiteboard, Mouse, param = whiteboard)

                # Normal mode -> without usp and moving mouse functionality
                elif mode == 'vs_mode':
                    cv2.line(img = whiteboard, pt1 = previous_point, pt2 = centroid, color = painting_color, thickness = radius)
                    previous_point = centroid
                
                elif mode == 'normal_mode':
                    cv2.line(img = whiteboard, pt1 = previous_point, pt2 = centroid, color = painting_color, thickness = radius)
                    previous_point = centroid
                
        
        # Plotting all windows for every mode
        if args['video_stream']:

            # Transparency of augmented reality mode
            frame_painting = cv2.bitwise_or(frame, whiteboard)
            frame_painting = cv2.addWeighted(frame_painting, alpha, frame, 1 - alpha, 0)

            # Plotting the segmented window
            cv2.namedWindow(window_segmented, cv2.WINDOW_NORMAL)
            cv2.imshow(window_segmented, mask_segmented)

            # Plotting original frame
            cv2.namedWindow(window_original_frame, cv2.WINDOW_NORMAL)
            cv2.imshow(window_original_frame, frame)

            # Whiteboard
            cv2.namedWindow('Painting Frame', cv2.WINDOW_NORMAL)
            cv2.imshow('Painting Frame', frame_painting)

        else:
            # Plotting the whiteboard
            cv2.namedWindow(window_whiteboard, cv2.WINDOW_NORMAL)
            cv2.imshow(window_whiteboard, whiteboard)

            # Plotting segmendted window
            cv2.namedWindow(window_segmented, cv2.WINDOW_NORMAL)
            cv2.imshow(window_segmented, mask_segmented)

            # Plotting the original frame
            cv2.namedWindow(window_original_frame, cv2.WINDOW_NORMAL)
            cv2.imshow(window_original_frame, frame)

        key = cv2.waitKey(20)
        if count == 15:
            menu()
            count = 0

        # Shortcuts

        if key == ord('r'):
            painting_color = (0, 0 ,255)
            print('Your pencil color is ' + Fore.RED + 'Red' + Fore.RESET)
            count += 1

        elif key == ord('g'):
            painting_color = (0, 255, 0)
            print('Your pencil color is ' + Fore.GREEN + 'Green' + Fore.RESET)
            count += 1
        
        elif key == ord('b'):
            painting_color = (255, 0, 0)
            print('Your pencil color is ' + Fore.BLUE  + 'Blue' + Fore.RESET)
            count += 1

        elif key == ord('o'):
            painting_color = (0, 155, 255)
            print('Your pencil color is ' + Fore.LIGHTRED_EX + 'Orange' + Fore.RESET + ', my favourite color!! :D')

        elif key == ord('e'):
            if args['video_stream']:
                painting_color = (0, 0, 0)
                print('You are using the eraser')
            else:
                painting_color = (255, 255, 255)
                print('You are using the eraser')
            count += 1

        elif key == ord('-'):
            if radius == 1:
                print('You have reached the minimum size!')
            else:
                radius -= 1
                print('Your pencil has ' + Fore.LIGHTYELLOW_EX + 'decreased' + Fore.RESET + ' to ' + str(radius))
            count += 1

        elif key == ord('+'):
            radius += 1
            print('Your pencil has ' + Fore.LIGHTYELLOW_EX + 'increased' + Fore.RESET + ' to ' + str(radius))
            count += 1

        elif key == ord('c'):
            if args['video_stream']:
                whiteboard = np.ones((width_frame, height_frame, channel), np.uint8)
            
            else:
                whiteboard = np.ones((width_frame, height_frame, channel), np.uint8) * 255

            print('Clearing your mess!')
            count += 1

        elif key == ord('w'):
            if args['video_stream']:
                time_string = ctime(time()).replace(' ', ' ')
                file_name = "Drawing_" + time_string + ".png"
                cv2.imwrite(file_name, frame_painting)
            else:
                time_string = ctime(time()).replace(' ', '_')
                file_name = "Drawing_" + time_string + ".png"
                cv2.imwrite(file_name, whiteboard)
            count += 1

        elif args['use_shake_prevention'] and key == ord('m'):
            mouse_toggle = True
            print("Move your mouse to paint")
            count += 1

        elif args['use_shake_prevention'] and key == ord('n'):
            mouse_toggle = False
            print('Not painting in mouse mode')
            count += 1

        elif key == ord('s'):
            print("Draw a Square")
            if not draw_square:
                previous_point_shape = (0, 0)

            draw_square = not draw_square
            what_to_draw = key
            cv2.setMouseCallback(window_whiteboard, Shapes, param = whiteboard)
            count += 1
            
        elif key == ord('a'):
            print('Draw an Circle')
            if not draw_circle:
                previous_point_shape = (0, 0)

            draw_circle = not draw_circle
            what_to_draw = key
            cv2.setMouseCallback(window_whiteboard, Shapes, param = whiteboard)
            count += 1

        elif key == ord('z'):
            menu()

        elif key == ord('q'):
            print('\nHope you had some fun! Come back soon!')
            print("\nPainters:\n\t- Carlos Cardoso \n\t- Beatriz Cruzeiro\n\t- João Cruz\n\n")
            break

if __name__ == "__main__":
      main()