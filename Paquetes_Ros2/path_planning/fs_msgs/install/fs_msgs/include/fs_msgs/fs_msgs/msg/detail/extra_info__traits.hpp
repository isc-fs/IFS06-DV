// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fs_msgs:msg/ExtraInfo.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__EXTRA_INFO__TRAITS_HPP_
#define FS_MSGS__MSG__DETAIL__EXTRA_INFO__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "fs_msgs/msg/detail/extra_info__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace fs_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const ExtraInfo & msg,
  std::ostream & out)
{
  out << "{";
  // member: doo_counter
  {
    out << "doo_counter: ";
    rosidl_generator_traits::value_to_yaml(msg.doo_counter, out);
    out << ", ";
  }

  // member: laps
  {
    if (msg.laps.size() == 0) {
      out << "laps: []";
    } else {
      out << "laps: [";
      size_t pending_items = msg.laps.size();
      for (auto item : msg.laps) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ExtraInfo & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: doo_counter
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "doo_counter: ";
    rosidl_generator_traits::value_to_yaml(msg.doo_counter, out);
    out << "\n";
  }

  // member: laps
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.laps.size() == 0) {
      out << "laps: []\n";
    } else {
      out << "laps:\n";
      for (auto item : msg.laps) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ExtraInfo & msg, bool use_flow_style = false)
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
  const fs_msgs::msg::ExtraInfo & msg,
  std::ostream & out, size_t indentation = 0)
{
  fs_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fs_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const fs_msgs::msg::ExtraInfo & msg)
{
  return fs_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<fs_msgs::msg::ExtraInfo>()
{
  return "fs_msgs::msg::ExtraInfo";
}

template<>
inline const char * name<fs_msgs::msg::ExtraInfo>()
{
  return "fs_msgs/msg/ExtraInfo";
}

template<>
struct has_fixed_size<fs_msgs::msg::ExtraInfo>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<fs_msgs::msg::ExtraInfo>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<fs_msgs::msg::ExtraInfo>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // FS_MSGS__MSG__DETAIL__EXTRA_INFO__TRAITS_HPP_
