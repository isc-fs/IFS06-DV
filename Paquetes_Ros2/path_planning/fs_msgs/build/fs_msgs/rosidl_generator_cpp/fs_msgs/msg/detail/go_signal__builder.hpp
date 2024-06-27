// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from fs_msgs:msg/GoSignal.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__GO_SIGNAL__BUILDER_HPP_
#define FS_MSGS__MSG__DETAIL__GO_SIGNAL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "fs_msgs/msg/detail/go_signal__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace fs_msgs
{

namespace msg
{

namespace builder
{

class Init_GoSignal_track
{
public:
  explicit Init_GoSignal_track(::fs_msgs::msg::GoSignal & msg)
  : msg_(msg)
  {}
  ::fs_msgs::msg::GoSignal track(::fs_msgs::msg::GoSignal::_track_type arg)
  {
    msg_.track = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fs_msgs::msg::GoSignal msg_;
};

class Init_GoSignal_mission
{
public:
  explicit Init_GoSignal_mission(::fs_msgs::msg::GoSignal & msg)
  : msg_(msg)
  {}
  Init_GoSignal_track mission(::fs_msgs::msg::GoSignal::_mission_type arg)
  {
    msg_.mission = std::move(arg);
    return Init_GoSignal_track(msg_);
  }

private:
  ::fs_msgs::msg::GoSignal msg_;
};

class Init_GoSignal_header
{
public:
  Init_GoSignal_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GoSignal_mission header(::fs_msgs::msg::GoSignal::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_GoSignal_mission(msg_);
  }

private:
  ::fs_msgs::msg::GoSignal msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::fs_msgs::msg::GoSignal>()
{
  return fs_msgs::msg::builder::Init_GoSignal_header();
}

}  // namespace fs_msgs

#endif  // FS_MSGS__MSG__DETAIL__GO_SIGNAL__BUILDER_HPP_
