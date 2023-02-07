#!/usr/bin/env python3

import rospy
import cv2
import actionlib
import math
import os
from interactive_markers.interactive_marker_server import *
from interactive_markers.interactive_marker_server import InteractiveMarkerServer
from interactive_markers.menu_handler import *
from visualization_msgs.msg import *
from geometry_msgs.msg import Twist
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from functools import partial
from goal import movebase_client
from camera import CameraNode
from picturex import Picturex
import bluecolorout
import RedSphere

# Global variables

server = None
menu_handler = MenuHandler()
locations = [
    "Living Room",
    "Bedroom",
    "Kitchen",
    "Office",
    "Middle Bedroom"
]

objects = [
    "Portátil",
    "Cadeira",
    "Esferas Vermelhas"
]

missions = [
    "Procurar um portátil no escritório",
    "Verificar se há esferas vermelhas no quarto",
    "Verificar se a mesa está levantada",
    "Contar o número de cubos azuis no quarto do meio"
]


def Menu():

    # Menu de Navegação
    go_to = menu_handler.insert("Divisões da Casa")
    for loc in locations:
        menu_handler.insert(loc, parent=go_to, callback=partial(Navigation, loc))

    # Menu de Visualização
    photo_handle = menu_handler.insert("Tirar uma foto", callback = Photo)
    detect_handle = menu_handler.insert("Procurar")
    for obj in objects:
        menu_handler.insert(obj, parent=detect_handle, callback=partial(Detect, obj))
    
    # Menu Contador
    count_handle = menu_handler.insert("Contar número de objetos")
    for obj in objects:
        menu_handler.insert(obj, parent=count_handle, callback=partial(Count, obj))

    # Menu de Missões
    mission_handle = menu_handler.insert("Missões")
    for mission in missions:
        menu_handler.insert(mission, parent=mission_handle, callback=partial(Mission, mission))

    # Menu de Fotografar Divisão
    photo_room_handle = menu_handler.insert("Fotografar Divisão")
    for loc in locations:
        menu_handler.insert(loc, parent=photo_room_handle, callback=partial(PhotoMission, loc))

def MenuMarker(marker):
    
    int_marker = InteractiveMarker()
    int_marker.header.frame_id = "base_link"
    int_marker.name = marker
    int_marker.pose.position.z = 1.2
    int_marker.scale = 0.1

    control = InteractiveMarkerControl()
    control.interaction_mode = InteractiveMarkerControl.BUTTON
    control.always_visible = True
    control.markers.append(Sphere(int_marker))
    int_marker.controls.append(control)

    server.insert(int_marker)

# Creates a text that shows the task that the robot is doing
def TextMarker(text = "Unknow", color = [0.5, 0.5, 0.5]):

    marker = Marker()
    marker.type = Marker.TEXT_VIEW_FACING

    marker.text = text
    marker.scale.z = 0.35
    marker.pose.position.z = 0.75
    marker.color.r = color[0]
    marker.color.g = color[1]
    marker.color.b = color[2]
    marker.color.a = 1 # transparecy

    int_marker = InteractiveMarker()
    int_marker.header.frame_id = "base_link"
    int_marker.name = "text_marker"

    control = InteractiveMarkerControl()
    control.interaction_mode = InteractiveMarkerControl.BUTTON
    control.always_visible = True
    control.markers.append(marker)
    int_marker.controls.append(control)

    global server
    if server is None:
        server = InteractiveMarkerServer("menu") 
    server.insert(int_marker)
    server.applyChanges()

# Creates a sphere above the robot
def Sphere(sphere):
    
    marker = Marker()   
        
    marker.type = Marker.SPHERE
    marker.scale.x = sphere.scale
    marker.scale.y = sphere.scale
    marker.scale.z = sphere.scale
    marker.color.r = 0.8
    marker.color.g = 0.8
    marker.color.b = 0.8
    marker.color.a = 0.3

    return marker

def Navigation(location, feedback):
    handle = feedback.menu_entry_id
    rospy.loginfo(f"A ir para: {location} (handle ID {handle})")
    TextMarker(text = f"Going to: {location}",
                color = [0, 0.6, 1])
  
    if location == "Kitchen":
        spot = "3"
        movebase_client(spot)
    elif location == "Bedroom":
        spot = "1"
        movebase_client(spot)
    elif location == "Living Room":
        spot = "2"
        movebase_client(spot)
    elif location == "Office":
        spot = "4"
        movebase_client(spot)
    elif location == "Middle Bedroom":
        spot = "5"
        movebase_client(spot)
    else:
        return
    

def Photo(feedback):
    handle = feedback.menu_entry_id
    rospy.loginfo("Sorri!")

    # Inicia a captura de imagem
    TextMarker(text = "Taking a picture!",
                color = [0.1, 1, 0.2])
    CameraNode()

def Detect(obj, feedback):
    handle = feedback.menu_entry_id
    rospy.loginfo(f"À procura de: {obj}")
    #server.applyChanges()

def Count(obj, feedback):
    handle = feedback.menu_entry_id
    rospy.loginfo(f"A contar número de: {obj}")

def PhotoMission(location, feedback):

    handle = feedback.menu_entry_id
    TextMarker(text = f"Taking a picture of: {location}",
                color = [0.4, 0.7, 1])

    if location == "Kitchen":
        spot = "3"
        movebase_client(spot)
        os.system("rosrun robutler_menu picturex.py")
    elif location == "Bedroom":
        spot = "1"
        movebase_client(spot)
        os.system("rosrun robutler_menu picturex.py")
    elif location == "Living Room":
        spot = "2"
        movebase_client(spot)
        os.system("rosrun robutler_menu picturex.py")
    elif location == "Office":
        spot = "4"
        movebase_client(spot)
        os.system("rosrun robutler_menu picturex.py")
    elif location == "Middle Bedroom":
        spot = "5"
        movebase_client(spot)
        os.system("rosrun robutler_menu picturex.py")
    else:
        return


def Mission(mission, location):
    # handle = feedback.menu_entry_id
    rospy.loginfo("A executar missão: " + mission)
    TextMarker(text = f"Doing the quest: {mission}",
                color = [0.4, 0.7, 1])

    if mission == "Verificar se há esferas vermelhas no quarto":
        movebase_client("3")
        RedSphere.RedColorDetector()
    elif mission == "Procurar um portátil no escritório":
        movebase_client("1")
        os.system("roslaunch robutler_opencv1 yolo.launch")
    elif mission == "Verificar se a mesa está levantada":
        movebase_client("11")
        os.system("roslaunch robutler_opencv1 yolo.launch")
    elif mission == "Contar o número de cubos azuis no quarto do meio":
        movebase_client("2")
        bluecolorout.BlueColorDetector()
    else:
        return
if __name__ == "__main__":

    rospy.init_node("menu")
    server = InteractiveMarkerServer("menu")

    Menu()
    MenuMarker("marker")

    menu_handler.apply(server, "marker")
    TextMarker(text = "Waiting for instruction")

    server.applyChanges()

    while not rospy.is_shutdown():
        rospy.sleep(10)
    cv2.destroyAllWindows()