#!/usr/bin/env python3

import rospy
from interactive_markers.interactive_marker_server import *
from interactive_markers.menu_handler import *
from visualization_msgs.msg import *

def process_feedback(feedback):
    print(feedback.menu_entry_id)

def main():
    rospy.init_node('outro2_node')

    server = InteractiveMarkerServer("outro2_marker")

    int_marker = InteractiveMarker()
    int_marker.header.frame_id = "base_link"
    int_marker.name = "my_marker"
    int_marker.description = "My Marker"
    int_marker.pose.position.x = 5
    int_marker.pose.position.y = 1
    int_marker.pose.position.z = 1

    control = InteractiveMarkerControl()
    control.interaction_mode = InteractiveMarkerControl.MENU
    control.name = "menu_control"
    int_marker.controls.append(control)

    menu_handler = MenuHandler()
    menu_handler.insert("First Entry", callback=process_feedback)
    menu_handler.insert("Second Entry", callback=process_feedback)
    menu_handler.insert("Third Entry", callback=process_feedback)

    server.insert(int_marker, process_feedback)
    menu_handler.apply(server, int_marker.name)
    server.applyChanges()

    rospy.spin()

if __name__ == '__main__':
    main()
