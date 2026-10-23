# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0 OR MIT
# --------------------------------------------------------------------------------------------------
cmake_minimum_required(VERSION 3.12)
project(test_lyra LANGUAGES CXX)

find_package(Lyra CONFIG REQUIRED)

add_executable(test_lyra main.cpp)
target_link_libraries(test_lyra PRIVATE bfg::Lyra)
