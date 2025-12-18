import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):

    def __init__(self):
        super().__init__('simple_publisher')
        # Create a publisher for the 'chatter' topic with String messages
        # and a queue size of 10
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.i = 0
        # Create a timer to publish messages every 0.5 seconds
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.get_logger().info('SimplePublisher node has been started.')

    def timer_callback(self, ):
        msg = String()
        msg.data = f'Hello ROS 2 World: {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args) # Initialize rclpy
    simple_publisher = SimplePublisher() # Create the node
    rclpy.spin(simple_publisher) # Keep the node alive until it's shutdown
    simple_publisher.destroy_node() # Destroy the node explicitly
    rclpy.shutdown() # Shutdown rclpy

if __name__ == '__main__':
    main()
