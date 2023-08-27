from launch import LaunchDescription
import launch_ros.actions 


def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='ball_tracking_turtle',
            name='ball_animation',
            executable='ball_animation.py'
        ),
        
        launch_ros.actions.Node(
            package='ball_tracking_turtle',
            name='ball_animation',
            executable='ball_pose.py'
        )
    ])