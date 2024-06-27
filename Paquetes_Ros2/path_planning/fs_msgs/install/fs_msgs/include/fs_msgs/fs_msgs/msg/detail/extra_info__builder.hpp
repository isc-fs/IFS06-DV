// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from fs_msgs:msg/ExtraInfo.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__EXTRA_INFO__BUILDER_HPP_
#define FS_MSGS__MSG__DETAIL__EXTRA_INFO__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "fs_msgs/msg/detail/extra_info__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace fs_msgs
{

namespace msg
{

namespace builder
{

class Init_ExtraInfo_laps
{
public:
  explicit Init_ExtraInfo_laps(::fs_msgs::msg::ExtraInfo & msg)
  : msg_(msg)
  {}
  ::fs_msgs::msg::ExtraInfo laps(::fs_msgs::msg::ExtraInfo::_laps_type arg)
  {
    msg_.laps = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fs_msgs::msg::ExtraInfo msg_;
};

class Init_ExtraInfo_doo_counter
{
public:
  Init_ExtraInfo_doo_counter()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ExtraInfo_laps doo_counter(::fs_msgs::msg::ExtraInfo::_doo_counter_type arg)
  {
    msg_.doo_counter = std::move(arg);
    return Init_ExtraInfo_laps(msg_);
  }

private:
  ::fs_msgs::msg::ExtraInfo msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::fs_msgs::msg::ExtraInfo>()
{
  return fs_msgs::msg::builder::Init_ExtraInfo_doo_counter();
}

}  // namespace fs_msgs

#endif  // FS_MSGS__MSG__DETAIL__EXTRA_INFO__BUILDER_HPP_
