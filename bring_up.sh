#!/bin/bash

ROS_MASTER_URI=http://10.10.10.10:11311
ROS_IP=10.10.10.55

docker run --rm --privileged \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  --mount type=bind,source="$(pwd)"/src,target=/home/docker/catkin_ws_tp_mir/src\
  -e DISPLAY=${DISPLAY} -e ROS_MASTER_URI=$ROS_MASTER_URI -e ROS_IP=$ROS_IP \
  --network host \
  --name tp_mir \
  drmateo/tp_iit:niryo-kinetic \
  bash -c 'echo "docker" | sudo -S chown -R 1000:1000 /home/docker/catkin_ws_tp_mir && tail -F /dev/null'