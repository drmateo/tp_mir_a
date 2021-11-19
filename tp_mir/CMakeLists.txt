cmake_minimum_required(VERSION 3.0.2)
project(tp_mir)

add_compile_options(-std=c++14)

find_package(catkin REQUIRED COMPONENTS
  niryo_one_python_api
  rospy
)

catkin_python_setup()
catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  scripts/control
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)