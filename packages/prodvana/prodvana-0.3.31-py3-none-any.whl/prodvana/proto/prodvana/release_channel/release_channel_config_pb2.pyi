"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import prodvana.proto.prodvana.common_config.constants_pb2
import prodvana.proto.prodvana.common_config.env_pb2
import prodvana.proto.prodvana.common_config.maturity_pb2
import prodvana.proto.prodvana.labels.labels_pb2
import prodvana.proto.prodvana.pipelines.pipelines_pb2
import prodvana.proto.prodvana.protection.attachments_pb2
import prodvana.proto.prodvana.runtimes.runtimes_config_pb2
import prodvana.proto.prodvana.workflow.integration_config_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _RuntimeConnectionType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _RuntimeConnectionTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_RuntimeConnectionType.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN_CONNECTION: _RuntimeConnectionType.ValueType  # 0
    LONG_LIVED_COMPUTE: _RuntimeConnectionType.ValueType  # 1
    EXTENSION: _RuntimeConnectionType.ValueType  # 2
    AWS_ECS: _RuntimeConnectionType.ValueType  # 3
    GOOGLE_CLOUD_RUN: _RuntimeConnectionType.ValueType  # 4

class RuntimeConnectionType(_RuntimeConnectionType, metaclass=_RuntimeConnectionTypeEnumTypeWrapper): ...

UNKNOWN_CONNECTION: RuntimeConnectionType.ValueType  # 0
LONG_LIVED_COMPUTE: RuntimeConnectionType.ValueType  # 1
EXTENSION: RuntimeConnectionType.ValueType  # 2
AWS_ECS: RuntimeConnectionType.ValueType  # 3
GOOGLE_CLOUD_RUN: RuntimeConnectionType.ValueType  # 4
global___RuntimeConnectionType = RuntimeConnectionType

class Policy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class DefaultEnvEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> prodvana.proto.prodvana.common_config.env_pb2.EnvValue: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: prodvana.proto.prodvana.common_config.env_pb2.EnvValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    DEFAULT_ENV_FIELD_NUMBER: builtins.int
    @property
    def default_env(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, prodvana.proto.prodvana.common_config.env_pb2.EnvValue]: ...
    def __init__(
        self,
        *,
        default_env: collections.abc.Mapping[builtins.str, prodvana.proto.prodvana.common_config.env_pb2.EnvValue] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["default_env", b"default_env"]) -> None: ...

global___Policy = Policy

class ReleaseChannelConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    GROUP_FIELD_NUMBER: builtins.int
    ORDER_FIELD_NUMBER: builtins.int
    MATURITY_FIELD_NUMBER: builtins.int
    POLICY_FIELD_NUMBER: builtins.int
    RUNTIMES_FIELD_NUMBER: builtins.int
    DEPLOY_ANNOTATIONS_FIELD_NUMBER: builtins.int
    PRECONDITIONS_FIELD_NUMBER: builtins.int
    PROTECTIONS_FIELD_NUMBER: builtins.int
    CONVERGENCE_PROTECTIONS_FIELD_NUMBER: builtins.int
    SERVICE_INSTANCE_PROTECTIONS_FIELD_NUMBER: builtins.int
    CONSTANTS_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    DISABLE_ALL_PROTECTIONS_FIELD_NUMBER: builtins.int
    name: builtins.str
    """intentionally does not reference cluster - this allows us to copy release channels across clusters via the same config"""
    group: builtins.str
    """if specified, this release channel is part of a group. This can affect how release channels are rendered on the Prodvana web interface."""
    order: builtins.int
    """deprecated"""
    maturity: prodvana.proto.prodvana.common_config.maturity_pb2.Maturity.ValueType
    """deprecated"""
    @property
    def policy(self) -> global___Policy: ...
    @property
    def runtimes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ReleaseChannelRuntimeConfig]: ...
    @property
    def deploy_annotations(self) -> prodvana.proto.prodvana.workflow.integration_config_pb2.AnnotationsConfig: ...
    @property
    def preconditions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Precondition]: ...
    @property
    def protections(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[prodvana.proto.prodvana.protection.attachments_pb2.ProtectionAttachmentConfig]: ...
    @property
    def convergence_protections(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[prodvana.proto.prodvana.protection.attachments_pb2.ProtectionAttachmentConfig]: ...
    @property
    def service_instance_protections(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[prodvana.proto.prodvana.protection.attachments_pb2.ProtectionAttachmentConfig]:
        """protections that all service instances in this release channel should get"""
    @property
    def constants(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[prodvana.proto.prodvana.common_config.constants_pb2.Constant]:
        """constants made available in template substitutions"""
    @property
    def labels(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[prodvana.proto.prodvana.labels.labels_pb2.LabelDefinition]: ...
    disable_all_protections: builtins.bool
    """Disable all protections for this release channel - protections will not be created for any service instances in this release channel.
    This is useful for release channels that are used for testing or are not yet in production (e.g., fast creation of new tenants).
    """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        group: builtins.str = ...,
        order: builtins.int = ...,
        maturity: prodvana.proto.prodvana.common_config.maturity_pb2.Maturity.ValueType = ...,
        policy: global___Policy | None = ...,
        runtimes: collections.abc.Iterable[global___ReleaseChannelRuntimeConfig] | None = ...,
        deploy_annotations: prodvana.proto.prodvana.workflow.integration_config_pb2.AnnotationsConfig | None = ...,
        preconditions: collections.abc.Iterable[global___Precondition] | None = ...,
        protections: collections.abc.Iterable[prodvana.proto.prodvana.protection.attachments_pb2.ProtectionAttachmentConfig] | None = ...,
        convergence_protections: collections.abc.Iterable[prodvana.proto.prodvana.protection.attachments_pb2.ProtectionAttachmentConfig] | None = ...,
        service_instance_protections: collections.abc.Iterable[prodvana.proto.prodvana.protection.attachments_pb2.ProtectionAttachmentConfig] | None = ...,
        constants: collections.abc.Iterable[prodvana.proto.prodvana.common_config.constants_pb2.Constant] | None = ...,
        labels: collections.abc.Iterable[prodvana.proto.prodvana.labels.labels_pb2.LabelDefinition] | None = ...,
        disable_all_protections: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["deploy_annotations", b"deploy_annotations", "policy", b"policy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["constants", b"constants", "convergence_protections", b"convergence_protections", "deploy_annotations", b"deploy_annotations", "disable_all_protections", b"disable_all_protections", "group", b"group", "labels", b"labels", "maturity", b"maturity", "name", b"name", "order", b"order", "policy", b"policy", "preconditions", b"preconditions", "protections", b"protections", "runtimes", b"runtimes", "service_instance_protections", b"service_instance_protections"]) -> None: ...

global___ReleaseChannelConfig = ReleaseChannelConfig

class Precondition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class ReleaseChannelStable(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        RELEASE_CHANNEL_FIELD_NUMBER: builtins.int
        SELECTOR_FIELD_NUMBER: builtins.int
        ALLOW_EMPTY_FIELD_NUMBER: builtins.int
        release_channel: builtins.str
        selector: builtins.str
        allow_empty: builtins.bool
        """if selector is used, allow selector to return an empty list of release channels"""
        def __init__(
            self,
            *,
            release_channel: builtins.str = ...,
            selector: builtins.str = ...,
            allow_empty: builtins.bool = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["release_channel", b"release_channel", "selector", b"selector", "stable_oneof", b"stable_oneof"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["allow_empty", b"allow_empty", "release_channel", b"release_channel", "selector", b"selector", "stable_oneof", b"stable_oneof"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["stable_oneof", b"stable_oneof"]) -> typing_extensions.Literal["release_channel", "selector"] | None: ...

    class ManualApproval(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        DESCRIPTION_FIELD_NUMBER: builtins.int
        EVERY_ACTION_FIELD_NUMBER: builtins.int
        name: builtins.str
        description: builtins.str
        every_action: builtins.bool
        """request approval on every apply action, not just the first.
        only works for runtime extensions, will do nothing for kubernetes services.
        """
        def __init__(
            self,
            *,
            name: builtins.str = ...,
            description: builtins.str = ...,
            every_action: builtins.bool = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "every_action", b"every_action", "name", b"name"]) -> None: ...

    class CustomTask(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TASK_NAME_FIELD_NUMBER: builtins.int
        CUSTOM_TASK_FIELD_NUMBER: builtins.int
        task_name: builtins.str
        @property
        def custom_task(self) -> prodvana.proto.prodvana.pipelines.pipelines_pb2.CustomTask: ...
        def __init__(
            self,
            *,
            task_name: builtins.str = ...,
            custom_task: prodvana.proto.prodvana.pipelines.pipelines_pb2.CustomTask | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["custom_task", b"custom_task"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["custom_task", b"custom_task", "task_name", b"task_name"]) -> None: ...

    class SharedManualApproval(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        name: builtins.str
        def __init__(
            self,
            *,
            name: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

    RELEASE_CHANNEL_STABLE_FIELD_NUMBER: builtins.int
    MANUAL_APPROVAL_FIELD_NUMBER: builtins.int
    CUSTOM_TASK_FIELD_NUMBER: builtins.int
    SHARED_MANUAL_APPROVAL_FIELD_NUMBER: builtins.int
    @property
    def release_channel_stable(self) -> global___Precondition.ReleaseChannelStable: ...
    @property
    def manual_approval(self) -> global___Precondition.ManualApproval: ...
    @property
    def custom_task(self) -> global___Precondition.CustomTask: ...
    @property
    def shared_manual_approval(self) -> global___Precondition.SharedManualApproval: ...
    def __init__(
        self,
        *,
        release_channel_stable: global___Precondition.ReleaseChannelStable | None = ...,
        manual_approval: global___Precondition.ManualApproval | None = ...,
        custom_task: global___Precondition.CustomTask | None = ...,
        shared_manual_approval: global___Precondition.SharedManualApproval | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["custom_task", b"custom_task", "manual_approval", b"manual_approval", "precondition", b"precondition", "release_channel_stable", b"release_channel_stable", "shared_manual_approval", b"shared_manual_approval"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["custom_task", b"custom_task", "manual_approval", b"manual_approval", "precondition", b"precondition", "release_channel_stable", b"release_channel_stable", "shared_manual_approval", b"shared_manual_approval"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["precondition", b"precondition"]) -> typing_extensions.Literal["release_channel_stable", "manual_approval", "custom_task", "shared_manual_approval"] | None: ...

global___Precondition = Precondition

class ReleaseChannelRuntimeConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RUNTIME_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    CONTAINER_ORCHESTRATION_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    runtime: builtins.str
    name: builtins.str
    """Optional identifier for this runtime connection within this release channel,
    useful if the release channel has multiple runtimes of the same type.
    Defaults to the value of `runtime``.
    """
    @property
    def container_orchestration(self) -> prodvana.proto.prodvana.runtimes.runtimes_config_pb2.ContainerOrchestrationRuntime: ...
    type: global___RuntimeConnectionType.ValueType
    """set internally by prodvana, overridden even if set manually."""
    def __init__(
        self,
        *,
        runtime: builtins.str = ...,
        name: builtins.str = ...,
        container_orchestration: prodvana.proto.prodvana.runtimes.runtimes_config_pb2.ContainerOrchestrationRuntime | None = ...,
        type: global___RuntimeConnectionType.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["capability", b"capability", "container_orchestration", b"container_orchestration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["capability", b"capability", "container_orchestration", b"container_orchestration", "name", b"name", "runtime", b"runtime", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["capability", b"capability"]) -> typing_extensions.Literal["container_orchestration"] | None: ...

global___ReleaseChannelRuntimeConfig = ReleaseChannelRuntimeConfig

class ReleaseChannelGroupGeneratorConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    RUNTIME_SELECTOR_FIELD_NUMBER: builtins.int
    ALLOW_EMPTY_FIELD_NUMBER: builtins.int
    TEMPLATE_FIELD_NUMBER: builtins.int
    name: builtins.str
    runtime_selector: builtins.str
    """label selector for runtimes to generate release channels for.
    One release channel will be generated for each runtime that matches this selector.
    The selector will automatically be intersected with "@type=runtime".
    """
    allow_empty: builtins.bool
    """By default, if the runtime selector returns an empty list of runtimes, Prodvana will error out.
    Set allow_empty to true to explicitly allow the selector to return an empty list.
    """
    @property
    def template(self) -> global___ReleaseChannelConfig:
        """optionally customize how the release channel will be generated.
        Template variables .Builtins.Group an d.Builtins.Runtime are available.
        Any value specified here will be merged with:
        name: {{.Builtins.Group}}-{{.Builtins.Runtime.Name}}
        group: {{.Builtins.Group}}
        runtimes:
        - runtime: {{Builtins.Runtime.Name}}
        """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        runtime_selector: builtins.str = ...,
        allow_empty: builtins.bool = ...,
        template: global___ReleaseChannelConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["template", b"template"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["allow_empty", b"allow_empty", "name", b"name", "runtime_selector", b"runtime_selector", "template", b"template"]) -> None: ...

global___ReleaseChannelGroupGeneratorConfig = ReleaseChannelGroupGeneratorConfig
