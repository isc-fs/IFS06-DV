# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fs_msgs:msg/Cone.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Cone(type):
    """Metaclass of message 'Cone'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'BLUE': 0,
        'YELLOW': 1,
        'ORANGE_BIG': 2,
        'ORANGE_SMALL': 3,
        'UNKNOWN': 4,
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
                'fs_msgs.msg.Cone')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__cone
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__cone
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__cone
            cls._TYPE_SUPPORT = module.type_support_msg__msg__cone
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__cone

            from geometry_msgs.msg import Point
            if Point.__class__._TYPE_SUPPORT is None:
                Point.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'BLUE': cls.__constants['BLUE'],
            'YELLOW': cls.__constants['YELLOW'],
            'ORANGE_BIG': cls.__constants['ORANGE_BIG'],
            'ORANGE_SMALL': cls.__constants['ORANGE_SMALL'],
            'UNKNOWN': cls.__constants['UNKNOWN'],
        }

    @property
    def BLUE(self):
        """Message constant 'BLUE'."""
        return Metaclass_Cone.__constants['BLUE']

    @property
    def YELLOW(self):
        """Message constant 'YELLOW'."""
        return Metaclass_Cone.__constants['YELLOW']

    @property
    def ORANGE_BIG(self):
        """Message constant 'ORANGE_BIG'."""
        return Metaclass_Cone.__constants['ORANGE_BIG']

    @property
    def ORANGE_SMALL(self):
        """Message constant 'ORANGE_SMALL'."""
        return Metaclass_Cone.__constants['ORANGE_SMALL']

    @property
    def UNKNOWN(self):
        """Message constant 'UNKNOWN'."""
        return Metaclass_Cone.__constants['UNKNOWN']


class Cone(metaclass=Metaclass_Cone):
    """
    Message class 'Cone'.

    Constants:
      BLUE
      YELLOW
      ORANGE_BIG
      ORANGE_SMALL
      UNKNOWN
    """

    __slots__ = [
        '_location',
        '_color',
    ]

    _fields_and_field_types = {
        'location': 'geometry_msgs/Point',
        'color': 'uint8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from geometry_msgs.msg import Point
        self.location = kwargs.get('location', Point())
        self.color = kwargs.get('color', int())

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
        if self.location != other.location:
            return False
        if self.color != other.color:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def location(self):
        """Message field 'location'."""
        return self._location

    @location.setter
    def location(self, value):
        if __debug__:
            from geometry_msgs.msg import Point
            assert \
                isinstance(value, Point), \
                "The 'location' field must be a sub message of type 'Point'"
        self._location = value

    @builtins.property
    def color(self):
        """Message field 'color'."""
        return self._color

    @color.setter
    def color(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'color' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'color' field must be an unsigned integer in [0, 255]"
        self._color = value
