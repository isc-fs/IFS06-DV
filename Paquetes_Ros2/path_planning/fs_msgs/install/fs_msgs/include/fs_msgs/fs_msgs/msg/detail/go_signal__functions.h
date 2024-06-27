// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from fs_msgs:msg/GoSignal.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__GO_SIGNAL__FUNCTIONS_H_
#define FS_MSGS__MSG__DETAIL__GO_SIGNAL__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "fs_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "fs_msgs/msg/detail/go_signal__struct.h"

/// Initialize msg/GoSignal message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * fs_msgs__msg__GoSignal
 * )) before or use
 * fs_msgs__msg__GoSignal__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
bool
fs_msgs__msg__GoSignal__init(fs_msgs__msg__GoSignal * msg);

/// Finalize msg/GoSignal message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
void
fs_msgs__msg__GoSignal__fini(fs_msgs__msg__GoSignal * msg);

/// Create msg/GoSignal message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * fs_msgs__msg__GoSignal__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
fs_msgs__msg__GoSignal *
fs_msgs__msg__GoSignal__create();

/// Destroy msg/GoSignal message.
/**
 * It calls
 * fs_msgs__msg__GoSignal__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
void
fs_msgs__msg__GoSignal__destroy(fs_msgs__msg__GoSignal * msg);

/// Check for msg/GoSignal message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
bool
fs_msgs__msg__GoSignal__are_equal(const fs_msgs__msg__GoSignal * lhs, const fs_msgs__msg__GoSignal * rhs);

/// Copy a msg/GoSignal message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
bool
fs_msgs__msg__GoSignal__copy(
  const fs_msgs__msg__GoSignal * input,
  fs_msgs__msg__GoSignal * output);

/// Initialize array of msg/GoSignal messages.
/**
 * It allocates the memory for the number of elements and calls
 * fs_msgs__msg__GoSignal__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
bool
fs_msgs__msg__GoSignal__Sequence__init(fs_msgs__msg__GoSignal__Sequence * array, size_t size);

/// Finalize array of msg/GoSignal messages.
/**
 * It calls
 * fs_msgs__msg__GoSignal__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
void
fs_msgs__msg__GoSignal__Sequence__fini(fs_msgs__msg__GoSignal__Sequence * array);

/// Create array of msg/GoSignal messages.
/**
 * It allocates the memory for the array and calls
 * fs_msgs__msg__GoSignal__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
fs_msgs__msg__GoSignal__Sequence *
fs_msgs__msg__GoSignal__Sequence__create(size_t size);

/// Destroy array of msg/GoSignal messages.
/**
 * It calls
 * fs_msgs__msg__GoSignal__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
void
fs_msgs__msg__GoSignal__Sequence__destroy(fs_msgs__msg__GoSignal__Sequence * array);

/// Check for msg/GoSignal message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
bool
fs_msgs__msg__GoSignal__Sequence__are_equal(const fs_msgs__msg__GoSignal__Sequence * lhs, const fs_msgs__msg__GoSignal__Sequence * rhs);

/// Copy an array of msg/GoSignal messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
bool
fs_msgs__msg__GoSignal__Sequence__copy(
  const fs_msgs__msg__GoSignal__Sequence * input,
  fs_msgs__msg__GoSignal__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // FS_MSGS__MSG__DETAIL__GO_SIGNAL__FUNCTIONS_H_
