---
sidebar_position: 1
title: ROS 2 Fundamentals
---

# Chapter 2: ROS 2 Fundamentals

ROS 2 (Robot Operating System) is not an actual operating system, but a middleware framework.

## Core Concepts
* **Nodes:** A single process performing a task.
* **Topics:** A bus over which nodes exchange messages.
* **Messages:** The data structure used when subscribing or publishing to a topic.

### The ROS 2 Graph
The Graph is a network of nodes and the connections between them. This allows different parts of a robot (like sensors and motors) to talk to each other.