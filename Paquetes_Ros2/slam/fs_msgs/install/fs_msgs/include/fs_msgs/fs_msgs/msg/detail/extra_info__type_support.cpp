// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from fs_msgs:msg/ExtraInfo.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "fs_msgs/msg/detail/extra_info__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace fs_msgs
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void ExtraInfo_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) fs_msgs::msg::ExtraInfo(_init);
}

void ExtraInfo_fini_function(void * message_memory)
{
  auto typed_message = static_cast<fs_msgs::msg::ExtraInfo *>(message_memory);
  typed_message->~ExtraInfo();
}

size_t size_function__ExtraInfo__laps(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__ExtraInfo__laps(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__ExtraInfo__laps(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void fetch_function__ExtraInfo__laps(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__ExtraInfo__laps(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__ExtraInfo__laps(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__ExtraInfo__laps(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

void resize_function__ExtraInfo__laps(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember ExtraInfo_message_member_array[2] = {
  {
    "doo_counter",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(fs_msgs::msg::ExtraInfo, doo_counter),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "laps",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(fs_msgs::msg::ExtraInfo, laps),  // bytes offset in struct
    nullptr,  // default value
    size_function__ExtraInfo__laps,  // size() function pointer
    get_const_function__ExtraInfo__laps,  // get_const(index) function pointer
    get_function__ExtraInfo__laps,  // get(index) function pointer
    fetch_function__ExtraInfo__laps,  // fetch(index, &value) function pointer
    assign_function__ExtraInfo__laps,  // assign(index, value) function pointer
    resize_function__ExtraInfo__laps  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers ExtraInfo_message_members = {
  "fs_msgs::msg",  // message namespace
  "ExtraInfo",  // message name
  2,  // number of fields
  sizeof(fs_msgs::msg::ExtraInfo),
  ExtraInfo_message_member_array,  // message members
  ExtraInfo_init_function,  // function to initialize message memory (memory has to be allocated)
  ExtraInfo_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t ExtraInfo_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &ExtraInfo_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace fs_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<fs_msgs::msg::ExtraInfo>()
{
  return &::fs_msgs::msg::rosidl_typesupport_introspection_cpp::ExtraInfo_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, fs_msgs, msg, ExtraInfo)() {
  return &::fs_msgs::msg::rosidl_typesupport_introspection_cpp::ExtraInfo_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
