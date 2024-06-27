// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fs_msgs:msg/Track.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__TRACK__TRAITS_HPP_
#define FS_MSGS__MSG__DETAIL__TRACK__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "fs_msgs/msg/detail/track__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'track'
#include "fs_msgs/msg/detail/cone__traits.hpp"

namespace fs_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Track & msg,
  std::ostream & out)
{
  out << "{";
  // member: track
  {
    if (msg.track.size() == 0) {
      out << "track: []";
    } else {
      out << "track: [";
      size_t pending_items = msg.track.size();
      for (auto item : msg.track) {
        to_flow_style_yaml(item, out);
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
  const Track & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: track
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.track.size() == 0) {
      out << "track: []\n";
    } else {
      out << "track:\n";
      for (auto item : msg.track) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Track & msg, bool use_flow_style = false)
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
  const fs_msgs::msg::Track & msg,
  std::ostream & out, size_t indentation = 0)
{
  fs_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fs_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const fs_msgs::msg::Track & msg)
{
  return fs_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<fs_msgs::msg::Track>()
{
  return "fs_msgs::msg::Track";
}

template<>
inline const char * name<fs_msgs::msg::Track>()
{
  return "fs_msgs/msg/Track";
}

template<>
struct has_fixed_size<fs_msgs::msg::Track>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<fs_msgs::msg::Track>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<fs_msgs::msg::Track>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // FS_MSGS__MSG__DETAIL__TRACK__TRAITS_HPP_
