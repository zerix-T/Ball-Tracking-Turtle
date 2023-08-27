#Ball Tracking Turtle

The turtle in turtlesim follows the track of a ball moving in a clip. Turtle mimicking of a ball movement is basically grabbing the pose of the ball and calling turtle service to follow that pose. 

There are ***Five*** scripts in this package :
- creat_moving_ball.py : creates a video file with moving ball.
- ball_animation.py : publishes all frames of moving_ball video in a loop.
- ball_pose.py : gets frames from above node and publishes the pose of the moving ball.
- follow.py : gets pose from above node and calls turtlesim serive to teleport the turtle to the given pose.


##Usage
Clone the repo in src folder of your ros2 workspace. Build the package, source the package,

In first terminal:

```bash
source install/setup.bash
```

```bash
ros2 launch ball_tracking_turtle moving_ball.launch.py
```

In second terminal:

```bash
ros2 launch ball_tracking_turtle go_turtle.launch.py
```