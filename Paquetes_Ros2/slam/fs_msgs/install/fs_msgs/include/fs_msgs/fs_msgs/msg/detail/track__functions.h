// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from fs_msgs:msg/Track.idl
// generated code does not contain a copyright notice

#ifndef FS_MSGS__MSG__DETAIL__TRACK__FUNCTIONS_H_
#define FS_MSGS__MSG__DETAIL__TRACK__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "fs_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "fs_msgs/msg/detail/track__struct.h"

/// Initialize msg/Track message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * fs_msgs__msg__Track
 * )) before or use
 * fs_msgs__msg__Track__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
bool
fs_msgs__msg__Track__init(fs_msgs__msg__Track * msg);

/// Finalize msg/Track message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
void
fs_msgs__msg__Track__fini(fs_msgs__msg__Track * msg);

/// Create msg/Track message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * fs_msgs__msg__Track__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
fs_msgs__msg__Track *
fs_msgs__msg__Track__create();

/// Destroy msg/Track message.
/**
 * It calls
 * fs_msgs__msg__Track__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
void
fs_msgs__msg__Track__destroy(fs_msgs__msg__Track * msg);

/// Check for msg/Track message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
bool
fs_msgs__msg__Track__are_equal(const fs_msgs__msg__Track * lhs, const fs_msgs__msg__Track * rhs);

/// Copy a msg/Track message.
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
fs_msgs__msg__Track__copy(
  const fs_msgs__msg__Track * input,
  fs_msgs__msg__Track * output);

/// Initialize array of msg/Track messages.
/**
 * It allocates the memory for the number of elements and calls
 * fs_msgs__msg__Track__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
bool
fs_msgs__msg__Track__Sequence__init(fs_msgs__msg__Track__Sequence * array, size_t size);

/// Finalize array of msg/Track messages.
/**
 * It calls
 * fs_msgs__msg__Track__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
void
fs_msgs__msg__Track__Sequence__fini(fs_msgs__msg__Track__Sequence * array);

/// Create array of msg/Track messages.
/**
 * It allocates the memory for the array and calls
 * fs_msgs__msg__Track__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
fs_msgs__msg__Track__Sequence *
fs_msgs__msg__Track__Sequence__create(size_t size);

/// Destroy array of msg/Track messages.
/**
 * It calls
 * fs_msgs__msg__Track__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
void
fs_msgs__msg__Track__Sequence__destroy(fs_msgs__msg__Track__Sequence * array);

/// Check for msg/Track message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_fs_msgs
bool
fs_msgs__msg__Track__Sequence__are_equal(const fs_msgs__msg__Track__Sequence * lhs, const fs_msgs__msg__Track__Sequence * rhs);

/// Copy an array of msg/Track messages.
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
fs_msgs__msg__Track__Sequence__copy(
  const fs_msgs__msg__Track__Sequence * input,
  fs_msgs__msg__Track__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // FS_MSGS__MSG__DETAIL__TRACK__FUNCTIONS_H_
