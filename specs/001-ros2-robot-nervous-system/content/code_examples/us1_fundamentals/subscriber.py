import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimpleSubscriber(Node):

    def __init__(self):
        super().__init__('simple_subscriber')
        # Create a subscriber for the 'chatter' topic with String messages
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.listener_callback,
            10)
        self.subscription # prevent unused variable warning
        self.get_logger().info('SimpleSubscriber node has been started.')

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args) # Initialize rclpy
    simple_subscriber = SimpleSubscriber() # Create the node
    rclpy.spin(simple_subscriber) # Keep the node alive until it's shutdown
    simple_subscriber.destroy_node() # Destroy the node explicitly
    rclpy.shutdown() # Shutdown rclpy

if __name__ == '__main__':
    main()
