# Robot sim sensors

Collection of sensors to use in gazebo. This repo is ROS2 use.



Collection of all sensors
repo will be based on the robotnik_sensors [repo](https://github.com/RobotnikAutomation/robotnik_sensors)
- sensor on principle
    * monocamera
    * depthcam
    * 360° cam
    * 3Dlidar
    * 2Dlidar/laser
    * imu
    * GPS


* Parameters of the sensor
    - prefix
    - name
    - index
    - parent frame
    - * origin
        -   location (x,y,z)
        -   orientation 
    - update_rate /fps
    - enabled

    
camera specific sensors

lidar specific sensors
* range_min
* range_max
* hfov
* vfov
* nr of layers





