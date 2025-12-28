---
sidebar_position: 1
title: URDF Modeling
---

# Chapter 3: URDF Modeling

URDF stands for **Unified Robot Description Format**. It is an XML file used to describe the physical structure of a robot.

## Elements of a URDF
1. **Links:** Represent the physical parts (chassis, wheels).
2. **Joints:** Represent how the links connect (fixed, revolute, continuous).

```xml
<link name="base_link">
  <visual>
    <geometry>
      <box size="0.6 0.4 0.2"/>
    </geometry>
  </visual>
</link>