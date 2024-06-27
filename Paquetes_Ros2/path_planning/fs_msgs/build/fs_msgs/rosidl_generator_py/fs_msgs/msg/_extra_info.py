# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fs_msgs:msg/ExtraInfo.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'laps'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ExtraInfo(type):
    """Metaclass of message 'ExtraInfo'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('fs_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'fs_msgs.msg.ExtraInfo')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__extra_info
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__extra_info
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__extra_info
            cls._TYPE_SUPPORT = module.type_support_msg__msg__extra_info
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__extra_info

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ExtraInfo(metaclass=Metaclass_ExtraInfo):
    """Message class 'ExtraInfo'."""

    __slots__ = [
        '_doo_counter',
        '_laps',
    ]

    _fields_and_field_types = {
        'doo_counter': 'uint32',
        'laps': 'sequence<float>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.doo_counter = kwargs.get('doo_counter', int())
        self.laps = array.array('f', kwargs.get('laps', []))

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.doo_counter != other.doo_counter:
            return False
        if self.laps != other.laps:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def doo_counter(self):
        """Message field 'doo_counter'."""
        return self._doo_counter

    @doo_counter.setter
    def doo_counter(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'doo_counter' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'doo_counter' field must be an unsigned integer in [0, 4294967295]"
        self._doo_counter = value

    @builtins.property
    def laps(self):
        """Message field 'laps'."""
        return self._laps

    @laps.setter
    def laps(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'laps' array.array() must have the type code of 'f'"
            self._laps = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'laps' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._laps = array.array('f', value)
