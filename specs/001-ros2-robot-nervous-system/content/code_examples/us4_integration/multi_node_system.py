# content/code_examples/us4_integration/multi_node_system.py
#
# This file contains conceptual code for both a publisher (Talker) and subscriber (Listener)
# to illustrate multi-node communication. In a real ROS 2 setup, these would typically be
# in separate Python files within their own ROS 2 packages, and launched independently.

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time # For simulation of independent processes

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(1.0, self.timer_callback) # Publish every 1 second
        self.i = 0
        self.get_logger().info('Talker node has been started.')

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello from Talker: {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(String, 'chatter', self.listener_callback, 10)
        self.get_logger().info('Listener node has been started.')

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')

def main_talker(args=None):
    rclpy.init(args=args)
    talker = Talker()
    rclpy.spin(talker)
    talker.destroy_node()
    rclpy.shutdown()

def main_listener(args=None):
    rclpy.init(args=args)
    listener = Listener()
    rclpy.spin(listener)
    listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    # This block is for conceptual demonstration.
    # In a real scenario, you'd run these as separate ROS 2 nodes.
    print("Conceptual multi-node system demonstration:")
    print("To run in ROS 2, compile talker.py and listener.py as separate nodes and launch them.")
    print("\nSimulating separate processes (not actual ROS 2 communication in this script):")

    # This part is just to show the concepts in a single runnable script,
    # it does NOT replace actual ROS 2 multi-process communication.
    # For actual ROS 2, you'd build and run these nodes separately using 'ros2 run' or 'ros2 launch'.

    # You could technically run both in separate threads/processes from a single Python script
    # but that deviates from the standard ROS 2 way of running distinct nodes.
    # For simplicity, we just print a message here.

    # Example of how you would conceptually run them:
    # 1. Open Terminal 1: ros2 run my_package talker_node
    # 2. Open Terminal 2: ros2 run my_package listener_node
    pass
