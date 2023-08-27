from launch import LaunchDescription
import launch_ros.actions 


def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='turtlesim',
            name='turtle',
            executable='turtlesim_node'
        ),
        
        launch_ros.actions.Node(
            package='ball_tracking_turtle',
            name='ball_animation',
            executable='follow.py'
        )
    ])