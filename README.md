# catkin_clang_format
## Overview



## Usage
- add below in your package.xml

        <?xml version="1.0"?>
        <package>
          <!-- ... -->
          <build_depend>catkin_clang_format</build_depend>
        </package>

- add below in your CMakeLists.txt

        find_package(catkin_clang_format REQUIRED)
        include(${CMAKE_MODULE_PATH}/ClangFormatMacros.cmake)
        enable_clang_build()
        enable_clang_format()
        enable_clang_tidy()

