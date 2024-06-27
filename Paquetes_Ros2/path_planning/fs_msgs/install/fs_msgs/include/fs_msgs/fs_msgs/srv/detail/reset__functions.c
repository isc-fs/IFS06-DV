// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from fs_msgs:srv/Reset.idl
// generated code does not contain a copyright notice
#include "fs_msgs/srv/detail/reset__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
fs_msgs__srv__Reset_Request__init(fs_msgs__srv__Reset_Request * msg)
{
  if (!msg) {
    return false;
  }
  // wait_on_last_task
  return true;
}

void
fs_msgs__srv__Reset_Request__fini(fs_msgs__srv__Reset_Request * msg)
{
  if (!msg) {
    return;
  }
  // wait_on_last_task
}

bool
fs_msgs__srv__Reset_Request__are_equal(const fs_msgs__srv__Reset_Request * lhs, const fs_msgs__srv__Reset_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // wait_on_last_task
  if (lhs->wait_on_last_task != rhs->wait_on_last_task) {
    return false;
  }
  return true;
}

bool
fs_msgs__srv__Reset_Request__copy(
  const fs_msgs__srv__Reset_Request * input,
  fs_msgs__srv__Reset_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // wait_on_last_task
  output->wait_on_last_task = input->wait_on_last_task;
  return true;
}

fs_msgs__srv__Reset_Request *
fs_msgs__srv__Reset_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fs_msgs__srv__Reset_Request * msg = (fs_msgs__srv__Reset_Request *)allocator.allocate(sizeof(fs_msgs__srv__Reset_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(fs_msgs__srv__Reset_Request));
  bool success = fs_msgs__srv__Reset_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
fs_msgs__srv__Reset_Request__destroy(fs_msgs__srv__Reset_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    fs_msgs__srv__Reset_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
fs_msgs__srv__Reset_Request__Sequence__init(fs_msgs__srv__Reset_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fs_msgs__srv__Reset_Request * data = NULL;

  if (size) {
    data = (fs_msgs__srv__Reset_Request *)allocator.zero_allocate(size, sizeof(fs_msgs__srv__Reset_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = fs_msgs__srv__Reset_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        fs_msgs__srv__Reset_Request__fini(&data[i - 1]);
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
fs_msgs__srv__Reset_Request__Sequence__fini(fs_msgs__srv__Reset_Request__Sequence * array)
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
      fs_msgs__srv__Reset_Request__fini(&array->data[i]);
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

fs_msgs__srv__Reset_Request__Sequence *
fs_msgs__srv__Reset_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fs_msgs__srv__Reset_Request__Sequence * array = (fs_msgs__srv__Reset_Request__Sequence *)allocator.allocate(sizeof(fs_msgs__srv__Reset_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = fs_msgs__srv__Reset_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
fs_msgs__srv__Reset_Request__Sequence__destroy(fs_msgs__srv__Reset_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    fs_msgs__srv__Reset_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
fs_msgs__srv__Reset_Request__Sequence__are_equal(const fs_msgs__srv__Reset_Request__Sequence * lhs, const fs_msgs__srv__Reset_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!fs_msgs__srv__Reset_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
fs_msgs__srv__Reset_Request__Sequence__copy(
  const fs_msgs__srv__Reset_Request__Sequence * input,
  fs_msgs__srv__Reset_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(fs_msgs__srv__Reset_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    fs_msgs__srv__Reset_Request * data =
      (fs_msgs__srv__Reset_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!fs_msgs__srv__Reset_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          fs_msgs__srv__Reset_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!fs_msgs__srv__Reset_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
fs_msgs__srv__Reset_Response__init(fs_msgs__srv__Reset_Response * msg)
{
  if (!msg) {
    return false;
  }
  // structure_needs_at_least_one_member
  return true;
}

void
fs_msgs__srv__Reset_Response__fini(fs_msgs__srv__Reset_Response * msg)
{
  if (!msg) {
    return;
  }
  // structure_needs_at_least_one_member
}

bool
fs_msgs__srv__Reset_Response__are_equal(const fs_msgs__srv__Reset_Response * lhs, const fs_msgs__srv__Reset_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // structure_needs_at_least_one_member
  if (lhs->structure_needs_at_least_one_member != rhs->structure_needs_at_least_one_member) {
    return false;
  }
  return true;
}

bool
fs_msgs__srv__Reset_Response__copy(
  const fs_msgs__srv__Reset_Response * input,
  fs_msgs__srv__Reset_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // structure_needs_at_least_one_member
  output->structure_needs_at_least_one_member = input->structure_needs_at_least_one_member;
  return true;
}

fs_msgs__srv__Reset_Response *
fs_msgs__srv__Reset_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fs_msgs__srv__Reset_Response * msg = (fs_msgs__srv__Reset_Response *)allocator.allocate(sizeof(fs_msgs__srv__Reset_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(fs_msgs__srv__Reset_Response));
  bool success = fs_msgs__srv__Reset_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
fs_msgs__srv__Reset_Response__destroy(fs_msgs__srv__Reset_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    fs_msgs__srv__Reset_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
fs_msgs__srv__Reset_Response__Sequence__init(fs_msgs__srv__Reset_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fs_msgs__srv__Reset_Response * data = NULL;

  if (size) {
    data = (fs_msgs__srv__Reset_Response *)allocator.zero_allocate(size, sizeof(fs_msgs__srv__Reset_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = fs_msgs__srv__Reset_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        fs_msgs__srv__Reset_Response__fini(&data[i - 1]);
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
fs_msgs__srv__Reset_Response__Sequence__fini(fs_msgs__srv__Reset_Response__Sequence * array)
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
      fs_msgs__srv__Reset_Response__fini(&array->data[i]);
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

fs_msgs__srv__Reset_Response__Sequence *
fs_msgs__srv__Reset_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fs_msgs__srv__Reset_Response__Sequence * array = (fs_msgs__srv__Reset_Response__Sequence *)allocator.allocate(sizeof(fs_msgs__srv__Reset_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = fs_msgs__srv__Reset_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
fs_msgs__srv__Reset_Response__Sequence__destroy(fs_msgs__srv__Reset_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    fs_msgs__srv__Reset_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
fs_msgs__srv__Reset_Response__Sequence__are_equal(const fs_msgs__srv__Reset_Response__Sequence * lhs, const fs_msgs__srv__Reset_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!fs_msgs__srv__Reset_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
fs_msgs__srv__Reset_Response__Sequence__copy(
  const fs_msgs__srv__Reset_Response__Sequence * input,
  fs_msgs__srv__Reset_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(fs_msgs__srv__Reset_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    fs_msgs__srv__Reset_Response * data =
      (fs_msgs__srv__Reset_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!fs_msgs__srv__Reset_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          fs_msgs__srv__Reset_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!fs_msgs__srv__Reset_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
