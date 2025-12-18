# Quickstart: Research paper on Module 1: The Robotic Nervous System (ROS 2)

This quickstart guide provides the necessary steps to set up a ROS 2 environment to run the examples in the research paper.

## Prerequisites

-   **Operating System**: Ubuntu 22.04
-   **ROS 2**: ROS 2 Humble Hawksbill
-   **Python**: Python 3.11

## Installation

### 1. Install ROS 2 Humble

Follow the official ROS 2 Humble installation guide for Ubuntu:
[https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)

### 2. Set up your environment

Source the ROS 2 setup file in your `.bashrc`:
```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

### 3. Install `colcon`

`colcon` is a command line tool to build, test, and run ROS 2 packages.
```bash
sudo apt install python3-colcon-common-extensions
```

## Running the Examples

The research paper will include several hands-on examples. To run them, you will typically need to:

1.  Create a ROS 2 workspace:
    ```bash
    mkdir -p ~/ros2_ws/src
    cd ~/ros2_ws
    ```

2.  Create a new ROS 2 package for the example code.

3.  Copy the example code into the package.

4.  Build the workspace:
    ```bash
    colcon build
    ```

5.  Source the workspace setup file:
    ```bash
    source ~/ros2_ws/install/setup.bash
    ```

6.  Run the example node:
    ```bash
    ros2 run <package_name> <node_name>
    ```

Detailed instructions will be provided with each example in the paper.
