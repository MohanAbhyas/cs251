cmake_minimum_required(VERSION 3.6.1)

project(${CMAKE_CURRENT_SOURCE_DIR})
add_executable(helloworld helloworld.cpp)
add_executable(usespthread usespthread.cpp)

target_link_libraries(usespthread -lpthread)

add_library(MyEngineStatic STATIC myengine/myengine.hpp myengine/myengine.cpp)
add_library(MyEngineDynamic SHARED myengine/myengine.hpp myengine/myengine.cpp)

install(TARGETS MyEngineStatic MyEngineDynamic DESTINATION lib)
install(FILES myengine/myengine.hpp DESTINATION include) 
