// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from fs_msgs:msg/ExtraInfo.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__EXTRA_INFO__STRUCT_HPP_
#define FS_MSGS__MSG__DETAIL__EXTRA_INFO__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__fs_msgs__msg__ExtraInfo __attribute__((deprecated))
#else
# define DEPRECATED__fs_msgs__msg__ExtraInfo __declspec(deprecated)
#endif

namespace fs_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ExtraInfo_
{
  using Type = ExtraInfo_<ContainerAllocator>;

  explicit ExtraInfo_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->doo_counter = 0ul;
    }
  }

  explicit ExtraInfo_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->doo_counter = 0ul;
    }
  }

  // field types and members
  using _doo_counter_type =
    uint32_t;
  _doo_counter_type doo_counter;
  using _laps_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _laps_type laps;

  // setters for named parameter idiom
  Type & set__doo_counter(
    const uint32_t & _arg)
  {
    this->doo_counter = _arg;
    return *this;
  }
  Type & set__laps(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->laps = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    fs_msgs::msg::ExtraInfo_<ContainerAllocator> *;
  using ConstRawPtr =
    const fs_msgs::msg::ExtraInfo_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fs_msgs::msg::ExtraInfo_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fs_msgs::msg::ExtraInfo_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fs_msgs::msg::ExtraInfo_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fs_msgs::msg::ExtraInfo_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fs_msgs::msg::ExtraInfo_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fs_msgs::msg::ExtraInfo_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fs_msgs::msg::ExtraInfo_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fs_msgs::msg::ExtraInfo_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fs_msgs__msg__ExtraInfo
    std::shared_ptr<fs_msgs::msg::ExtraInfo_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fs_msgs__msg__ExtraInfo
    std::shared_ptr<fs_msgs::msg::ExtraInfo_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ExtraInfo_ & other) const
  {
    if (this->doo_counter != other.doo_counter) {
      return false;
    }
    if (this->laps != other.laps) {
      return false;
    }
    return true;
  }
  bool operator!=(const ExtraInfo_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ExtraInfo_

// alias to use template instance with default allocator
using ExtraInfo =
  fs_msgs::msg::ExtraInfo_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace fs_msgs

#endif  // FS_MSGS__MSG__DETAIL__EXTRA_INFO__STRUCT_HPP_
