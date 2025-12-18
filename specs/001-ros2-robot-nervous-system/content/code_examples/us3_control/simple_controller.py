import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64 # Assuming we control joint position with a float

class SimpleJointController(Node):

    def __init__(self):
        super().__init__('simple_joint_controller')
        self.publisher_ = self.create_publisher(Float64, '/joint_command', 10)
        self.joint_positions = [0.0, 0.5, 1.0, 0.5, 0.0] # Example target positions in radians
        self.current_position_idx = 0
        self.timer = self.create_timer(2.0, self.timer_callback) # Cycle every 2 seconds
        self.get_logger().info('SimpleJointController node has been started.')

    def timer_callback(self):
        msg = Float64()
        msg.data = self.joint_positions[self.current_position_idx]
        self.publisher_.publish(msg)
        self.get_logger().info(f'Commanding joint to: {msg.data} radians')
        self.current_position_idx = (self.current_position_idx + 1) % len(self.joint_positions)

def main(args=None):
    rclpy.init(args=args)
    simple_joint_controller = SimpleJointController()
    rclpy.spin(simple_joint_controller)
    simple_joint_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
