// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from fs_msgs:msg/Track.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "fs_msgs/msg/detail/track__rosidl_typesupport_introspection_c.h"
#include "fs_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "fs_msgs/msg/detail/track__functions.h"
#include "fs_msgs/msg/detail/track__struct.h"


// Include directives for member types
// Member `track`
#include "fs_msgs/msg/cone.h"
// Member `track`
#include "fs_msgs/msg/detail/cone__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void fs_msgs__msg__Track__rosidl_typesupport_introspection_c__Track_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  fs_msgs__msg__Track__init(message_memory);
}

void fs_msgs__msg__Track__rosidl_typesupport_introspection_c__Track_fini_function(void * message_memory)
{
  fs_msgs__msg__Track__fini(message_memory);
}

size_t fs_msgs__msg__Track__rosidl_typesupport_introspection_c__size_function__Track__track(
  const void * untyped_member)
{
  const fs_msgs__msg__Cone__Sequence * member =
    (const fs_msgs__msg__Cone__Sequence *)(untyped_member);
  return member->size;
}

const void * fs_msgs__msg__Track__rosidl_typesupport_introspection_c__get_const_function__Track__track(
  const void * untyped_member, size_t index)
{
  const fs_msgs__msg__Cone__Sequence * member =
    (const fs_msgs__msg__Cone__Sequence *)(untyped_member);
  return &member->data[index];
}

void * fs_msgs__msg__Track__rosidl_typesupport_introspection_c__get_function__Track__track(
  void * untyped_member, size_t index)
{
  fs_msgs__msg__Cone__Sequence * member =
    (fs_msgs__msg__Cone__Sequence *)(untyped_member);
  return &member->data[index];
}

void fs_msgs__msg__Track__rosidl_typesupport_introspection_c__fetch_function__Track__track(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const fs_msgs__msg__Cone * item =
    ((const fs_msgs__msg__Cone *)
    fs_msgs__msg__Track__rosidl_typesupport_introspection_c__get_const_function__Track__track(untyped_member, index));
  fs_msgs__msg__Cone * value =
    (fs_msgs__msg__Cone *)(untyped_value);
  *value = *item;
}

void fs_msgs__msg__Track__rosidl_typesupport_introspection_c__assign_function__Track__track(
  void * untyped_member, size_t index, const void * untyped_value)
{
  fs_msgs__msg__Cone * item =
    ((fs_msgs__msg__Cone *)
    fs_msgs__msg__Track__rosidl_typesupport_introspection_c__get_function__Track__track(untyped_member, index));
  const fs_msgs__msg__Cone * value =
    (const fs_msgs__msg__Cone *)(untyped_value);
  *item = *value;
}

bool fs_msgs__msg__Track__rosidl_typesupport_introspection_c__resize_function__Track__track(
  void * untyped_member, size_t size)
{
  fs_msgs__msg__Cone__Sequence * member =
    (fs_msgs__msg__Cone__Sequence *)(untyped_member);
  fs_msgs__msg__Cone__Sequence__fini(member);
  return fs_msgs__msg__Cone__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember fs_msgs__msg__Track__rosidl_typesupport_introspection_c__Track_message_member_array[1] = {
  {
    "track",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(fs_msgs__msg__Track, track),  // bytes offset in struct
    NULL,  // default value
    fs_msgs__msg__Track__rosidl_typesupport_introspection_c__size_function__Track__track,  // size() function pointer
    fs_msgs__msg__Track__rosidl_typesupport_introspection_c__get_const_function__Track__track,  // get_const(index) function pointer
    fs_msgs__msg__Track__rosidl_typesupport_introspection_c__get_function__Track__track,  // get(index) function pointer
    fs_msgs__msg__Track__rosidl_typesupport_introspection_c__fetch_function__Track__track,  // fetch(index, &value) function pointer
    fs_msgs__msg__Track__rosidl_typesupport_introspection_c__assign_function__Track__track,  // assign(index, value) function pointer
    fs_msgs__msg__Track__rosidl_typesupport_introspection_c__resize_function__Track__track  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers fs_msgs__msg__Track__rosidl_typesupport_introspection_c__Track_message_members = {
  "fs_msgs__msg",  // message namespace
  "Track",  // message name
  1,  // number of fields
  sizeof(fs_msgs__msg__Track),
  fs_msgs__msg__Track__rosidl_typesupport_introspection_c__Track_message_member_array,  // message members
  fs_msgs__msg__Track__rosidl_typesupport_introspection_c__Track_init_function,  // function to initialize message memory (memory has to be allocated)
  fs_msgs__msg__Track__rosidl_typesupport_introspection_c__Track_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t fs_msgs__msg__Track__rosidl_typesupport_introspection_c__Track_message_type_support_handle = {
  0,
  &fs_msgs__msg__Track__rosidl_typesupport_introspection_c__Track_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_fs_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, fs_msgs, msg, Track)() {
  fs_msgs__msg__Track__rosidl_typesupport_introspection_c__Track_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, fs_msgs, msg, Cone)();
  if (!fs_msgs__msg__Track__rosidl_typesupport_introspection_c__Track_message_type_support_handle.typesupport_identifier) {
    fs_msgs__msg__Track__rosidl_typesupport_introspection_c__Track_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &fs_msgs__msg__Track__rosidl_typesupport_introspection_c__Track_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
