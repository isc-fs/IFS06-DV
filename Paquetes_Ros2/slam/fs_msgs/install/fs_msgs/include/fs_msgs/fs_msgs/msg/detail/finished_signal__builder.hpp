// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from fs_msgs:msg/FinishedSignal.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__FINISHED_SIGNAL__BUILDER_HPP_
#define FS_MSGS__MSG__DETAIL__FINISHED_SIGNAL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "fs_msgs/msg/detail/finished_signal__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace fs_msgs
{

namespace msg
{

namespace builder
{

class Init_FinishedSignal_placeholder
{
public:
  explicit Init_FinishedSignal_placeholder(::fs_msgs::msg::FinishedSignal & msg)
  : msg_(msg)
  {}
  ::fs_msgs::msg::FinishedSignal placeholder(::fs_msgs::msg::FinishedSignal::_placeholder_type arg)
  {
    msg_.placeholder = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fs_msgs::msg::FinishedSignal msg_;
};

class Init_FinishedSignal_header
{
public:
  Init_FinishedSignal_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_FinishedSignal_placeholder header(::fs_msgs::msg::FinishedSignal::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_FinishedSignal_placeholder(msg_);
  }

private:
  ::fs_msgs::msg::FinishedSignal msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::fs_msgs::msg::FinishedSignal>()
{
  return fs_msgs::msg::builder::Init_FinishedSignal_header();
}

}  // namespace fs_msgs

#endif  // FS_MSGS__MSG__DETAIL__FINISHED_SIGNAL__BUILDER_HPP_
