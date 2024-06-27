// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from fs_msgs:msg/ExtraInfo.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__EXTRA_INFO__STRUCT_H_
#define FS_MSGS__MSG__DETAIL__EXTRA_INFO__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'laps'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in msg/ExtraInfo in the package fs_msgs.
/**
  * The number of Down Or Out cones during the run
 */
typedef struct fs_msgs__msg__ExtraInfo
{
  uint32_t doo_counter;
  /// The number of finished laps driven by the vehicle
  rosidl_runtime_c__float__Sequence laps;
} fs_msgs__msg__ExtraInfo;

// Struct for a sequence of fs_msgs__msg__ExtraInfo.
typedef struct fs_msgs__msg__ExtraInfo__Sequence
{
  fs_msgs__msg__ExtraInfo * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fs_msgs__msg__ExtraInfo__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // FS_MSGS__MSG__DETAIL__EXTRA_INFO__STRUCT_H_
