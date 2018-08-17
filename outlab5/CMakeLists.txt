cmake_minimum_required(VERSION 3.6.1)

project(mygame)

add_executable(mygamestatic mygame.cpp)
target_link_libraries(mygamestatic MyEngineStatic)

add_executable(mygamedynamic mygame.cpp)
target_link_libraries(mygamedynamic MyEngineDynamic)
