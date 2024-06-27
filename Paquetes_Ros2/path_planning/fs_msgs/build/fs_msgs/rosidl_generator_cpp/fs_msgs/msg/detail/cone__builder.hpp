// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from fs_msgs:msg/Cone.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__CONE__BUILDER_HPP_
#define FS_MSGS__MSG__DETAIL__CONE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "fs_msgs/msg/detail/cone__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace fs_msgs
{

namespace msg
{

namespace builder
{

class Init_Cone_color
{
public:
  explicit Init_Cone_color(::fs_msgs::msg::Cone & msg)
  : msg_(msg)
  {}
  ::fs_msgs::msg::Cone color(::fs_msgs::msg::Cone::_color_type arg)
  {
    msg_.color = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fs_msgs::msg::Cone msg_;
};

class Init_Cone_location
{
public:
  Init_Cone_location()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Cone_color location(::fs_msgs::msg::Cone::_location_type arg)
  {
    msg_.location = std::move(arg);
    return Init_Cone_color(msg_);
  }

private:
  ::fs_msgs::msg::Cone msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::fs_msgs::msg::Cone>()
{
  return fs_msgs::msg::builder::Init_Cone_location();
}

}  // namespace fs_msgs

#endif  // FS_MSGS__MSG__DETAIL__CONE__BUILDER_HPP_
