// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fs_msgs:srv/Reset.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__SRV__DETAIL__RESET__TRAITS_HPP_
#define FS_MSGS__SRV__DETAIL__RESET__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "fs_msgs/srv/detail/reset__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace fs_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const Reset_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: wait_on_last_task
  {
    out << "wait_on_last_task: ";
    rosidl_generator_traits::value_to_yaml(msg.wait_on_last_task, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Reset_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: wait_on_last_task
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "wait_on_last_task: ";
    rosidl_generator_traits::value_to_yaml(msg.wait_on_last_task, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Reset_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace fs_msgs

namespace rosidl_generator_traits
{

[[deprecated("use fs_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const fs_msgs::srv::Reset_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  fs_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fs_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const fs_msgs::srv::Reset_Request & msg)
{
  return fs_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<fs_msgs::srv::Reset_Request>()
{
  return "fs_msgs::srv::Reset_Request";
}

template<>
inline const char * name<fs_msgs::srv::Reset_Request>()
{
  return "fs_msgs/srv/Reset_Request";
}

template<>
struct has_fixed_size<fs_msgs::srv::Reset_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<fs_msgs::srv::Reset_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<fs_msgs::srv::Reset_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace fs_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const Reset_Response & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Reset_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Reset_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace fs_msgs

namespace rosidl_generator_traits
{

[[deprecated("use fs_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const fs_msgs::srv::Reset_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  fs_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fs_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const fs_msgs::srv::Reset_Response & msg)
{
  return fs_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<fs_msgs::srv::Reset_Response>()
{
  return "fs_msgs::srv::Reset_Response";
}

template<>
inline const char * name<fs_msgs::srv::Reset_Response>()
{
  return "fs_msgs/srv/Reset_Response";
}

template<>
struct has_fixed_size<fs_msgs::srv::Reset_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<fs_msgs::srv::Reset_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<fs_msgs::srv::Reset_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<fs_msgs::srv::Reset>()
{
  return "fs_msgs::srv::Reset";
}

template<>
inline const char * name<fs_msgs::srv::Reset>()
{
  return "fs_msgs/srv/Reset";
}

template<>
struct has_fixed_size<fs_msgs::srv::Reset>
  : std::integral_constant<
    bool,
    has_fixed_size<fs_msgs::srv::Reset_Request>::value &&
    has_fixed_size<fs_msgs::srv::Reset_Response>::value
  >
{
};

template<>
struct has_bounded_size<fs_msgs::srv::Reset>
  : std::integral_constant<
    bool,
    has_bounded_size<fs_msgs::srv::Reset_Request>::value &&
    has_bounded_size<fs_msgs::srv::Reset_Response>::value
  >
{
};

template<>
struct is_service<fs_msgs::srv::Reset>
  : std::true_type
{
};

template<>
struct is_service_request<fs_msgs::srv::Reset_Request>
  : std::true_type
{
};

template<>
struct is_service_response<fs_msgs::srv::Reset_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // FS_MSGS__SRV__DETAIL__RESET__TRAITS_HPP_
