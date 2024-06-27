// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fs_msgs:msg/Cone.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__CONE__TRAITS_HPP_
#define FS_MSGS__MSG__DETAIL__CONE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "fs_msgs/msg/detail/cone__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'location'
#include "geometry_msgs/msg/detail/point__traits.hpp"

namespace fs_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Cone & msg,
  std::ostream & out)
{
  out << "{";
  // member: location
  {
    out << "location: ";
    to_flow_style_yaml(msg.location, out);
    out << ", ";
  }

  // member: color
  {
    out << "color: ";
    rosidl_generator_traits::value_to_yaml(msg.color, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Cone & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: location
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "location:\n";
    to_block_style_yaml(msg.location, out, indentation + 2);
  }

  // member: color
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "color: ";
    rosidl_generator_traits::value_to_yaml(msg.color, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Cone & msg, bool use_flow_style = false)
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
  const fs_msgs::msg::Cone & msg,
  std::ostream & out, size_t indentation = 0)
{
  fs_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fs_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const fs_msgs::msg::Cone & msg)
{
  return fs_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<fs_msgs::msg::Cone>()
{
  return "fs_msgs::msg::Cone";
}

template<>
inline const char * name<fs_msgs::msg::Cone>()
{
  return "fs_msgs/msg/Cone";
}

template<>
struct has_fixed_size<fs_msgs::msg::Cone>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::Point>::value> {};

template<>
struct has_bounded_size<fs_msgs::msg::Cone>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::Point>::value> {};

template<>
struct is_message<fs_msgs::msg::Cone>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // FS_MSGS__MSG__DETAIL__CONE__TRAITS_HPP_
