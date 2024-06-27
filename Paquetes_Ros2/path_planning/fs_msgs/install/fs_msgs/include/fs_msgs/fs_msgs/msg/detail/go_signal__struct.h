// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from fs_msgs:msg/GoSignal.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__GO_SIGNAL__STRUCT_H_
#define FS_MSGS__MSG__DETAIL__GO_SIGNAL__STRUCT_H_

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
// Member 'mission'
// Member 'track'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/GoSignal in the package fs_msgs.
typedef struct fs_msgs__msg__GoSignal
{
  std_msgs__msg__Header header;
  rosidl_runtime_c__String mission;
  rosidl_runtime_c__String track;
} fs_msgs__msg__GoSignal;

// Struct for a sequence of fs_msgs__msg__GoSignal.
typedef struct fs_msgs__msg__GoSignal__Sequence
{
  fs_msgs__msg__GoSignal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fs_msgs__msg__GoSignal__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // FS_MSGS__MSG__DETAIL__GO_SIGNAL__STRUCT_H_
