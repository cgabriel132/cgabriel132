#!/usr/bin/env python3

# Import the necessary libraries
import rospy
import actionlib
from interactive_markers.menu_handler import MenuHandler
from interactive_markers.interactive_marker_server import InteractiveMarkerServer
from visualization_msgs.msg import InteractiveMarker, InteractiveMarkerControl, InteractiveMarkerFeedback
from visualization_msgs.msg import Marker
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Point 

# Create the callback function for menu options
def processFeedback(feedback):

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    bedroom = (0.17,3.53,1)
    bathroom = (0.17,3.53,1)
    gym = (0.17,3.53,1)
    kitchen = (0.17,3.53,1)

    if feedback.event_type == InteractiveMarkerFeedback.MENU_SELECT:
        if feedback.menu_entry_id == 1:
            # Go to the kitchen
            rospy.loginfo("A ir para a cozinha")
            goal.target_pose.pose.position.x = kitchen[0]
            goal.target_pose.pose.position.y = kitchen[1]
            goal.target_pose.pose.orientation.w = kitchen[2]
            print("Cheguei, quero uma cerveja")
        elif feedback.menu_entry_id == 2:
            # Go to the bedroom
            rospy.loginfo("A ir para o quarto")
            goal.target_pose.pose.position.x = bedroom[0]
            goal.target_pose.pose.position.y = bedroom[1]
            goal.target_pose.pose.orientation.w = bedroom[2]
            print("Cheguei, vou dormir kkkkkkk")

# Initialize the ROS node
rospy.init_node("my_rviz_menu")

# Create the InteractiveMarkerServer
server = InteractiveMarkerServer("my_menu")

# Create the MenuHandler
menu_handler = MenuHandler()

# Add the menu option
entry_handle = menu_handler.insert("Go to the kitchen", callback=processFeedback)
menu_handler.insert("Go to the bedroom", callback=processFeedback)

# Create the InteractiveMarker for the menu
int_marker = InteractiveMarker()
int_marker.header.frame_id = "base_footprint"
int_marker.name = "Menu"
int_marker.description = "Missões"
int_marker.pose.position.x = 1.0
int_marker.pose.position.y = 2.0
int_marker.pose.position.z = 0
int_marker.pose.orientation.w = 1.0

# Create a Marker
marker = Marker()
marker.type = Marker.SPHERE
marker.scale.x = 0.45
marker.scale.y = 0.45
marker.scale.z = 0.45
marker.color.r = 0.0
marker.color.g = 1.0
marker.color.b = 0.0
marker.color.a = 1.0

# Create a control for the InteractiveMarker
control = InteractiveMarkerControl()
control.interaction_mode = InteractiveMarkerControl.MENU
control.always_visible = True
control.name = "Menu Control"
control.markers.append(marker)

# Add the control to the InteractiveMarker
int_marker.controls.append(control)

# Add the InteractiveMarker to the server
# server.insert(int_marker, processFeedback)

# Apply the menu to the InteractiveMarkerServer
menu_handler.apply(server, "Menu")

# Apply changes
server.insert(int_marker, processFeedback)
server.applyChanges()