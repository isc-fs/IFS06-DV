// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from fs_msgs:msg/Track.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__TRACK__BUILDER_HPP_
#define FS_MSGS__MSG__DETAIL__TRACK__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "fs_msgs/msg/detail/track__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace fs_msgs
{

namespace msg
{

namespace builder
{

class Init_Track_track
{
public:
  Init_Track_track()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::fs_msgs::msg::Track track(::fs_msgs::msg::Track::_track_type arg)
  {
    msg_.track = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fs_msgs::msg::Track msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::fs_msgs::msg::Track>()
{
  return fs_msgs::msg::builder::Init_Track_track();
}

}  // namespace fs_msgs

#endif  // FS_MSGS__MSG__DETAIL__TRACK__BUILDER_HPP_
