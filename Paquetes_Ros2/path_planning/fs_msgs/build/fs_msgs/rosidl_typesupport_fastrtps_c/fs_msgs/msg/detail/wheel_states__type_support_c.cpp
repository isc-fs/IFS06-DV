// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from fs_msgs:msg/WheelStates.idl
// generated code does not contain a copyright notice
#include "fs_msgs/msg/detail/wheel_states__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "fs_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "fs_msgs/msg/detail/wheel_states__struct.h"
#include "fs_msgs/msg/detail/wheel_states__functions.h"
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

#include "std_msgs/msg/detail/header__functions.h"  // header

// forward declare type support functions
ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_fs_msgs
size_t get_serialized_size_std_msgs__msg__Header(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_fs_msgs
size_t max_serialized_size_std_msgs__msg__Header(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_fs_msgs
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, std_msgs, msg, Header)();


using _WheelStates__ros_msg_type = fs_msgs__msg__WheelStates;

static bool _WheelStates__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _WheelStates__ros_msg_type * ros_message = static_cast<const _WheelStates__ros_msg_type *>(untyped_ros_message);
  // Field name: header
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, Header
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->header, cdr))
    {
      return false;
    }
  }

  // Field name: fl_rpm
  {
    cdr << ros_message->fl_rpm;
  }

  // Field name: fr_rpm
  {
    cdr << ros_message->fr_rpm;
  }

  // Field name: rl_rpm
  {
    cdr << ros_message->rl_rpm;
  }

  // Field name: rr_rpm
  {
    cdr << ros_message->rr_rpm;
  }

  // Field name: fl_rotation_angle
  {
    cdr << ros_message->fl_rotation_angle;
  }

  // Field name: fr_rotation_angle
  {
    cdr << ros_message->fr_rotation_angle;
  }

  // Field name: rl_rotation_angle
  {
    cdr << ros_message->rl_rotation_angle;
  }

  // Field name: rr_rotation_angle
  {
    cdr << ros_message->rr_rotation_angle;
  }

  // Field name: fl_steering_angle
  {
    cdr << ros_message->fl_steering_angle;
  }

  // Field name: fr_steering_angle
  {
    cdr << ros_message->fr_steering_angle;
  }

  // Field name: rl_steering_angle
  {
    cdr << ros_message->rl_steering_angle;
  }

  // Field name: rr_steering_angle
  {
    cdr << ros_message->rr_steering_angle;
  }

  return true;
}

static bool _WheelStates__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _WheelStates__ros_msg_type * ros_message = static_cast<_WheelStates__ros_msg_type *>(untyped_ros_message);
  // Field name: header
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, Header
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->header))
    {
      return false;
    }
  }

  // Field name: fl_rpm
  {
    cdr >> ros_message->fl_rpm;
  }

  // Field name: fr_rpm
  {
    cdr >> ros_message->fr_rpm;
  }

  // Field name: rl_rpm
  {
    cdr >> ros_message->rl_rpm;
  }

  // Field name: rr_rpm
  {
    cdr >> ros_message->rr_rpm;
  }

  // Field name: fl_rotation_angle
  {
    cdr >> ros_message->fl_rotation_angle;
  }

  // Field name: fr_rotation_angle
  {
    cdr >> ros_message->fr_rotation_angle;
  }

  // Field name: rl_rotation_angle
  {
    cdr >> ros_message->rl_rotation_angle;
  }

  // Field name: rr_rotation_angle
  {
    cdr >> ros_message->rr_rotation_angle;
  }

  // Field name: fl_steering_angle
  {
    cdr >> ros_message->fl_steering_angle;
  }

  // Field name: fr_steering_angle
  {
    cdr >> ros_message->fr_steering_angle;
  }

  // Field name: rl_steering_angle
  {
    cdr >> ros_message->rl_steering_angle;
  }

  // Field name: rr_steering_angle
  {
    cdr >> ros_message->rr_steering_angle;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_fs_msgs
size_t get_serialized_size_fs_msgs__msg__WheelStates(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _WheelStates__ros_msg_type * ros_message = static_cast<const _WheelStates__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name header

  current_alignment += get_serialized_size_std_msgs__msg__Header(
    &(ros_message->header), current_alignment);
  // field.name fl_rpm
  {
    size_t item_size = sizeof(ros_message->fl_rpm);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name fr_rpm
  {
    size_t item_size = sizeof(ros_message->fr_rpm);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name rl_rpm
  {
    size_t item_size = sizeof(ros_message->rl_rpm);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name rr_rpm
  {
    size_t item_size = sizeof(ros_message->rr_rpm);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name fl_rotation_angle
  {
    size_t item_size = sizeof(ros_message->fl_rotation_angle);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name fr_rotation_angle
  {
    size_t item_size = sizeof(ros_message->fr_rotation_angle);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name rl_rotation_angle
  {
    size_t item_size = sizeof(ros_message->rl_rotation_angle);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name rr_rotation_angle
  {
    size_t item_size = sizeof(ros_message->rr_rotation_angle);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name fl_steering_angle
  {
    size_t item_size = sizeof(ros_message->fl_steering_angle);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name fr_steering_angle
  {
    size_t item_size = sizeof(ros_message->fr_steering_angle);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name rl_steering_angle
  {
    size_t item_size = sizeof(ros_message->rl_steering_angle);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name rr_steering_angle
  {
    size_t item_size = sizeof(ros_message->rr_steering_angle);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _WheelStates__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_fs_msgs__msg__WheelStates(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_fs_msgs
size_t max_serialized_size_fs_msgs__msg__WheelStates(
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

  // member: header
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size;
      inner_size =
        max_serialized_size_std_msgs__msg__Header(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }
  // member: fl_rpm
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: fr_rpm
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: rl_rpm
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: rr_rpm
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: fl_rotation_angle
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: fr_rotation_angle
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: rl_rotation_angle
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: rr_rotation_angle
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: fl_steering_angle
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: fr_steering_angle
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: rl_steering_angle
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: rr_steering_angle
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = fs_msgs__msg__WheelStates;
    is_plain =
      (
      offsetof(DataType, rr_steering_angle) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _WheelStates__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_fs_msgs__msg__WheelStates(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_WheelStates = {
  "fs_msgs::msg",
  "WheelStates",
  _WheelStates__cdr_serialize,
  _WheelStates__cdr_deserialize,
  _WheelStates__get_serialized_size,
  _WheelStates__max_serialized_size
};

static rosidl_message_type_support_t _WheelStates__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_WheelStates,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, fs_msgs, msg, WheelStates)() {
  return &_WheelStates__type_support;
}

#if defined(__cplusplus)
}
#endif
