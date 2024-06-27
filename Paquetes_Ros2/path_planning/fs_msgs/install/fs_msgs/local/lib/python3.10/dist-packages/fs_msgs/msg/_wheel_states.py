# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fs_msgs:msg/WheelStates.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_WheelStates(type):
    """Metaclass of message 'WheelStates'."""

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
                'fs_msgs.msg.WheelStates')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__wheel_states
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__wheel_states
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__wheel_states
            cls._TYPE_SUPPORT = module.type_support_msg__msg__wheel_states
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__wheel_states

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class WheelStates(metaclass=Metaclass_WheelStates):
    """Message class 'WheelStates'."""

    __slots__ = [
        '_header',
        '_fl_rpm',
        '_fr_rpm',
        '_rl_rpm',
        '_rr_rpm',
        '_fl_rotation_angle',
        '_fr_rotation_angle',
        '_rl_rotation_angle',
        '_rr_rotation_angle',
        '_fl_steering_angle',
        '_fr_steering_angle',
        '_rl_steering_angle',
        '_rr_steering_angle',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'fl_rpm': 'float',
        'fr_rpm': 'float',
        'rl_rpm': 'float',
        'rr_rpm': 'float',
        'fl_rotation_angle': 'float',
        'fr_rotation_angle': 'float',
        'rl_rotation_angle': 'float',
        'rr_rotation_angle': 'float',
        'fl_steering_angle': 'float',
        'fr_steering_angle': 'float',
        'rl_steering_angle': 'float',
        'rr_steering_angle': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.fl_rpm = kwargs.get('fl_rpm', float())
        self.fr_rpm = kwargs.get('fr_rpm', float())
        self.rl_rpm = kwargs.get('rl_rpm', float())
        self.rr_rpm = kwargs.get('rr_rpm', float())
        self.fl_rotation_angle = kwargs.get('fl_rotation_angle', float())
        self.fr_rotation_angle = kwargs.get('fr_rotation_angle', float())
        self.rl_rotation_angle = kwargs.get('rl_rotation_angle', float())
        self.rr_rotation_angle = kwargs.get('rr_rotation_angle', float())
        self.fl_steering_angle = kwargs.get('fl_steering_angle', float())
        self.fr_steering_angle = kwargs.get('fr_steering_angle', float())
        self.rl_steering_angle = kwargs.get('rl_steering_angle', float())
        self.rr_steering_angle = kwargs.get('rr_steering_angle', float())

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
        if self.header != other.header:
            return False
        if self.fl_rpm != other.fl_rpm:
            return False
        if self.fr_rpm != other.fr_rpm:
            return False
        if self.rl_rpm != other.rl_rpm:
            return False
        if self.rr_rpm != other.rr_rpm:
            return False
        if self.fl_rotation_angle != other.fl_rotation_angle:
            return False
        if self.fr_rotation_angle != other.fr_rotation_angle:
            return False
        if self.rl_rotation_angle != other.rl_rotation_angle:
            return False
        if self.rr_rotation_angle != other.rr_rotation_angle:
            return False
        if self.fl_steering_angle != other.fl_steering_angle:
            return False
        if self.fr_steering_angle != other.fr_steering_angle:
            return False
        if self.rl_steering_angle != other.rl_steering_angle:
            return False
        if self.rr_steering_angle != other.rr_steering_angle:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if __debug__:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @builtins.property
    def fl_rpm(self):
        """Message field 'fl_rpm'."""
        return self._fl_rpm

    @fl_rpm.setter
    def fl_rpm(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'fl_rpm' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'fl_rpm' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._fl_rpm = value

    @builtins.property
    def fr_rpm(self):
        """Message field 'fr_rpm'."""
        return self._fr_rpm

    @fr_rpm.setter
    def fr_rpm(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'fr_rpm' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'fr_rpm' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._fr_rpm = value

    @builtins.property
    def rl_rpm(self):
        """Message field 'rl_rpm'."""
        return self._rl_rpm

    @rl_rpm.setter
    def rl_rpm(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'rl_rpm' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'rl_rpm' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._rl_rpm = value

    @builtins.property
    def rr_rpm(self):
        """Message field 'rr_rpm'."""
        return self._rr_rpm

    @rr_rpm.setter
    def rr_rpm(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'rr_rpm' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'rr_rpm' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._rr_rpm = value

    @builtins.property
    def fl_rotation_angle(self):
        """Message field 'fl_rotation_angle'."""
        return self._fl_rotation_angle

    @fl_rotation_angle.setter
    def fl_rotation_angle(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'fl_rotation_angle' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'fl_rotation_angle' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._fl_rotation_angle = value

    @builtins.property
    def fr_rotation_angle(self):
        """Message field 'fr_rotation_angle'."""
        return self._fr_rotation_angle

    @fr_rotation_angle.setter
    def fr_rotation_angle(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'fr_rotation_angle' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'fr_rotation_angle' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._fr_rotation_angle = value

    @builtins.property
    def rl_rotation_angle(self):
        """Message field 'rl_rotation_angle'."""
        return self._rl_rotation_angle

    @rl_rotation_angle.setter
    def rl_rotation_angle(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'rl_rotation_angle' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'rl_rotation_angle' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._rl_rotation_angle = value

    @builtins.property
    def rr_rotation_angle(self):
        """Message field 'rr_rotation_angle'."""
        return self._rr_rotation_angle

    @rr_rotation_angle.setter
    def rr_rotation_angle(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'rr_rotation_angle' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'rr_rotation_angle' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._rr_rotation_angle = value

    @builtins.property
    def fl_steering_angle(self):
        """Message field 'fl_steering_angle'."""
        return self._fl_steering_angle

    @fl_steering_angle.setter
    def fl_steering_angle(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'fl_steering_angle' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'fl_steering_angle' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._fl_steering_angle = value

    @builtins.property
    def fr_steering_angle(self):
        """Message field 'fr_steering_angle'."""
        return self._fr_steering_angle

    @fr_steering_angle.setter
    def fr_steering_angle(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'fr_steering_angle' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'fr_steering_angle' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._fr_steering_angle = value

    @builtins.property
    def rl_steering_angle(self):
        """Message field 'rl_steering_angle'."""
        return self._rl_steering_angle

    @rl_steering_angle.setter
    def rl_steering_angle(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'rl_steering_angle' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'rl_steering_angle' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._rl_steering_angle = value

    @builtins.property
    def rr_steering_angle(self):
        """Message field 'rr_steering_angle'."""
        return self._rr_steering_angle

    @rr_steering_angle.setter
    def rr_steering_angle(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'rr_steering_angle' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'rr_steering_angle' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._rr_steering_angle = value
