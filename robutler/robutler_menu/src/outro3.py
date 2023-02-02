#!/usr/bin/env python3

import rospy
import actionlib
from interactive_markers.interactive_marker_server import *
from interactive_markers.menu_handler import *
from visualization_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def process_feedback(feedback):

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    bedroom = (0.17,3.53,1)
    # bathroom = (0.17,3.53,1)
    # gym = (0.17,3.53,1)
    kitchen = (0.17,3.53,1)

    if feedback.event_type == InteractiveMarkerFeedback.MENU_SELECT:
        if feedback.menu_entry_id == 1:
            # Go to the kitchen
            rospy.loginfo("Going to the kitchen")
            goal.target_pose.pose.position.x = kitchen[0]
            goal.target_pose.pose.position.y = kitchen[1]
            goal.target_pose.pose.orientation.w = kitchen[2]
            print("Arrived, I want a beer")
        elif feedback.menu_entry_id == 2:
            # Go to the bedroom
            rospy.loginfo("Going to the bedroom")
            goal.target_pose.pose.position.x = bedroom[0]
            goal.target_pose.pose.position.y = bedroom[1]
            goal.target_pose.pose.orientation.w = bedroom[2]
            print("Arrived, going to sleep kkkkkkk")
        client.send_goal(goal)

def main():
    
    rospy.init_node('outro3_node')

    server = InteractiveMarkerServer("outro3_marker")

    int_marker = InteractiveMarker()
    int_marker.header.frame_id = "base_footprint"
    int_marker.name = "my_marker"
    int_marker.description = "teste teste teste teste"
    int_marker.pose.position.x = 1
    int_marker.pose.position.y = 0
    int_marker.pose.position.z = 1

    menu_handler = MenuHandler()
    menu_handler.insert("Ir para a Cozinha", callback=process_feedback)
    menu_handler.insert("Ir para o Quarto", callback=process_feedback)

    control = InteractiveMarkerControl()
    control.interaction_mode = InteractiveMarkerControl.MENU
    control.name = "menu_control"
    int_marker.controls.append(control)

    server.insert(int_marker, process_feedback) 
    server.applyChanges()

    rospy.spin()

if __name__ == '__main__':
    main()