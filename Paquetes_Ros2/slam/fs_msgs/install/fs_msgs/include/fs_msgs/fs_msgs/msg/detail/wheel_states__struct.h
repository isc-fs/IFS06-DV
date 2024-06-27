// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from fs_msgs:msg/WheelStates.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__WHEEL_STATES__STRUCT_H_
#define FS_MSGS__MSG__DETAIL__WHEEL_STATES__STRUCT_H_

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

/// Struct defined in msg/WheelStates in the package fs_msgs.
typedef struct fs_msgs__msg__WheelStates
{
  std_msgs__msg__Header header;
  float fl_rpm;
  float fr_rpm;
  float rl_rpm;
  float rr_rpm;
  float fl_rotation_angle;
  float fr_rotation_angle;
  float rl_rotation_angle;
  float rr_rotation_angle;
  float fl_steering_angle;
  float fr_steering_angle;
  float rl_steering_angle;
  float rr_steering_angle;
} fs_msgs__msg__WheelStates;

// Struct for a sequence of fs_msgs__msg__WheelStates.
typedef struct fs_msgs__msg__WheelStates__Sequence
{
  fs_msgs__msg__WheelStates * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fs_msgs__msg__WheelStates__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // FS_MSGS__MSG__DETAIL__WHEEL_STATES__STRUCT_H_
