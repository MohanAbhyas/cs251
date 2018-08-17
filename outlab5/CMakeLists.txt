cmake_minimum_required(VERSION 3.6.1)

project(inlab5-files)
file (GLOB *)
set(SOURCE1 ${CMAKE_CURRENT_SOURCE_DIR}/myengine/myengine.hpp)
set(SOURCE2 ${CMAKE_CURRENT_SOURCE_DIR}/myengine/myengine.cpp)
add_executable(helloworld helloworld.cpp)
add_executable(usespthread usespthread.cpp)

target_link_libraries(usespthread -lpthread)

add_library(MyEngineStatic STATIC ${SOURCE1} ${SOURCE2})
add_library(MyEngineDynamic SHARED ${SOURCE1} ${SOURCE2})

install(TARGETS MyEngineStatic MyEngineDynamic DESTINATION /usr/local/lib)
install(FILES myengine.hpp DESTINATION /usr/local/include) 
