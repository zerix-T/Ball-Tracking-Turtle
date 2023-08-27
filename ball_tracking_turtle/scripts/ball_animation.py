#!/usr/bin/env python3
import os
import rclpy
import ament_index_python
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2


class framePublisher(Node):
    def __init__(self):
        super().__init__('frame_publisher')
        self.bridge = CvBridge()
        
        share_directory = ament_index_python.get_package_share_directory('ball_tracking_turtle')
        vid_path = share_directory + "/resource/moving_ball.avi"

        self.video = cv2.VideoCapture(vid_path)
        self.pub = self.create_publisher(Image, '/image/ball_animation', 1)
        self.get_logger().info("Publishing ball frames.....")
        self.callback()


    def callback(self):
        frame_counter = 0
        while rclpy.ok():
            r, frame = self.video.read()
            if not r:break
            frame_counter+=1

            if frame_counter == self.video.get(cv2.CAP_PROP_FRAME_COUNT):
                frame_counter = 0
                self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            
            msg = self.bridge.cv2_to_imgmsg(frame, "bgr8")
            self.pub.publish(msg)
            

            if cv2.waitKey(1) & 0xFF == ord('m'):
                break

def main(args=None):
    rclpy.init(args=args)
    frame_pub = framePublisher()
    rclpy.spin(frame_pub)

    frame_pub.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()


