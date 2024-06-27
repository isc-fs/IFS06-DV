# generated from
# rosidl_cmake/cmake/template/rosidl_cmake_export_typesupport_targets.cmake.in

set(_exported_typesupport_targets
  "__rosidl_generator_c:fs_msgs__rosidl_generator_c;__rosidl_typesupport_fastrtps_c:fs_msgs__rosidl_typesupport_fastrtps_c;__rosidl_generator_cpp:fs_msgs__rosidl_generator_cpp;__rosidl_typesupport_fastrtps_cpp:fs_msgs__rosidl_typesupport_fastrtps_cpp;__rosidl_typesupport_introspection_c:fs_msgs__rosidl_typesupport_introspection_c;__rosidl_typesupport_c:fs_msgs__rosidl_typesupport_c;__rosidl_typesupport_introspection_cpp:fs_msgs__rosidl_typesupport_introspection_cpp;__rosidl_typesupport_cpp:fs_msgs__rosidl_typesupport_cpp;__rosidl_generator_py:fs_msgs__rosidl_generator_py")

# populate fs_msgs_TARGETS_<suffix>
if(NOT _exported_typesupport_targets STREQUAL "")
  # loop over typesupport targets
  foreach(_tuple ${_exported_typesupport_targets})
    string(REPLACE ":" ";" _tuple "${_tuple}")
    list(GET _tuple 0 _suffix)
    list(GET _tuple 1 _target)

    set(_target "fs_msgs::${_target}")
    if(NOT TARGET "${_target}")
      # the exported target must exist
      message(WARNING "Package 'fs_msgs' exports the typesupport target '${_target}' which doesn't exist")
    else()
      list(APPEND fs_msgs_TARGETS${_suffix} "${_target}")
    endif()
  endforeach()
endif()
