  # URDF for Humanoid Robot Modeling

**Learning Goal (User Story 2):**  
A robotics developer will learn to use URDF for modeling humanoid robot joints, links, and sensors. This is considered essential for practical humanoid robotics development.

---

## 3.1 The Need for a Standardized Model

Before any control code is written in `rclpy`, the robot's physical form must be defined. This is crucial for visualization, simulation, and calculating the complex movements inherent in humanoid robotics.

The tool used for this purpose is **URDF (Unified Robot Description Format)**, which is an XML-based format for robot modeling, including links, joints, and sensors.

URDF files define the robot's structure, including:

- The exact physical dimensions (mass, volume, shape) of every body segment  
- The connection points and limits of every joint  
- The precise location of sensors  

This comprehensive model is read by the ROS 2 system, which uses it to inform kinematic solvers and visualization tools. This allows developers to see and test their code in a simulated environment before deploying it to physical hardware.

---

## 3.2 Defining the Physical Structure

URDF models are constructed using two main XML tags:

1. **`<link>`**  
   Represents a rigid physical part of the robot, such as a torso, a hand, or a segment of a leg.  
   Each link is modeled with:
   - Inertia (how difficult it is to move)
   - Visual geometry (what it looks like)
   - Collision geometry (used for physics calculations)

2. **`<joint>`**  
   Represents the physical connection and the type of motion allowed between two links (a parent link and a child link).  
   Common joint types include:
   - `revolute` (rotational movement, like an elbow)
   - `fixed` (no movement, such as a sensor mount)

---

## 3.3 URDF Modeling Example

The following example demonstrates a simple `revolute` joint connecting two links.  
Creating a basic URDF model like this is a core skill in humanoid robot modeling.

```xml
<robot name="robot_model">

  <link name="base_link">
  </link>

  <link name="upper_arm_link">
  </link>

  <joint name="shoulder_joint" type="revolute">
    <parent link="base_link"/>
    <child link="upper_arm_link"/>
    <axis xyz="0 1 0"/>
    <limit effort="100" velocity="1" lower="-2.0" upper="2.0"/>
  </joint>

</robot>
