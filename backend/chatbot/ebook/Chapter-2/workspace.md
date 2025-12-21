### `docs/chapter2/workspace.md`
```markdown
---
id: chapter2/workspace
title: Setting Up a ROS 2 Workspace
sidebar_label: Workspace
---

# Chapter 2: Setting Up Your ROS 2 Workspace

A ROS 2 workspace is a directory where you develop and build packages.

<grok-card data-id="b00e82" data-type="image_card"></grok-card>


## Steps to Create a Workspace
```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
