cmake_minimum_required(VERSION 2.8.3)
cmake_policy(SET CMP0054 NEW)
project(catkin_format)

find_package(catkin REQUIRED rospy)
catkin_python_setup()
catkin_package()
# catkin_package(CFG_EXTRAS catkin_format-extras.cmake)
include_directories(${catkin_INCLUDE_DIRS})

## Install all cmake files
# install(DIRECTORY cmake/Modules
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/cmake)
# install(PROGRAMS
#    scripts/catkin_format/__init__.py
#    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

catkin_install_python(PROGRAMS src/catkin_format/__init__.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
