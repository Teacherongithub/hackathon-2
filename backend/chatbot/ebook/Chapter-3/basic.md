 # URDF for Humanoid Robot Modeling

**Learning Goal (User Story 2):**  
A robotics developer will learn to use URDF for modeling humanoid robot joints, links, and sensors. This is considered essential for practical humanoid robotics development.

---

## 3.1 The Need for a Standardized Model

Before any control code is written in `rclpy`, the robot's physical form must be defined. This is crucial for visualization, simulation, and calculating the complex movements inherent in Humanoid Robotics.

The tool used for this is **URDF (Unified Robot Description Format)**, which is the XML format for robot modeling (links, joints, sensors).

URDF files define the robot's structure, including:

- The exact physical dimensions (mass, volume, shape) of every body segment  
- The connection points and limits of every `joint`  
- The precise location of sensors  

This comprehensive model is read by the ROS 2 system, which uses it to inform kinematic solvers and visualization tools, allowing developers to see and test their code in a simulated environment before deploying it to the physical hardware.

---

## 3.2 Defining the Physical Structure

URDF models are constructed using two main XML tags:

1. **`<link>`**  
   Represents a rigid physical part of the robot, such as a torso, a hand, or a segment of a leg. Each link is modeled with:
   - Inertia (how difficult it is to move)
   - Visual geometry (what it looks like)
   - Collision geometry (its shape for physics calculations)

2. **`<joint>`**  
   Represents the physical connection and type of motion allowed between two links (a parent link and a child link). Common joint types include:
   - `revolute` (rotation, like an elbow)
   - `fixed` (no movement, like a sensor mount)

---

## 3.3 URDF Modeling Example

The following example illustrates a simple revolute joint connecting two links. The developer's ability to create a basic URDF model for a simple robotic arm is a core test of this knowledge.

XML

<robot name="robot_model">
  <link name="base_link">
    </link>


  <joint name="shoulder_joint" type="revolute">
    <parent link="base_link"/>
    <child link="upper_arm_link"/>
    <axis xyz="0 1 0"/> <limit effort="100" velocity="1" lower="-2.0" upper="2.0"/> </joint>


  <link name="upper_arm_link">
    </link>
</robot>


The joint publishes its state on a ROS topic identified by a `topic_name`.

> **Action for the learner:**  
> Review the URDF code example to ensure all XML tags such as `<link>` and `<joint>` are correctly opened and closed for direct use in a `.urdf` file.
