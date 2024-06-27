// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from fs_msgs:msg/ControlCommand.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__CONTROL_COMMAND__STRUCT_H_
#define FS_MSGS__MSG__DETAIL__CONTROL_COMMAND__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

/// Struct defined in msg/ControlCommand in the package fs_msgs.
typedef struct fs_msgs__msg__ControlCommand
{
  std_msgs__msg__Header header;
  /// range : (0, 1)
  double throttle;
  /// range : (-1, 1)
  double steering;
  /// # range : (0, 1)
  double brake;
} fs_msgs__msg__ControlCommand;

// Struct for a sequence of fs_msgs__msg__ControlCommand.
typedef struct fs_msgs__msg__ControlCommand__Sequence
{
  fs_msgs__msg__ControlCommand * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fs_msgs__msg__ControlCommand__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // FS_MSGS__MSG__DETAIL__CONTROL_COMMAND__STRUCT_H_
