cmake_minimum_required(VERSION 3.10)
project(warframe_market_recorder VERSION 0.0.1)

option(GEN_PROTO3 "generate the codes from proto3 files" ON)

set(WF_ITEMS_DIR "warframe-items")
# check warframe-items
if(NOT EXISTS "${WF_ITEMS_DIR}/" OR NOT EXISTS "${WF_ITEMS_DIR}/data/")
    message(FATAL_ERROR "submodule `warframe-items` not found")
endif()

# proto3
set(PROTO_DIR "proto3")
if(GEN_PROTO3)
    find_package(Protobuf REQUIRED)
    file(GLOB PROTO3_SRC "${PROTO_DIR}/*.proto3")
    add_custom_target(proto3_compile ALL
        COMMAND ${Protobuf_PROTOC_EXECUTABLE} -I ${CMAKE_SOURCE_DIR} --python_out=. ${PROTO3_SRC}
        DEPENDS ${PROTO3_SRC}
    )
    foreach(PROTO_FILE ${PROTO3_SRC})
        get_filename_component(PROTO_FILE_STEM ${PROTO_FILE} NAME_WE)
        set(INIT_FILE "${PROTO_DIR}/${PROTO_FILE_STEM}/__init__.py")
        add_custom_command(OUTPUT "${INIT_FILE}"
            COMMAND touch ${INIT_FILE}
            DEPENDS proto3_compile
        )
        add_custom_target(proto3_init_py_${PROTO_FILE_STEM} ALL
            DEPENDS "${INIT_FILE}"
        )
    endforeach()
endif()
