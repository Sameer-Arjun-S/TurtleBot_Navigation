# TurtleBot Navigation
Navigation and obstacle avoidance implemented on TurtleBot3

### Author
Sameer Arjun S

### Running the program

#### Setting up the environment for Ubuntu 22 and ROS2
```
source /opt/ros/humble/setup.bash
export TURTLEBOT3_MODEL=burger
cd ros2_ws/src
```

#### Cloning the repositiory
```
git clone https://github.com/Sameer-Arjun-S/TurtleBot_Navigation.git
cd ..
```
#### Running teleoperation program
##### Terminal 1
```
colcon build --packages-select turtlebot_navigation
source install/setup.bash
ros2 ros2 launch turtlebot3_gazebo empty_world.launch.py 
```
##### Terminal 2
```
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 run turtlebot_navigation teleop.py
```
#### Running obstacle avoidance program
```
colcon build --packages-select turtlebot_navigation
source install/setup.bash
ros2 launch turtlebot_navigation launch.py
```
