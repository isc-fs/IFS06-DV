// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from fs_msgs:msg/Track.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__TRACK__STRUCT_H_
#define FS_MSGS__MSG__DETAIL__TRACK__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'track'
#include "fs_msgs/msg/detail/cone__struct.h"

/// Struct defined in msg/Track in the package fs_msgs.
typedef struct fs_msgs__msg__Track
{
  fs_msgs__msg__Cone__Sequence track;
} fs_msgs__msg__Track;

// Struct for a sequence of fs_msgs__msg__Track.
typedef struct fs_msgs__msg__Track__Sequence
{
  fs_msgs__msg__Track * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fs_msgs__msg__Track__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // FS_MSGS__MSG__DETAIL__TRACK__STRUCT_H_
