// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from fs_msgs:srv/Reset.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__SRV__DETAIL__RESET__BUILDER_HPP_
#define FS_MSGS__SRV__DETAIL__RESET__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "fs_msgs/srv/detail/reset__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace fs_msgs
{

namespace srv
{

namespace builder
{

class Init_Reset_Request_wait_on_last_task
{
public:
  Init_Reset_Request_wait_on_last_task()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::fs_msgs::srv::Reset_Request wait_on_last_task(::fs_msgs::srv::Reset_Request::_wait_on_last_task_type arg)
  {
    msg_.wait_on_last_task = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fs_msgs::srv::Reset_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::fs_msgs::srv::Reset_Request>()
{
  return fs_msgs::srv::builder::Init_Reset_Request_wait_on_last_task();
}

}  // namespace fs_msgs


namespace fs_msgs
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::fs_msgs::srv::Reset_Response>()
{
  return ::fs_msgs::srv::Reset_Response(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace fs_msgs

#endif  // FS_MSGS__SRV__DETAIL__RESET__BUILDER_HPP_
