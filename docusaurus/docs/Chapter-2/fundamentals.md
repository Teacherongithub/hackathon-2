  ROS 2 Fundamentals: Architecture and rclpy

Learning Goal (User Story 1): A robotics student will read this chapter and understand ROS 2 architecture, middleware, and programming fundamentals with 'rclpy'. Mastering these concepts is foundational for all subsequent modules.

2.1 The Pillars of ROS 2 Architecture

The architecture of ROS 2 is defined by three fundamental communication concepts that enable distributed software execution:

   1-Nodes: These are the smallest, independent executable processes that perform a specific computational task (e.g., a simple motor speed controller or a dedicated object recognition algorithm). Every component of the robot's intelligence is encapsulated within a Node.
   2-Topics: These serve as the backbone for asynchronous data streaming. Data is published on a Topic by one Node and can be simultaneously received by any number of Subscriber Nodes. They are used for continuous, high-volume data like sensor readings or trajectory updates.
   3-Services: These establish a synchronous request/reply mechanism. Unlike Topics, Services are used when a Node needs a single, specific response (e.g., "Request the arm to move to pose X" and "Reply with confirmation").

2.2 Programming ROS 2 with rclpy

To bring these concepts to life, we rely on client libraries. rclpy is the Python client library for ROS 2, making it the preferred tool for rapid development and teaching due to Python's accessibility. The ability to write simple publisher and subscriber code in rclpy is 
a core learning objective.


(ACTION FOR YOU: Complete the main and if __name__ == '__main__' blocks and insert the corresponding Subscriber Node code. This code should illustrate how a Node publishes continuous data to a Topic, fulfilling the learning goal of understanding rclpy fundamentals.)
