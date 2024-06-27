// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from fs_msgs:msg/ControlCommand.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__CONTROL_COMMAND__BUILDER_HPP_
#define FS_MSGS__MSG__DETAIL__CONTROL_COMMAND__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "fs_msgs/msg/detail/control_command__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace fs_msgs
{

namespace msg
{

namespace builder
{

class Init_ControlCommand_brake
{
public:
  explicit Init_ControlCommand_brake(::fs_msgs::msg::ControlCommand & msg)
  : msg_(msg)
  {}
  ::fs_msgs::msg::ControlCommand brake(::fs_msgs::msg::ControlCommand::_brake_type arg)
  {
    msg_.brake = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fs_msgs::msg::ControlCommand msg_;
};

class Init_ControlCommand_steering
{
public:
  explicit Init_ControlCommand_steering(::fs_msgs::msg::ControlCommand & msg)
  : msg_(msg)
  {}
  Init_ControlCommand_brake steering(::fs_msgs::msg::ControlCommand::_steering_type arg)
  {
    msg_.steering = std::move(arg);
    return Init_ControlCommand_brake(msg_);
  }

private:
  ::fs_msgs::msg::ControlCommand msg_;
};

class Init_ControlCommand_throttle
{
public:
  explicit Init_ControlCommand_throttle(::fs_msgs::msg::ControlCommand & msg)
  : msg_(msg)
  {}
  Init_ControlCommand_steering throttle(::fs_msgs::msg::ControlCommand::_throttle_type arg)
  {
    msg_.throttle = std::move(arg);
    return Init_ControlCommand_steering(msg_);
  }

private:
  ::fs_msgs::msg::ControlCommand msg_;
};

class Init_ControlCommand_header
{
public:
  Init_ControlCommand_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ControlCommand_throttle header(::fs_msgs::msg::ControlCommand::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_ControlCommand_throttle(msg_);
  }

private:
  ::fs_msgs::msg::ControlCommand msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::fs_msgs::msg::ControlCommand>()
{
  return fs_msgs::msg::builder::Init_ControlCommand_header();
}

}  // namespace fs_msgs

#endif  // FS_MSGS__MSG__DETAIL__CONTROL_COMMAND__BUILDER_HPP_
