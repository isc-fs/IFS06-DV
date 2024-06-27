// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from fs_msgs:msg/FinishedSignal.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__FINISHED_SIGNAL__STRUCT_H_
#define FS_MSGS__MSG__DETAIL__FINISHED_SIGNAL__STRUCT_H_

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

/// Struct defined in msg/FinishedSignal in the package fs_msgs.
typedef struct fs_msgs__msg__FinishedSignal
{
  std_msgs__msg__Header header;
  bool placeholder;
} fs_msgs__msg__FinishedSignal;

// Struct for a sequence of fs_msgs__msg__FinishedSignal.
typedef struct fs_msgs__msg__FinishedSignal__Sequence
{
  fs_msgs__msg__FinishedSignal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fs_msgs__msg__FinishedSignal__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // FS_MSGS__MSG__DETAIL__FINISHED_SIGNAL__STRUCT_H_
