// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fs_msgs:msg/WheelStates.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__WHEEL_STATES__TRAITS_HPP_
#define FS_MSGS__MSG__DETAIL__WHEEL_STATES__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "fs_msgs/msg/detail/wheel_states__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace fs_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const WheelStates & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: fl_rpm
  {
    out << "fl_rpm: ";
    rosidl_generator_traits::value_to_yaml(msg.fl_rpm, out);
    out << ", ";
  }

  // member: fr_rpm
  {
    out << "fr_rpm: ";
    rosidl_generator_traits::value_to_yaml(msg.fr_rpm, out);
    out << ", ";
  }

  // member: rl_rpm
  {
    out << "rl_rpm: ";
    rosidl_generator_traits::value_to_yaml(msg.rl_rpm, out);
    out << ", ";
  }

  // member: rr_rpm
  {
    out << "rr_rpm: ";
    rosidl_generator_traits::value_to_yaml(msg.rr_rpm, out);
    out << ", ";
  }

  // member: fl_rotation_angle
  {
    out << "fl_rotation_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.fl_rotation_angle, out);
    out << ", ";
  }

  // member: fr_rotation_angle
  {
    out << "fr_rotation_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.fr_rotation_angle, out);
    out << ", ";
  }

  // member: rl_rotation_angle
  {
    out << "rl_rotation_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.rl_rotation_angle, out);
    out << ", ";
  }

  // member: rr_rotation_angle
  {
    out << "rr_rotation_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.rr_rotation_angle, out);
    out << ", ";
  }

  // member: fl_steering_angle
  {
    out << "fl_steering_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.fl_steering_angle, out);
    out << ", ";
  }

  // member: fr_steering_angle
  {
    out << "fr_steering_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.fr_steering_angle, out);
    out << ", ";
  }

  // member: rl_steering_angle
  {
    out << "rl_steering_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.rl_steering_angle, out);
    out << ", ";
  }

  // member: rr_steering_angle
  {
    out << "rr_steering_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.rr_steering_angle, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const WheelStates & msg,
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

  // member: fl_rpm
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "fl_rpm: ";
    rosidl_generator_traits::value_to_yaml(msg.fl_rpm, out);
    out << "\n";
  }

  // member: fr_rpm
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "fr_rpm: ";
    rosidl_generator_traits::value_to_yaml(msg.fr_rpm, out);
    out << "\n";
  }

  // member: rl_rpm
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rl_rpm: ";
    rosidl_generator_traits::value_to_yaml(msg.rl_rpm, out);
    out << "\n";
  }

  // member: rr_rpm
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rr_rpm: ";
    rosidl_generator_traits::value_to_yaml(msg.rr_rpm, out);
    out << "\n";
  }

  // member: fl_rotation_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "fl_rotation_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.fl_rotation_angle, out);
    out << "\n";
  }

  // member: fr_rotation_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "fr_rotation_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.fr_rotation_angle, out);
    out << "\n";
  }

  // member: rl_rotation_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rl_rotation_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.rl_rotation_angle, out);
    out << "\n";
  }

  // member: rr_rotation_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rr_rotation_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.rr_rotation_angle, out);
    out << "\n";
  }

  // member: fl_steering_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "fl_steering_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.fl_steering_angle, out);
    out << "\n";
  }

  // member: fr_steering_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "fr_steering_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.fr_steering_angle, out);
    out << "\n";
  }

  // member: rl_steering_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rl_steering_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.rl_steering_angle, out);
    out << "\n";
  }

  // member: rr_steering_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rr_steering_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.rr_steering_angle, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const WheelStates & msg, bool use_flow_style = false)
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
  const fs_msgs::msg::WheelStates & msg,
  std::ostream & out, size_t indentation = 0)
{
  fs_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fs_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const fs_msgs::msg::WheelStates & msg)
{
  return fs_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<fs_msgs::msg::WheelStates>()
{
  return "fs_msgs::msg::WheelStates";
}

template<>
inline const char * name<fs_msgs::msg::WheelStates>()
{
  return "fs_msgs/msg/WheelStates";
}

template<>
struct has_fixed_size<fs_msgs::msg::WheelStates>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<fs_msgs::msg::WheelStates>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<fs_msgs::msg::WheelStates>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // FS_MSGS__MSG__DETAIL__WHEEL_STATES__TRAITS_HPP_
