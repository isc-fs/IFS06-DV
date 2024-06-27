// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from fs_msgs:msg/Track.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__TRACK__STRUCT_HPP_
#define FS_MSGS__MSG__DETAIL__TRACK__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'track'
#include "fs_msgs/msg/detail/cone__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__fs_msgs__msg__Track __attribute__((deprecated))
#else
# define DEPRECATED__fs_msgs__msg__Track __declspec(deprecated)
#endif

namespace fs_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Track_
{
  using Type = Track_<ContainerAllocator>;

  explicit Track_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit Track_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _track_type =
    std::vector<fs_msgs::msg::Cone_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<fs_msgs::msg::Cone_<ContainerAllocator>>>;
  _track_type track;

  // setters for named parameter idiom
  Type & set__track(
    const std::vector<fs_msgs::msg::Cone_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<fs_msgs::msg::Cone_<ContainerAllocator>>> & _arg)
  {
    this->track = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    fs_msgs::msg::Track_<ContainerAllocator> *;
  using ConstRawPtr =
    const fs_msgs::msg::Track_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fs_msgs::msg::Track_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fs_msgs::msg::Track_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fs_msgs::msg::Track_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fs_msgs::msg::Track_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fs_msgs::msg::Track_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fs_msgs::msg::Track_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fs_msgs::msg::Track_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fs_msgs::msg::Track_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fs_msgs__msg__Track
    std::shared_ptr<fs_msgs::msg::Track_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fs_msgs__msg__Track
    std::shared_ptr<fs_msgs::msg::Track_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Track_ & other) const
  {
    if (this->track != other.track) {
      return false;
    }
    return true;
  }
  bool operator!=(const Track_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Track_

// alias to use template instance with default allocator
using Track =
  fs_msgs::msg::Track_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace fs_msgs

#endif  // FS_MSGS__MSG__DETAIL__TRACK__STRUCT_HPP_
