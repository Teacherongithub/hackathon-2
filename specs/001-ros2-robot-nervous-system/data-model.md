# Data Model: Research paper on Module 1: The Robotic Nervous System (ROS 2)

This document outlines the key entities and concepts that will be covered in the research paper.

## Key Entities

### 1. ROS 2
- **Description**: The core framework for robotics development.
- **Attributes**:
    - Open-source
    - Middleware for robotics
    - Community-supported

### 2. DDS (Data Distribution Service)
- **Description**: The middleware underlying ROS 2 communication.
- **Attributes**:
    - Real-time data sharing
    - Decoupled communication
    - Quality of Service (QoS) policies

### 3. ROS 2 Node
- **Description**: A process that performs a specific task in a ROS 2 system.
- **Attributes**:
    - Can be a publisher, subscriber, service client, or service server.
    - Can be written in Python (`rclpy`) or C++.

### 4. ROS 2 Topic
- **Description**: A named bus over which nodes exchange messages.
- **Attributes**:
    - Unidirectional communication
    - Many-to-many communication

### 5. ROS 2 Service
- **Description**: A request-response communication pattern.
- **Attributes**:
    - Bidirectional communication
    - One-to-one communication

### 6. `rclpy`
- **Description**: The Python client library for ROS 2.
- **Attributes**:
    - Provides a Pythonic interface to the ROS 2 C++ libraries.
    - Used to write ROS 2 nodes in Python.

### 7. URDF (Unified Robot Description Format)
- **Description**: An XML format for representing a robot model.
- **Attributes**:
    - Defines the robot's links, joints, and sensors.
    - Used by ROS 2 for robot visualization and simulation.

## Relationships

- A **ROS 2 System** is composed of one or more **ROS 2 Nodes**.
- **ROS 2 Nodes** communicate with each other using **ROS 2 Topics** and **ROS 2 Services**.
- **DDS** is the underlying middleware that enables this communication.
- **`rclpy`** is used to write **ROS 2 Nodes** in Python.
- **URDF** is used to describe the physical structure of the robot that the **ROS 2 Nodes** control.
