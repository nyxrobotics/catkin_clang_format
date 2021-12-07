# catkin_clang_format
## Overview
This package provides CMake macros of formatting C++ sources and headers with clang-tidy and clang-format.


## Setup
- install clang packages

        sudo apt install clang-8 clang-format-8 clang-tidy-8 clang-tools-8

- clone this ros package into your catkin workspace

        cd path-to-your-catkin-workspace
        git clone https://github.com/nyxrobotics/catkin_clang_format.git
        cd catkin_clang_format/cmake_clang_macros

- copy .clang-format and .clang-tidy to your catkin workspace

        cp ./config/.clang-* path-to-your-catkin-workspace

## Usage
- add below in your package.xml

        <?xml version="1.0"?>
        <package>
          <!-- ... -->
          <build_depend>catkin_clang_format</build_depend>
        </package>

- add below in your CMakeLists.txt

        find_package(cmake_clang_macros REQUIRED)
        include(${CMAKE_MODULE_PATH}/ClangFormatMacros.cmake)
        enable_clang_build()
        enable_clang_format()
        enable_clang_tidy()


## References
- Apply clang-format and clang-tidy from cmake (Japanese blog) : https://qiita.com/tenmyo/items/f8548ee9bab78f18cd25
- How to export cmake modules with ros package : https://github.com/ros/cmake_modules  
- .clang-format settings for ROS package : https://github.com/davetcoleman/roscpp_code_format  
- .clang-tidy settings for ROS package : https://github.com/ros-planning/moveit/blob/master/.clang-tidy  