// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from fs_msgs:msg/WheelStates.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__WHEEL_STATES__BUILDER_HPP_
#define FS_MSGS__MSG__DETAIL__WHEEL_STATES__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "fs_msgs/msg/detail/wheel_states__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace fs_msgs
{

namespace msg
{

namespace builder
{

class Init_WheelStates_rr_steering_angle
{
public:
  explicit Init_WheelStates_rr_steering_angle(::fs_msgs::msg::WheelStates & msg)
  : msg_(msg)
  {}
  ::fs_msgs::msg::WheelStates rr_steering_angle(::fs_msgs::msg::WheelStates::_rr_steering_angle_type arg)
  {
    msg_.rr_steering_angle = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fs_msgs::msg::WheelStates msg_;
};

class Init_WheelStates_rl_steering_angle
{
public:
  explicit Init_WheelStates_rl_steering_angle(::fs_msgs::msg::WheelStates & msg)
  : msg_(msg)
  {}
  Init_WheelStates_rr_steering_angle rl_steering_angle(::fs_msgs::msg::WheelStates::_rl_steering_angle_type arg)
  {
    msg_.rl_steering_angle = std::move(arg);
    return Init_WheelStates_rr_steering_angle(msg_);
  }

private:
  ::fs_msgs::msg::WheelStates msg_;
};

class Init_WheelStates_fr_steering_angle
{
public:
  explicit Init_WheelStates_fr_steering_angle(::fs_msgs::msg::WheelStates & msg)
  : msg_(msg)
  {}
  Init_WheelStates_rl_steering_angle fr_steering_angle(::fs_msgs::msg::WheelStates::_fr_steering_angle_type arg)
  {
    msg_.fr_steering_angle = std::move(arg);
    return Init_WheelStates_rl_steering_angle(msg_);
  }

private:
  ::fs_msgs::msg::WheelStates msg_;
};

class Init_WheelStates_fl_steering_angle
{
public:
  explicit Init_WheelStates_fl_steering_angle(::fs_msgs::msg::WheelStates & msg)
  : msg_(msg)
  {}
  Init_WheelStates_fr_steering_angle fl_steering_angle(::fs_msgs::msg::WheelStates::_fl_steering_angle_type arg)
  {
    msg_.fl_steering_angle = std::move(arg);
    return Init_WheelStates_fr_steering_angle(msg_);
  }

private:
  ::fs_msgs::msg::WheelStates msg_;
};

class Init_WheelStates_rr_rotation_angle
{
public:
  explicit Init_WheelStates_rr_rotation_angle(::fs_msgs::msg::WheelStates & msg)
  : msg_(msg)
  {}
  Init_WheelStates_fl_steering_angle rr_rotation_angle(::fs_msgs::msg::WheelStates::_rr_rotation_angle_type arg)
  {
    msg_.rr_rotation_angle = std::move(arg);
    return Init_WheelStates_fl_steering_angle(msg_);
  }

private:
  ::fs_msgs::msg::WheelStates msg_;
};

class Init_WheelStates_rl_rotation_angle
{
public:
  explicit Init_WheelStates_rl_rotation_angle(::fs_msgs::msg::WheelStates & msg)
  : msg_(msg)
  {}
  Init_WheelStates_rr_rotation_angle rl_rotation_angle(::fs_msgs::msg::WheelStates::_rl_rotation_angle_type arg)
  {
    msg_.rl_rotation_angle = std::move(arg);
    return Init_WheelStates_rr_rotation_angle(msg_);
  }

private:
  ::fs_msgs::msg::WheelStates msg_;
};

class Init_WheelStates_fr_rotation_angle
{
public:
  explicit Init_WheelStates_fr_rotation_angle(::fs_msgs::msg::WheelStates & msg)
  : msg_(msg)
  {}
  Init_WheelStates_rl_rotation_angle fr_rotation_angle(::fs_msgs::msg::WheelStates::_fr_rotation_angle_type arg)
  {
    msg_.fr_rotation_angle = std::move(arg);
    return Init_WheelStates_rl_rotation_angle(msg_);
  }

private:
  ::fs_msgs::msg::WheelStates msg_;
};

class Init_WheelStates_fl_rotation_angle
{
public:
  explicit Init_WheelStates_fl_rotation_angle(::fs_msgs::msg::WheelStates & msg)
  : msg_(msg)
  {}
  Init_WheelStates_fr_rotation_angle fl_rotation_angle(::fs_msgs::msg::WheelStates::_fl_rotation_angle_type arg)
  {
    msg_.fl_rotation_angle = std::move(arg);
    return Init_WheelStates_fr_rotation_angle(msg_);
  }

private:
  ::fs_msgs::msg::WheelStates msg_;
};

class Init_WheelStates_rr_rpm
{
public:
  explicit Init_WheelStates_rr_rpm(::fs_msgs::msg::WheelStates & msg)
  : msg_(msg)
  {}
  Init_WheelStates_fl_rotation_angle rr_rpm(::fs_msgs::msg::WheelStates::_rr_rpm_type arg)
  {
    msg_.rr_rpm = std::move(arg);
    return Init_WheelStates_fl_rotation_angle(msg_);
  }

private:
  ::fs_msgs::msg::WheelStates msg_;
};

class Init_WheelStates_rl_rpm
{
public:
  explicit Init_WheelStates_rl_rpm(::fs_msgs::msg::WheelStates & msg)
  : msg_(msg)
  {}
  Init_WheelStates_rr_rpm rl_rpm(::fs_msgs::msg::WheelStates::_rl_rpm_type arg)
  {
    msg_.rl_rpm = std::move(arg);
    return Init_WheelStates_rr_rpm(msg_);
  }

private:
  ::fs_msgs::msg::WheelStates msg_;
};

class Init_WheelStates_fr_rpm
{
public:
  explicit Init_WheelStates_fr_rpm(::fs_msgs::msg::WheelStates & msg)
  : msg_(msg)
  {}
  Init_WheelStates_rl_rpm fr_rpm(::fs_msgs::msg::WheelStates::_fr_rpm_type arg)
  {
    msg_.fr_rpm = std::move(arg);
    return Init_WheelStates_rl_rpm(msg_);
  }

private:
  ::fs_msgs::msg::WheelStates msg_;
};

class Init_WheelStates_fl_rpm
{
public:
  explicit Init_WheelStates_fl_rpm(::fs_msgs::msg::WheelStates & msg)
  : msg_(msg)
  {}
  Init_WheelStates_fr_rpm fl_rpm(::fs_msgs::msg::WheelStates::_fl_rpm_type arg)
  {
    msg_.fl_rpm = std::move(arg);
    return Init_WheelStates_fr_rpm(msg_);
  }

private:
  ::fs_msgs::msg::WheelStates msg_;
};

class Init_WheelStates_header
{
public:
  Init_WheelStates_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_WheelStates_fl_rpm header(::fs_msgs::msg::WheelStates::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_WheelStates_fl_rpm(msg_);
  }

private:
  ::fs_msgs::msg::WheelStates msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::fs_msgs::msg::WheelStates>()
{
  return fs_msgs::msg::builder::Init_WheelStates_header();
}

}  // namespace fs_msgs

#endif  // FS_MSGS__MSG__DETAIL__WHEEL_STATES__BUILDER_HPP_
