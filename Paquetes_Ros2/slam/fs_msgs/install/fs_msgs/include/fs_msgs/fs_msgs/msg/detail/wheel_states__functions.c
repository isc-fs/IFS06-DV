// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from fs_msgs:msg/WheelStates.idl
// generated code does not contain a copyright notice
#include "fs_msgs/msg/detail/wheel_states__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
fs_msgs__msg__WheelStates__init(fs_msgs__msg__WheelStates * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    fs_msgs__msg__WheelStates__fini(msg);
    return false;
  }
  // fl_rpm
  // fr_rpm
  // rl_rpm
  // rr_rpm
  // fl_rotation_angle
  // fr_rotation_angle
  // rl_rotation_angle
  // rr_rotation_angle
  // fl_steering_angle
  // fr_steering_angle
  // rl_steering_angle
  // rr_steering_angle
  return true;
}

void
fs_msgs__msg__WheelStates__fini(fs_msgs__msg__WheelStates * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // fl_rpm
  // fr_rpm
  // rl_rpm
  // rr_rpm
  // fl_rotation_angle
  // fr_rotation_angle
  // rl_rotation_angle
  // rr_rotation_angle
  // fl_steering_angle
  // fr_steering_angle
  // rl_steering_angle
  // rr_steering_angle
}

bool
fs_msgs__msg__WheelStates__are_equal(const fs_msgs__msg__WheelStates * lhs, const fs_msgs__msg__WheelStates * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // fl_rpm
  if (lhs->fl_rpm != rhs->fl_rpm) {
    return false;
  }
  // fr_rpm
  if (lhs->fr_rpm != rhs->fr_rpm) {
    return false;
  }
  // rl_rpm
  if (lhs->rl_rpm != rhs->rl_rpm) {
    return false;
  }
  // rr_rpm
  if (lhs->rr_rpm != rhs->rr_rpm) {
    return false;
  }
  // fl_rotation_angle
  if (lhs->fl_rotation_angle != rhs->fl_rotation_angle) {
    return false;
  }
  // fr_rotation_angle
  if (lhs->fr_rotation_angle != rhs->fr_rotation_angle) {
    return false;
  }
  // rl_rotation_angle
  if (lhs->rl_rotation_angle != rhs->rl_rotation_angle) {
    return false;
  }
  // rr_rotation_angle
  if (lhs->rr_rotation_angle != rhs->rr_rotation_angle) {
    return false;
  }
  // fl_steering_angle
  if (lhs->fl_steering_angle != rhs->fl_steering_angle) {
    return false;
  }
  // fr_steering_angle
  if (lhs->fr_steering_angle != rhs->fr_steering_angle) {
    return false;
  }
  // rl_steering_angle
  if (lhs->rl_steering_angle != rhs->rl_steering_angle) {
    return false;
  }
  // rr_steering_angle
  if (lhs->rr_steering_angle != rhs->rr_steering_angle) {
    return false;
  }
  return true;
}

bool
fs_msgs__msg__WheelStates__copy(
  const fs_msgs__msg__WheelStates * input,
  fs_msgs__msg__WheelStates * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // fl_rpm
  output->fl_rpm = input->fl_rpm;
  // fr_rpm
  output->fr_rpm = input->fr_rpm;
  // rl_rpm
  output->rl_rpm = input->rl_rpm;
  // rr_rpm
  output->rr_rpm = input->rr_rpm;
  // fl_rotation_angle
  output->fl_rotation_angle = input->fl_rotation_angle;
  // fr_rotation_angle
  output->fr_rotation_angle = input->fr_rotation_angle;
  // rl_rotation_angle
  output->rl_rotation_angle = input->rl_rotation_angle;
  // rr_rotation_angle
  output->rr_rotation_angle = input->rr_rotation_angle;
  // fl_steering_angle
  output->fl_steering_angle = input->fl_steering_angle;
  // fr_steering_angle
  output->fr_steering_angle = input->fr_steering_angle;
  // rl_steering_angle
  output->rl_steering_angle = input->rl_steering_angle;
  // rr_steering_angle
  output->rr_steering_angle = input->rr_steering_angle;
  return true;
}

fs_msgs__msg__WheelStates *
fs_msgs__msg__WheelStates__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fs_msgs__msg__WheelStates * msg = (fs_msgs__msg__WheelStates *)allocator.allocate(sizeof(fs_msgs__msg__WheelStates), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(fs_msgs__msg__WheelStates));
  bool success = fs_msgs__msg__WheelStates__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
fs_msgs__msg__WheelStates__destroy(fs_msgs__msg__WheelStates * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    fs_msgs__msg__WheelStates__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
fs_msgs__msg__WheelStates__Sequence__init(fs_msgs__msg__WheelStates__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fs_msgs__msg__WheelStates * data = NULL;

  if (size) {
    data = (fs_msgs__msg__WheelStates *)allocator.zero_allocate(size, sizeof(fs_msgs__msg__WheelStates), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = fs_msgs__msg__WheelStates__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        fs_msgs__msg__WheelStates__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
fs_msgs__msg__WheelStates__Sequence__fini(fs_msgs__msg__WheelStates__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      fs_msgs__msg__WheelStates__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

fs_msgs__msg__WheelStates__Sequence *
fs_msgs__msg__WheelStates__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fs_msgs__msg__WheelStates__Sequence * array = (fs_msgs__msg__WheelStates__Sequence *)allocator.allocate(sizeof(fs_msgs__msg__WheelStates__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = fs_msgs__msg__WheelStates__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
fs_msgs__msg__WheelStates__Sequence__destroy(fs_msgs__msg__WheelStates__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    fs_msgs__msg__WheelStates__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
fs_msgs__msg__WheelStates__Sequence__are_equal(const fs_msgs__msg__WheelStates__Sequence * lhs, const fs_msgs__msg__WheelStates__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!fs_msgs__msg__WheelStates__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
fs_msgs__msg__WheelStates__Sequence__copy(
  const fs_msgs__msg__WheelStates__Sequence * input,
  fs_msgs__msg__WheelStates__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(fs_msgs__msg__WheelStates);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    fs_msgs__msg__WheelStates * data =
      (fs_msgs__msg__WheelStates *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!fs_msgs__msg__WheelStates__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          fs_msgs__msg__WheelStates__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!fs_msgs__msg__WheelStates__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
