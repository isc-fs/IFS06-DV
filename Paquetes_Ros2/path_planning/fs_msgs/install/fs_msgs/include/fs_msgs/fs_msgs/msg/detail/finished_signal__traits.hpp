// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fs_msgs:msg/FinishedSignal.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__FINISHED_SIGNAL__TRAITS_HPP_
#define FS_MSGS__MSG__DETAIL__FINISHED_SIGNAL__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "fs_msgs/msg/detail/finished_signal__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace fs_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const FinishedSignal & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: placeholder
  {
    out << "placeholder: ";
    rosidl_generator_traits::value_to_yaml(msg.placeholder, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const FinishedSignal & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: placeholder
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "placeholder: ";
    rosidl_generator_traits::value_to_yaml(msg.placeholder, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const FinishedSignal & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace fs_msgs

namespace rosidl_generator_traits
{

[[deprecated("use fs_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const fs_msgs::msg::FinishedSignal & msg,
  std::ostream & out, size_t indentation = 0)
{
  fs_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fs_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const fs_msgs::msg::FinishedSignal & msg)
{
  return fs_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<fs_msgs::msg::FinishedSignal>()
{
  return "fs_msgs::msg::FinishedSignal";
}

template<>
inline const char * name<fs_msgs::msg::FinishedSignal>()
{
  return "fs_msgs/msg/FinishedSignal";
}

template<>
struct has_fixed_size<fs_msgs::msg::FinishedSignal>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<fs_msgs::msg::FinishedSignal>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<fs_msgs::msg::FinishedSignal>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // FS_MSGS__MSG__DETAIL__FINISHED_SIGNAL__TRAITS_HPP_
