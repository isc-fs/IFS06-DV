// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from fs_msgs:msg/WheelStates.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__WHEEL_STATES__STRUCT_HPP_
#define FS_MSGS__MSG__DETAIL__WHEEL_STATES__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__fs_msgs__msg__WheelStates __attribute__((deprecated))
#else
# define DEPRECATED__fs_msgs__msg__WheelStates __declspec(deprecated)
#endif

namespace fs_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct WheelStates_
{
  using Type = WheelStates_<ContainerAllocator>;

  explicit WheelStates_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->fl_rpm = 0.0f;
      this->fr_rpm = 0.0f;
      this->rl_rpm = 0.0f;
      this->rr_rpm = 0.0f;
      this->fl_rotation_angle = 0.0f;
      this->fr_rotation_angle = 0.0f;
      this->rl_rotation_angle = 0.0f;
      this->rr_rotation_angle = 0.0f;
      this->fl_steering_angle = 0.0f;
      this->fr_steering_angle = 0.0f;
      this->rl_steering_angle = 0.0f;
      this->rr_steering_angle = 0.0f;
    }
  }

  explicit WheelStates_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->fl_rpm = 0.0f;
      this->fr_rpm = 0.0f;
      this->rl_rpm = 0.0f;
      this->rr_rpm = 0.0f;
      this->fl_rotation_angle = 0.0f;
      this->fr_rotation_angle = 0.0f;
      this->rl_rotation_angle = 0.0f;
      this->rr_rotation_angle = 0.0f;
      this->fl_steering_angle = 0.0f;
      this->fr_steering_angle = 0.0f;
      this->rl_steering_angle = 0.0f;
      this->rr_steering_angle = 0.0f;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _fl_rpm_type =
    float;
  _fl_rpm_type fl_rpm;
  using _fr_rpm_type =
    float;
  _fr_rpm_type fr_rpm;
  using _rl_rpm_type =
    float;
  _rl_rpm_type rl_rpm;
  using _rr_rpm_type =
    float;
  _rr_rpm_type rr_rpm;
  using _fl_rotation_angle_type =
    float;
  _fl_rotation_angle_type fl_rotation_angle;
  using _fr_rotation_angle_type =
    float;
  _fr_rotation_angle_type fr_rotation_angle;
  using _rl_rotation_angle_type =
    float;
  _rl_rotation_angle_type rl_rotation_angle;
  using _rr_rotation_angle_type =
    float;
  _rr_rotation_angle_type rr_rotation_angle;
  using _fl_steering_angle_type =
    float;
  _fl_steering_angle_type fl_steering_angle;
  using _fr_steering_angle_type =
    float;
  _fr_steering_angle_type fr_steering_angle;
  using _rl_steering_angle_type =
    float;
  _rl_steering_angle_type rl_steering_angle;
  using _rr_steering_angle_type =
    float;
  _rr_steering_angle_type rr_steering_angle;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__fl_rpm(
    const float & _arg)
  {
    this->fl_rpm = _arg;
    return *this;
  }
  Type & set__fr_rpm(
    const float & _arg)
  {
    this->fr_rpm = _arg;
    return *this;
  }
  Type & set__rl_rpm(
    const float & _arg)
  {
    this->rl_rpm = _arg;
    return *this;
  }
  Type & set__rr_rpm(
    const float & _arg)
  {
    this->rr_rpm = _arg;
    return *this;
  }
  Type & set__fl_rotation_angle(
    const float & _arg)
  {
    this->fl_rotation_angle = _arg;
    return *this;
  }
  Type & set__fr_rotation_angle(
    const float & _arg)
  {
    this->fr_rotation_angle = _arg;
    return *this;
  }
  Type & set__rl_rotation_angle(
    const float & _arg)
  {
    this->rl_rotation_angle = _arg;
    return *this;
  }
  Type & set__rr_rotation_angle(
    const float & _arg)
  {
    this->rr_rotation_angle = _arg;
    return *this;
  }
  Type & set__fl_steering_angle(
    const float & _arg)
  {
    this->fl_steering_angle = _arg;
    return *this;
  }
  Type & set__fr_steering_angle(
    const float & _arg)
  {
    this->fr_steering_angle = _arg;
    return *this;
  }
  Type & set__rl_steering_angle(
    const float & _arg)
  {
    this->rl_steering_angle = _arg;
    return *this;
  }
  Type & set__rr_steering_angle(
    const float & _arg)
  {
    this->rr_steering_angle = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    fs_msgs::msg::WheelStates_<ContainerAllocator> *;
  using ConstRawPtr =
    const fs_msgs::msg::WheelStates_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fs_msgs::msg::WheelStates_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fs_msgs::msg::WheelStates_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fs_msgs::msg::WheelStates_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fs_msgs::msg::WheelStates_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fs_msgs::msg::WheelStates_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fs_msgs::msg::WheelStates_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fs_msgs::msg::WheelStates_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fs_msgs::msg::WheelStates_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fs_msgs__msg__WheelStates
    std::shared_ptr<fs_msgs::msg::WheelStates_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fs_msgs__msg__WheelStates
    std::shared_ptr<fs_msgs::msg::WheelStates_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const WheelStates_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->fl_rpm != other.fl_rpm) {
      return false;
    }
    if (this->fr_rpm != other.fr_rpm) {
      return false;
    }
    if (this->rl_rpm != other.rl_rpm) {
      return false;
    }
    if (this->rr_rpm != other.rr_rpm) {
      return false;
    }
    if (this->fl_rotation_angle != other.fl_rotation_angle) {
      return false;
    }
    if (this->fr_rotation_angle != other.fr_rotation_angle) {
      return false;
    }
    if (this->rl_rotation_angle != other.rl_rotation_angle) {
      return false;
    }
    if (this->rr_rotation_angle != other.rr_rotation_angle) {
      return false;
    }
    if (this->fl_steering_angle != other.fl_steering_angle) {
      return false;
    }
    if (this->fr_steering_angle != other.fr_steering_angle) {
      return false;
    }
    if (this->rl_steering_angle != other.rl_steering_angle) {
      return false;
    }
    if (this->rr_steering_angle != other.rr_steering_angle) {
      return false;
    }
    return true;
  }
  bool operator!=(const WheelStates_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct WheelStates_

// alias to use template instance with default allocator
using WheelStates =
  fs_msgs::msg::WheelStates_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace fs_msgs

#endif  // FS_MSGS__MSG__DETAIL__WHEEL_STATES__STRUCT_HPP_
