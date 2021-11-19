from niryo_one_python_api.niryo_one_api import *
import rospy
import time
import math
import numpy as np
from rospy.topics import Publisher

from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from sensor_msgs.msg import JointState

from niryo_one_msgs.srv import GetInt

def rs2narray(rs):
    return np.array([rs.position.x, rs.position.y, rs.position.z, rs.rpy.roll, rs.rpy.pitch, rs.rpy.yaw])

def loop():
    rospy.init_node('niryo_one_example_python_api')
    print "--- Start"

    global pub
    pub = Publisher('/name_topic', JointTrajectory)

    global joint_cmd
    global joints_str
    global point0
    global point1
    global x

    joints_str = JointTrajectory()
    joints_str.joint_names = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6']
    point0 = JointTrajectoryPoint()
    point1 = JointTrajectoryPoint()
    joint_cmd = []
    x = np.array([1.0, 0, 0.0, 0, 0, 0])
    def callback_joint_states(joint_states):
        global joint_cmd
	# do smt

        pub.publish(joints_str)

    
    sub = rospy.Subscriber('/joint_states', JointState, callback_joint_states)

    print "--- Start"

    robot = NiryoOne()

    # Calibrate robot first
    robot.calibrate_auto()
    print "Calibration finished !\n"

    time.sleep(1)

    # Test learning mode
    robot.activate_learning_mode(False)
    print "Learning mode activated? "
    print robot.get_learning_mode()
    
    # Move
    # robot.set_arm_max_velocity(50)

    rospy.spin()


    print "--- End"
