cmake_minimum_required(VERSION 3.6.1)

project(inlab5-files)
add_executable(helloworld helloworld.cpp)
add_executable(usespthread usespthread.cpp)

target_link_libraries(usespthread -lpthread)

add_library(MyEngineStatic STATIC myengine/myengine.hpp myengine/myengine.cpp)
add_library(MyEngineDynamic SHARED myengine/myengine.hpp myengine/myengine.cpp)

install(TARGETS MyEngineStatic MyEngineDynamic DESTINATION /usr/local/lib)
install(FILES myengine/myengine.hpp DESTINATION /usr/local/include) 
