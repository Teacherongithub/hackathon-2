---
id: workspace
title: Setting Up a ROS 2 Workspace
sidebar_label: Workspace
---

A ROS 2 workspace is a directory where you develop and build packages.

## Steps to Create a Workspace

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
