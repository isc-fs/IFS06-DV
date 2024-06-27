// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from fs_msgs:msg/Track.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "fs_msgs/msg/detail/track__struct.hpp"
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

void Track_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) fs_msgs::msg::Track(_init);
}

void Track_fini_function(void * message_memory)
{
  auto typed_message = static_cast<fs_msgs::msg::Track *>(message_memory);
  typed_message->~Track();
}

size_t size_function__Track__track(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<fs_msgs::msg::Cone> *>(untyped_member);
  return member->size();
}

const void * get_const_function__Track__track(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<fs_msgs::msg::Cone> *>(untyped_member);
  return &member[index];
}

void * get_function__Track__track(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<fs_msgs::msg::Cone> *>(untyped_member);
  return &member[index];
}

void fetch_function__Track__track(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const fs_msgs::msg::Cone *>(
    get_const_function__Track__track(untyped_member, index));
  auto & value = *reinterpret_cast<fs_msgs::msg::Cone *>(untyped_value);
  value = item;
}

void assign_function__Track__track(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<fs_msgs::msg::Cone *>(
    get_function__Track__track(untyped_member, index));
  const auto & value = *reinterpret_cast<const fs_msgs::msg::Cone *>(untyped_value);
  item = value;
}

void resize_function__Track__track(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<fs_msgs::msg::Cone> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Track_message_member_array[1] = {
  {
    "track",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<fs_msgs::msg::Cone>(),  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(fs_msgs::msg::Track, track),  // bytes offset in struct
    nullptr,  // default value
    size_function__Track__track,  // size() function pointer
    get_const_function__Track__track,  // get_const(index) function pointer
    get_function__Track__track,  // get(index) function pointer
    fetch_function__Track__track,  // fetch(index, &value) function pointer
    assign_function__Track__track,  // assign(index, value) function pointer
    resize_function__Track__track  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Track_message_members = {
  "fs_msgs::msg",  // message namespace
  "Track",  // message name
  1,  // number of fields
  sizeof(fs_msgs::msg::Track),
  Track_message_member_array,  // message members
  Track_init_function,  // function to initialize message memory (memory has to be allocated)
  Track_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Track_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Track_message_members,
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
get_message_type_support_handle<fs_msgs::msg::Track>()
{
  return &::fs_msgs::msg::rosidl_typesupport_introspection_cpp::Track_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, fs_msgs, msg, Track)() {
  return &::fs_msgs::msg::rosidl_typesupport_introspection_cpp::Track_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
