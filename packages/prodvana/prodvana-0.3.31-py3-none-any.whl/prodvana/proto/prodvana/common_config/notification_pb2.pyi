"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class NotificationConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class Slack(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        CHANNEL_FIELD_NUMBER: builtins.int
        channel: builtins.str
        def __init__(
            self,
            *,
            channel: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["channel", b"channel"]) -> None: ...

    SLACK_FIELD_NUMBER: builtins.int
    @property
    def slack(self) -> global___NotificationConfig.Slack: ...
    def __init__(
        self,
        *,
        slack: global___NotificationConfig.Slack | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["slack", b"slack"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["slack", b"slack"]) -> None: ...

global___NotificationConfig = NotificationConfig
