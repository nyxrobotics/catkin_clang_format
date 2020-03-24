# catkin_clang_format
## Overview



## Usage
- add below in your package.xml

        <?xml version="1.0"?>
        <package>
          <!-- ... -->
          <build_depend>cmake_modules</build_depend>
        </package>

- add below in your CMakeLists.txt

        find_package(catkin_clang_format REQUIRED)
        enable_clang_build()
        clang_format_fix()
        clang_tidy_fix()

