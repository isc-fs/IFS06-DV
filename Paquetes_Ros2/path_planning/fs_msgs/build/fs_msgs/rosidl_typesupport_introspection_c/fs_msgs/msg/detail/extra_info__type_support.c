// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from fs_msgs:msg/ExtraInfo.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "fs_msgs/msg/detail/extra_info__rosidl_typesupport_introspection_c.h"
#include "fs_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "fs_msgs/msg/detail/extra_info__functions.h"
#include "fs_msgs/msg/detail/extra_info__struct.h"


// Include directives for member types
// Member `laps`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__ExtraInfo_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  fs_msgs__msg__ExtraInfo__init(message_memory);
}

void fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__ExtraInfo_fini_function(void * message_memory)
{
  fs_msgs__msg__ExtraInfo__fini(message_memory);
}

size_t fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__size_function__ExtraInfo__laps(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__get_const_function__ExtraInfo__laps(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__get_function__ExtraInfo__laps(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__fetch_function__ExtraInfo__laps(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__get_const_function__ExtraInfo__laps(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__assign_function__ExtraInfo__laps(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__get_function__ExtraInfo__laps(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__resize_function__ExtraInfo__laps(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__ExtraInfo_message_member_array[2] = {
  {
    "doo_counter",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(fs_msgs__msg__ExtraInfo, doo_counter),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "laps",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(fs_msgs__msg__ExtraInfo, laps),  // bytes offset in struct
    NULL,  // default value
    fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__size_function__ExtraInfo__laps,  // size() function pointer
    fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__get_const_function__ExtraInfo__laps,  // get_const(index) function pointer
    fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__get_function__ExtraInfo__laps,  // get(index) function pointer
    fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__fetch_function__ExtraInfo__laps,  // fetch(index, &value) function pointer
    fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__assign_function__ExtraInfo__laps,  // assign(index, value) function pointer
    fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__resize_function__ExtraInfo__laps  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__ExtraInfo_message_members = {
  "fs_msgs__msg",  // message namespace
  "ExtraInfo",  // message name
  2,  // number of fields
  sizeof(fs_msgs__msg__ExtraInfo),
  fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__ExtraInfo_message_member_array,  // message members
  fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__ExtraInfo_init_function,  // function to initialize message memory (memory has to be allocated)
  fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__ExtraInfo_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__ExtraInfo_message_type_support_handle = {
  0,
  &fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__ExtraInfo_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_fs_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, fs_msgs, msg, ExtraInfo)() {
  if (!fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__ExtraInfo_message_type_support_handle.typesupport_identifier) {
    fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__ExtraInfo_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &fs_msgs__msg__ExtraInfo__rosidl_typesupport_introspection_c__ExtraInfo_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
