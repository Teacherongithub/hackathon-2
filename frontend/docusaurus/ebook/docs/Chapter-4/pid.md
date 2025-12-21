 # Basic Control, Integration, and Debugging

**Learning Goal (User Story 3 & 4):**  
A student/developer will be able to implement basic ROS 2 robot control using provided examples, and understand how to integrate multiple ROS 2 nodes and debug common issues.

---

## 4.1 Implementing Basic Robot Control

The most fundamental task in robotics is controlling movement. Once the `rclpy` fundamentals are understood, the focus shifts to publishing data that affects the robot's physical state.

For simple mobile movement, control is often achieved by publishing a `geometry_msgs/Twist` message to a designated velocity topic. This message contains two vectors:

- **Linear velocity** (how fast and in which direction to move)
- **Angular velocity** (how fast to rotate)

> **Action for the learner:**  
> Insert a simple `rclpy` publisher code block here that publishes a constant `Twist` message to make a robot move forward. This directly addresses the goal of implementing basic control.

---

## 4.2 Integrating Multi-Node Systems

A realistic humanoid robot system involves numerous ROS 2 Nodes working together. The successful integration of multiple nodes depends on strict adherence to Topic and Message standards:

1. **Topic Consistency**  
   Every component that needs a piece of data must subscribe to the **exact topic name** being published. Misspellings are the most common integration error.

2. **Message Type Agreement**  
   The communicating Nodes must agree on the format of the data. For example:
   - An image processing node publishes `sensor_msgs/Image`
   - The computer vision node must be prepared to receive `sensor_msgs/Image`

Understanding this integration structure allows developers to move toward real-world robot control problems.

---

## 4.3 Debugging Common ROS 2 Issues

Debugging is a required skill for any developer, especially when integrating multiple ROS 2 nodes. When a system fails, the problem is often related to **communication**, not necessarily logic.

Here are the core command-line tools used for diagnosis:

- **`ros2 node list`**  
  Use this command to verify that all necessary Nodes (sensor drivers, motor controllers, etc.) are running. If a Node is missing, the system will not function correctly.

- **`ros2 topic info <topic_name>`**  
  Use this command to check whether a specific Topic is active and confirm that both a Publisher and a Subscriber are correctly connected.

- **`ros2 topic echo <topic_name>`**  
  This tool allows you to inspect the data stream in real time. If data is flowing but incorrect (for example, publishing `0.0` when it should be `1.0`), the issue lies within the Node’s internal logic.
