// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from fs_msgs:msg/FinishedSignal.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__FINISHED_SIGNAL__STRUCT_HPP_
#define FS_MSGS__MSG__DETAIL__FINISHED_SIGNAL__STRUCT_HPP_

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
# define DEPRECATED__fs_msgs__msg__FinishedSignal __attribute__((deprecated))
#else
# define DEPRECATED__fs_msgs__msg__FinishedSignal __declspec(deprecated)
#endif

namespace fs_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct FinishedSignal_
{
  using Type = FinishedSignal_<ContainerAllocator>;

  explicit FinishedSignal_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->placeholder = false;
    }
  }

  explicit FinishedSignal_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->placeholder = false;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _placeholder_type =
    bool;
  _placeholder_type placeholder;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__placeholder(
    const bool & _arg)
  {
    this->placeholder = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    fs_msgs::msg::FinishedSignal_<ContainerAllocator> *;
  using ConstRawPtr =
    const fs_msgs::msg::FinishedSignal_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fs_msgs::msg::FinishedSignal_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fs_msgs::msg::FinishedSignal_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fs_msgs::msg::FinishedSignal_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fs_msgs::msg::FinishedSignal_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fs_msgs::msg::FinishedSignal_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fs_msgs::msg::FinishedSignal_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fs_msgs::msg::FinishedSignal_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fs_msgs::msg::FinishedSignal_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fs_msgs__msg__FinishedSignal
    std::shared_ptr<fs_msgs::msg::FinishedSignal_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fs_msgs__msg__FinishedSignal
    std::shared_ptr<fs_msgs::msg::FinishedSignal_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FinishedSignal_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->placeholder != other.placeholder) {
      return false;
    }
    return true;
  }
  bool operator!=(const FinishedSignal_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FinishedSignal_

// alias to use template instance with default allocator
using FinishedSignal =
  fs_msgs::msg::FinishedSignal_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace fs_msgs

#endif  // FS_MSGS__MSG__DETAIL__FINISHED_SIGNAL__STRUCT_HPP_
