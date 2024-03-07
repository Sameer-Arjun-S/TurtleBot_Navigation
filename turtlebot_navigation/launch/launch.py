# Importing the necessary libraries
import os
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument,IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    #args_record_topics = DeclareLaunchArgument('record_topics', default_value='False', choices=['True', 'False'])  
    navigation_node = Node(
            package='turtlebot_navigation',
            executable='obs_avoid.py',
            name='navigation'
        )
    gazebo_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch'),
                                      '/turtlebot3_world.launch.py'])
    )
    
    return LaunchDescription([
        gazebo_world,
        navigation_node
    ])