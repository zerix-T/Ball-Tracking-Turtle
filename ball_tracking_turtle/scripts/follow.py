#!/usr/bin/env python
import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute
from turtlesim.msg import Pose
from std_srvs.srv import Empty as EmptyServiceCall
from math import atan2, sqrt, pow

class followTurtle(Node):
    def __init__(self):
        super().__init__('follow_turtle')
        self.move_turtle1 = self.create_client(TeleportAbsolute, "/turtle1/teleport_absolute")
        self.x0 = 5.5444
        self.y0 = 5.5444
        
        self.sub_0 = self.create_subscription(Pose, "/turtle/move_pose", self.final_callback, 10)
        
    def final_callback(self, data):
        x = round(data.x, 4)
        y = round(data.y, 4)
        
        if (sqrt(pow((x-self.x0), 2)) + pow((y - self.y0), 2)) < 2:
            theta = atan2(y-self.y0, x-self.x0)
            req = TeleportAbsolute.Request()
            req.x = x
            req.y = y
            req.theta = theta
            
            print("sending pose : {}, {}, {}".format(x, y, theta))
            
            while not self.move_turtle1.wait_for_service(timeout_sec=1.0):
                self.get_logger().info('service not available, waiting again...')
                
            self.move_turtle1.call_async(req)
            self.x0 = x
            self.y0 = y
            
def main(args=None):
    rclpy.init(args=args)
    
    f_pub = followTurtle()
    rclpy.spin(f_pub)
    f_pub.destroy_node()
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()
        