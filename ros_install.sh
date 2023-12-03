#!/bin/bash
set -e
# sudo apt update -y && sudo apt install -y curl gnupg2 lsb-release
# sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg
# echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
# cd ~/Downloads
# wget -O ros2-iron-20231120-linux-jammy-amd64.tar.bz2 https://github.com/ros2/ros2/releases/download/release-iron-20231120/ros2-iron-20231120-linux-jammy-amd64.tar.bz2
# mkdir -p ~/ros2_dashing
cd ~/ros2_dashing
# tar xvf ~/Downloads/ros2-iron-20231120-linux-jammy-amd64.tar.bz2
# sudo apt update -y
sudo apt install -y python3-rosdep2
sudo rosdep init
rosdep update
rosdep update --include-eol-distros
rosdep install --from-paths ~/ros2_dashing/ros2-linux/share --ignore-src --rosdistro iron -y --skip-keys "console_bridge fastcdr fastrtps libopensplice67 libopensplice69 osrf_testing_tools_cpp poco_vendor rmw_connext_cpp rosidl_typesupport_connext_c rosidl_typesupport_connext_cpp rti-connext-dds-5.3.1 tinyxml_vendor tinyxml2_vendor urdfdom urdfdom_headers" --os=ubuntu:focal
sudo apt install -y libpython3-dev python3-pip
pip3 install -U argcomplete
