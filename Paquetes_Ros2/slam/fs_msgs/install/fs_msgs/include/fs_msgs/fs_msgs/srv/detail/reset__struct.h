// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from fs_msgs:srv/Reset.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__SRV__DETAIL__RESET__STRUCT_H_
#define FS_MSGS__SRV__DETAIL__RESET__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/Reset in the package fs_msgs.
typedef struct fs_msgs__srv__Reset_Request
{
  bool wait_on_last_task;
} fs_msgs__srv__Reset_Request;

// Struct for a sequence of fs_msgs__srv__Reset_Request.
typedef struct fs_msgs__srv__Reset_Request__Sequence
{
  fs_msgs__srv__Reset_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fs_msgs__srv__Reset_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Reset in the package fs_msgs.
typedef struct fs_msgs__srv__Reset_Response
{
  uint8_t structure_needs_at_least_one_member;
} fs_msgs__srv__Reset_Response;

// Struct for a sequence of fs_msgs__srv__Reset_Response.
typedef struct fs_msgs__srv__Reset_Response__Sequence
{
  fs_msgs__srv__Reset_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fs_msgs__srv__Reset_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // FS_MSGS__SRV__DETAIL__RESET__STRUCT_H_
