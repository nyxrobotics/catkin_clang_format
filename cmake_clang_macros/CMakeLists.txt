cmake_minimum_required(VERSION 2.8.3)
cmake_policy(SET CMP0054 NEW)
project(cmake_clang_macros)

find_package(catkin REQUIRED)

catkin_package(CFG_EXTRAS cmake_clang_macros-extras.cmake)

## Install all cmake files
install(DIRECTORY cmake/Modules
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/cmake)