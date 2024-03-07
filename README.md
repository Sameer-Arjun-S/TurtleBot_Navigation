# ROS2_TurtleBot_Walker
 Walker algorithm inplementation in ROS2 on Turtlebot 
### Author
Sameer Arjun S

### Running the program
''
source /opt/ros/humble/setup.bash
export TURTLEBOT3_MODEL=burger
cd ros2_ws/src
''


Clone the repository using the command below. Use terminal in Ubuntu

git clone https://github.com/vinay06vinay/Turtlebot3-Obstacle-Avoidance-ROS2.git
cd ..

Run below commands to perform teleoperation

# Terminal 1
colcon build --packages-select obstacle_avoidance_tb3
source install/setup.bash
ros2 launch turtlebot3_gazebo turtlebot3_dqn_stage2.launch.py
# Terminal 2
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 run obstacle_avoidance_tb3 turtlebot_teleop.py

Run below commands to execute obstacle Avoidance algorithm

# Terminal 1
colcon build --packages-select obstacle_avoidance_tb3
source install/setup.bash
ros2 launch obstacle_avoidance_tb3 launch.py