"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _FeatureType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _FeatureTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_FeatureType.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN: _FeatureType.ValueType  # 0
    EXPOSED_SERVICE: _FeatureType.ValueType  # 1
    TLS_SERVICE: _FeatureType.ValueType  # 2
    COST_ANALYSIS: _FeatureType.ValueType  # 3
    DATADOG: _FeatureType.ValueType  # 4
    ARGO_ROLLOUTS: _FeatureType.ValueType  # 5

class FeatureType(_FeatureType, metaclass=_FeatureTypeEnumTypeWrapper): ...

UNKNOWN: FeatureType.ValueType  # 0
EXPOSED_SERVICE: FeatureType.ValueType  # 1
TLS_SERVICE: FeatureType.ValueType  # 2
COST_ANALYSIS: FeatureType.ValueType  # 3
DATADOG: FeatureType.ValueType  # 4
ARGO_ROLLOUTS: FeatureType.ValueType  # 5
global___FeatureType = FeatureType
