// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from fs_msgs:msg/ExtraInfo.idl
// generated code does not contain a copyright notice
#include "fs_msgs/msg/detail/extra_info__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "fs_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "fs_msgs/msg/detail/extra_info__struct.h"
#include "fs_msgs/msg/detail/extra_info__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "rosidl_runtime_c/primitives_sequence.h"  // laps
#include "rosidl_runtime_c/primitives_sequence_functions.h"  // laps

// forward declare type support functions


using _ExtraInfo__ros_msg_type = fs_msgs__msg__ExtraInfo;

static bool _ExtraInfo__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _ExtraInfo__ros_msg_type * ros_message = static_cast<const _ExtraInfo__ros_msg_type *>(untyped_ros_message);
  // Field name: doo_counter
  {
    cdr << ros_message->doo_counter;
  }

  // Field name: laps
  {
    size_t size = ros_message->laps.size;
    auto array_ptr = ros_message->laps.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  return true;
}

static bool _ExtraInfo__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _ExtraInfo__ros_msg_type * ros_message = static_cast<_ExtraInfo__ros_msg_type *>(untyped_ros_message);
  // Field name: doo_counter
  {
    cdr >> ros_message->doo_counter;
  }

  // Field name: laps
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->laps.data) {
      rosidl_runtime_c__float__Sequence__fini(&ros_message->laps);
    }
    if (!rosidl_runtime_c__float__Sequence__init(&ros_message->laps, size)) {
      fprintf(stderr, "failed to create array for field 'laps'");
      return false;
    }
    auto array_ptr = ros_message->laps.data;
    cdr.deserializeArray(array_ptr, size);
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_fs_msgs
size_t get_serialized_size_fs_msgs__msg__ExtraInfo(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _ExtraInfo__ros_msg_type * ros_message = static_cast<const _ExtraInfo__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name doo_counter
  {
    size_t item_size = sizeof(ros_message->doo_counter);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name laps
  {
    size_t array_size = ros_message->laps.size;
    auto array_ptr = ros_message->laps.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _ExtraInfo__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_fs_msgs__msg__ExtraInfo(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_fs_msgs
size_t max_serialized_size_fs_msgs__msg__ExtraInfo(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: doo_counter
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: laps
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = fs_msgs__msg__ExtraInfo;
    is_plain =
      (
      offsetof(DataType, laps) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _ExtraInfo__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_fs_msgs__msg__ExtraInfo(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_ExtraInfo = {
  "fs_msgs::msg",
  "ExtraInfo",
  _ExtraInfo__cdr_serialize,
  _ExtraInfo__cdr_deserialize,
  _ExtraInfo__get_serialized_size,
  _ExtraInfo__max_serialized_size
};

static rosidl_message_type_support_t _ExtraInfo__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_ExtraInfo,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, fs_msgs, msg, ExtraInfo)() {
  return &_ExtraInfo__type_support;
}

#if defined(__cplusplus)
}
#endif
