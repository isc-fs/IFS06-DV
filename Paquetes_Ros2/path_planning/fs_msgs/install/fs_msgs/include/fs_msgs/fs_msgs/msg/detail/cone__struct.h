// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from fs_msgs:msg/Cone.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__CONE__STRUCT_H_
#define FS_MSGS__MSG__DETAIL__CONE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'BLUE'.
/**
  * Constants
 */
enum
{
  fs_msgs__msg__Cone__BLUE = 0
};

/// Constant 'YELLOW'.
enum
{
  fs_msgs__msg__Cone__YELLOW = 1
};

/// Constant 'ORANGE_BIG'.
enum
{
  fs_msgs__msg__Cone__ORANGE_BIG = 2
};

/// Constant 'ORANGE_SMALL'.
enum
{
  fs_msgs__msg__Cone__ORANGE_SMALL = 3
};

/// Constant 'UNKNOWN'.
enum
{
  fs_msgs__msg__Cone__UNKNOWN = 4
};

// Include directives for member types
// Member 'location'
#include "geometry_msgs/msg/detail/point__struct.h"

/// Struct defined in msg/Cone in the package fs_msgs.
typedef struct fs_msgs__msg__Cone
{
  /// x,y,z wrt to the car start location (origin)
  geometry_msgs__msg__Point location;
  /// use the enum below
  uint8_t color;
} fs_msgs__msg__Cone;

// Struct for a sequence of fs_msgs__msg__Cone.
typedef struct fs_msgs__msg__Cone__Sequence
{
  fs_msgs__msg__Cone * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fs_msgs__msg__Cone__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // FS_MSGS__MSG__DETAIL__CONE__STRUCT_H_
