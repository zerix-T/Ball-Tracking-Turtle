#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from turtlesim.msg import Pose
from cv_bridge import CvBridge, CvBridgeError
import cv2

class posePublisher(Node):
    def __init__(self):
        super().__init__("pose_publisher")
        self.pub = self.create_publisher(Pose, '/turtle/move_pose', 10)
        self.sub = self.create_subscription(Image, '/image/ball_animation', self.frame_callback, 1)


    def frame_callback(self, data):
        try:
            bridge = CvBridge()
            self.frame = bridge.imgmsg_to_cv2(data, "bgr8")
            self.showImage()

        except CvBridgeError as e:
            print(e)
            return
        
    def showImage(self):
        self.new_frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.gray = cv2.cvtColor(self.new_frame, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(self.gray, 30, 200)
        p = Pose()
        
        # cv2.imshow('gray', self.gray)
        
        _, binary = cv2.threshold(self.gray, 1, 255, cv2.THRESH_OTSU)
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        img = cv2.drawContours(self.new_frame, contours, 1, (255,0,0), 3)
        cnt = contours[1]
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        
        # h,w = img.shape[:2]
        # print("frame size is : ({}, {})".format(h, w))
        
        cv2.imshow("output", img)
        
        
        cx = (cx*11)/500
        cy = (cy*11)/500
        cy = 11 - cy
        
        p.x = cx
        p.y = cy
        
        if cx>=11 or cy>=11:
            print("Oops error happened")
        self.pub.publish(p)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.release()
            cv2.destroyAllWindows()
            
            
def main(args=None):
    rclpy.init(args=args)
    
    pose_pub = posePublisher()
    
    rclpy.spin(pose_pub)
    pose_pub.destroy_node()
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()