from abc import ABC, abstractmethod

from typing import (
    Dict,
    List,
    Literal,
    Optional,
    Tuple,
    TypedDict,
    Union,
    Any,
    Protocol,
    runtime_checkable,
    Callable,
    overload,
)

Callback = Callable[..., Any]


# database types
class Go2RtcFFMPEGSource(TypedDict):
    aac: str
    opus: str


class Go2RtcWSSource(TypedDict):
    webrtc: str


class Go2RtcRTSPSource(TypedDict):
    single: str
    default: str
    mp4: str


class Go2RtcEndpoint(TypedDict):
    webrtc: str
    mse: str
    lmp4: str
    mmp4: str
    mp4: str
    mp4Snapshot: str
    jpegSnapshot: str
    lHlsTs: str
    lHlsFmp4: str
    mHlsFmp4: str
    mjpeg: str
    mjpegHtml: str


class StreamUrls(TypedDict):
    ws: Go2RtcWSSource
    rtsp: Go2RtcRTSPSource
    transcoded: Go2RtcFFMPEGSource
    www: Go2RtcEndpoint


class CameraInput(TypedDict, total=False):
    _id: str
    name: str
    roles: List["CameraRoles"]
    urls: StreamUrls


CameraRoles = Literal["detect", "record", "stream", "snapshot", "none"]


class CameraZone(TypedDict):
    name: str
    regions: List["ZoneRegion"]


class ZoneRegion(TypedDict):
    _id: str
    coords: List["ZoneCoord"]


class ZoneCoord(TypedDict):
    _id: str
    points: Tuple[int, int]


class CameraInformation(TypedDict):
    model: str
    manufacturer: str
    hardware: str
    serialNumber: str
    firmwareVersion: str
    supportUrl: str


CameraType = Literal["camera", "doorbell"]


class BaseCamera(TypedDict, total=False):
    _id: str
    nativeId: Optional[str]
    pluginId: str
    name: str
    disabled: bool
    isCloud: bool
    hasLight: bool
    hasSiren: bool
    hasBinarySensor: bool
    hasBattery: bool
    info: CameraInformation
    type: CameraType
    motionZones: List[CameraZone]
    objectZones: List[CameraZone]


class Camera(BaseCamera):
    hasAudioDetector: bool
    hasMotionDetector: bool
    hasObjectDetector: bool
    hasPtz: bool
    sources: List[CameraInput]


# camera types
CameraExtension = Literal[
    "hub",
    "prebuffer",
    "motionDetection",
    "objectDetection",
    "audioDetection",
    "ptz",
    "intercom",
]


class BaseCameraConfig(TypedDict, total=False):
    name: str
    nativeId: Optional[str]
    isCloud: Optional[bool]
    hasLight: Optional[bool]
    hasSiren: Optional[bool]
    hasBinarySensor: Optional[bool]
    hasBattery: Optional[bool]
    disabled: Optional[bool]
    info: Optional[CameraInformation]


class CameraInputSettings(TypedDict, total=False):
    _id: str
    name: str
    roles: List[CameraRoles]
    urls: List[str]


class CameraConfigWithSources(BaseCameraConfig):
    sources: Optional[List[CameraInputSettings]]


class CameraConfigWithDelegate(BaseCameraConfig):
    delegate: Any


CameraConfig = Union[CameraConfigWithSources, CameraConfigWithDelegate]


# plugins types
PluginConfig = Dict[str, Union[str, int, bool]]


class JsonBaseSchema(TypedDict):
    type: str
    key: Optional[str]
    title: Optional[str]
    description: Optional[str]
    required: Optional[bool]
    readonly: Optional[bool]
    placeholder: Optional[str]
    hidden: Optional[bool]
    group: Optional[str]
    defaultValue: Optional[Union[str, int, bool]]


# Erweitertes Basis-Schema für Plugins
class PluginJsonBaseSchema(JsonBaseSchema):
    store: Optional[bool]
    onGet: Any
    onSet: Any


class PluginJsonSchemaString(PluginJsonBaseSchema):
    type: Literal["string"]
    format: Optional[str]
    minLength: Optional[int]
    maxLength: Optional[int]


class PluginJsonSchemaNumber(PluginJsonBaseSchema):
    type: Literal["number"]
    minimum: Optional[int]
    maximum: Optional[int]


class PluginJsonSchemaBoolean(PluginJsonBaseSchema):
    type: Literal["boolean"]


class PluginJsonSchemaEnum(PluginJsonBaseSchema):
    type: Literal["string"]
    enum: List[str]
    multiple: Optional[bool]


class PluginJsonSchemaObject(PluginJsonBaseSchema):
    type: Literal["object"]
    opened: Optional[bool]
    properties: Optional[Dict[str, "PluginJsonSchema"]]


PluginJsonSchema = Union[
    PluginJsonSchemaString,
    PluginJsonSchemaNumber,
    PluginJsonSchemaBoolean,
    PluginJsonSchemaEnum,
    PluginJsonSchemaObject,
]


class PluginJsonSchemaForm(TypedDict, total=False):
    pass


class PluginRootSchema(TypedDict):
    schema: PluginJsonSchemaForm


# json schema types
class JsonSchemaString(JsonBaseSchema):
    type: Literal["string"]
    format: Optional[str]
    minLength: Optional[int]
    maxLength: Optional[int]


class JsonSchemaNumber(JsonBaseSchema):
    type: Literal["number"]
    minimum: Optional[int]
    maximum: Optional[int]


class JsonSchemaBoolean(JsonBaseSchema):
    type: Literal["boolean"]


class JsonSchemaEnum(JsonBaseSchema):
    type: Literal["string"]
    enum: List[str]
    multiple: Optional[bool]


class JsonSchemaObject(JsonBaseSchema):
    type: Literal["object"]
    opened: Optional[bool]
    properties: Optional[Dict[str, "JsonSchema"]]


class JsonSchemaButton(TypedDict):
    label: str
    onSubmit: str


class JsonSchemaObjectWithButtons(JsonSchemaObject):
    buttons: Optional[Tuple[JsonSchemaButton, Optional[JsonSchemaButton]]]


class JsonSchemaAnyOf(TypedDict):
    anyOf: List["JsonSchema"]


class JsonSchemaArray(JsonBaseSchema):
    type: Literal["array"]
    opened: Optional[bool]
    items: Optional[Union["JsonSchema", JsonSchemaAnyOf]]


JsonSchema = Union[
    JsonSchemaString,
    JsonSchemaNumber,
    JsonSchemaBoolean,
    JsonSchemaEnum,
    JsonSchemaObject,
    JsonSchemaObjectWithButtons,
    JsonSchemaArray,
]


class JsonSchemaForm(TypedDict):
    pass


class RootSchema(TypedDict):
    schema: JsonSchemaForm


class SchemaConfig(TypedDict):
    rootSchema: PluginRootSchema
    config: Dict[str, Union[str, int, bool]]


# camera storage
@runtime_checkable
class CameraStorage(Protocol):
    async def initialize_storage(self) -> None: ...
    async def get_value(self, path: str, default_value: Any = None) -> Any: ...
    async def set_value(self, path: str, new_value: Any) -> None: ...
    def has_value(self, path: str) -> bool: ...
    async def get_config(self) -> SchemaConfig: ...
    async def set_config(self, new_config: Dict[str, Any]) -> None: ...
    async def add_schema(
        self,
        schema_or_path: Union[PluginJsonSchemaForm, str],
        schema: Optional[PluginJsonSchema] = None,
    ) -> None: ...
    def remove_schema(self, path: str) -> None: ...
    async def change_schema(self, path: str, new_schema: Dict[str, Any]) -> None: ...
    def get_schema(self, path: str) -> Optional[PluginJsonSchema]: ...
    def has_schema(self, path: str) -> bool: ...
    async def _resolve_on_get_functions(
        self,
        schema: Union[PluginJsonSchemaForm, PluginJsonSchema],
        base_schema_path: str = "",
    ) -> None: ...
    async def _resolve_on_get_functions_for_object(
        self,
        schema: PluginJsonSchemaForm,
        base_schema_path: str,
    ) -> None: ...
    async def _resolve_on_get_functions_for_schema(self, schema_path: str) -> None: ...
    async def _trigger_on_set_for_changes(
        self,
        old_config: Dict[str, Any],
        new_config: Dict[str, Any],
        path: str = "",
    ) -> None: ...
    def _filter_storable_values(
        self,
        schema: PluginJsonSchemaForm,
        base_schema_path: str = "",
        result: Dict[str, Any] = {},
    ) -> Dict[str, Any]: ...
    def _contains_storable_schema(
        self,
        schema: Union[PluginJsonSchemaForm, PluginJsonSchema],
    ) -> bool: ...
    def _save_db(self) -> None: ...
    def _remove_db(self) -> None: ...


# storage controller
@runtime_checkable
class StorageController(Protocol):
    async def create_camera_storage(
        self,
        instance: Any,
        camera_id: str,
        schema: Optional[PluginJsonSchemaForm] = None,
    ) -> CameraStorage: ...
    def get_camera_storage(self, camera_id: str) -> Optional[CameraStorage]: ...
    def remove_camera_storage(self, camera_id: str) -> None: ...


# logger
@runtime_checkable
class PluginLogger(Protocol):
    def log(self, *args: Union[str, dict, Exception]) -> None: ...
    def error(self, *args: Union[str, dict, Exception]) -> None: ...
    def warn(self, *args: Union[str, dict, Exception]) -> None: ...
    def attention(self, *args: Union[str, dict, Exception]) -> None: ...
    def debug(self, *args: Union[str, dict, Exception]) -> None: ...
    def trace(self, *args: Union[str, dict, Exception]) -> None: ...


# config service
@runtime_checkable
class PluginConfigService(Protocol):
    def get(
        self,
        key: str,
        default: Optional[Any] = None,
        validate: Optional[Callable[[Any], bool]] = None,
        refresh: bool = False,
        write_if_not_valid: bool = False,
    ) -> Any: ...

    def has(self, key: str, refresh: bool = False) -> bool: ...
    def ensure_exists(
        self, key: str, default: Optional[Any] = None, write: bool = False
    ) -> None: ...
    def set(self, key: str, value: Any, write: bool = False) -> None: ...
    def insert(
        self, key: str, value: Any, index: Optional[int] = None, write: bool = False
    ) -> None: ...
    def push(self, key: str, *values: Any, write: bool = False) -> None: ...
    def delete(self, key: str, write: bool = False) -> None: ...
    def all(self, refresh: bool = False) -> Dict[str, Any]: ...
    def replace(self, new_config: Dict[str, Any], write: bool = False) -> None: ...
    def update_value(
        self,
        path: str,
        search_key: str,
        search_value: Any,
        target_key: str,
        new_value: Any,
        write: bool = False,
    ) -> None: ...
    def replace_or_add_item(
        self,
        path: str,
        search_key: str,
        search_value: Any,
        new_item: Any,
        write: bool = False,
    ) -> None: ...


# manager todo: improve typing
@runtime_checkable
class SystemManager(Protocol):
    def on(self, event: str, listener: Callable) -> "SystemManager": ...
    def once(self, event: str, listener: Callable) -> "SystemManager": ...
    def remove_listener(self, event: str, listener: Callable) -> "SystemManager": ...
    def remove_all_listeners(self, event: str) -> "SystemManager": ...


@runtime_checkable
class PluginsManager(Protocol):  # todo: add methods
    def on(self, event: str, listener: Callable) -> "PluginsManager": ...
    def once(self, event: str, listener: Callable) -> "PluginsManager": ...
    def remove_listener(self, event: str, listener: Callable) -> "PluginsManager": ...
    def remove_all_listeners(self, event: str) -> "PluginsManager": ...


@runtime_checkable
class CameraDevice(Protocol):  # todo
    pass


# device manager
DeviceManagerEventType = Literal[
    "cameraSelected",
    "cameraDeselected",
    "cameraAdded",
    "cameraRemoved",
    "cameraUpdated",
]

CameraSelectedCallback = Callable[[CameraDevice, CameraExtension], None]
CameraDeselectedCallback = Callable[[str, CameraExtension], None]
CameraAddedCallback = Callable[[CameraDevice], None]
CameraRemovedCallback = Callable[[str], None]
CameraUpdatedCallback = Callable[[str, CameraDevice], None]


@runtime_checkable
class DeviceManager(Protocol):  # todo: add methods
    @overload
    def on(
        self, event: Literal["cameraSelected"], listener: CameraSelectedCallback
    ) -> "DeviceManager": ...
    @overload
    def on(
        self, event: Literal["cameraDeselected"], listener: CameraDeselectedCallback
    ) -> "DeviceManager": ...
    @overload
    def on(
        self, event: Literal["cameraAdded"], listener: CameraAddedCallback
    ) -> "DeviceManager": ...
    @overload
    def on(
        self, event: Literal["cameraRemoved"], listener: CameraRemovedCallback
    ) -> "DeviceManager": ...
    @overload
    def on(
        self, event: Literal["cameraUpdated"], listener: CameraUpdatedCallback
    ) -> "DeviceManager": ...

    @overload
    def once(
        self, event: Literal["cameraSelected"], listener: CameraSelectedCallback
    ) -> "DeviceManager": ...
    @overload
    def once(
        self, event: Literal["cameraDeselected"], listener: CameraDeselectedCallback
    ) -> "DeviceManager": ...
    @overload
    def once(
        self, event: Literal["cameraAdded"], listener: CameraAddedCallback
    ) -> "DeviceManager": ...
    @overload
    def once(
        self, event: Literal["cameraRemoved"], listener: CameraRemovedCallback
    ) -> "DeviceManager": ...
    @overload
    def once(
        self, event: Literal["cameraUpdated"], listener: CameraUpdatedCallback
    ) -> "DeviceManager": ...

    @overload
    def remove_listener(
        self, event: Literal["cameraSelected"], listener: CameraSelectedCallback
    ) -> "DeviceManager": ...
    @overload
    def remove_listener(
        self, event: Literal["cameraDeselected"], listener: CameraDeselectedCallback
    ) -> "DeviceManager": ...
    @overload
    def remove_listener(
        self, event: Literal["cameraAdded"], listener: CameraAddedCallback
    ) -> "DeviceManager": ...
    @overload
    def remove_listener(
        self, event: Literal["cameraRemoved"], listener: CameraRemovedCallback
    ) -> "DeviceManager": ...
    @overload
    def remove_listener(
        self, event: Literal["cameraUpdated"], listener: CameraUpdatedCallback
    ) -> "DeviceManager": ...

    def remove_all_listeners(
        self, event: Optional[DeviceManagerEventType] = None
    ) -> "DeviceManager": ...


# plugin api
APIEventType = Literal["finishLaunching", "shutdown"]


@runtime_checkable
class PluginAPI(Protocol):
    storage_path: str
    config_file: str
    config_service: PluginConfigService
    storage_controller: StorageController
    device_manager: DeviceManager
    system_manager: SystemManager
    plugins_manager: PluginsManager

    def on(self, event: APIEventType, listener: Callable) -> "PluginAPI": ...
    def once(self, event: APIEventType, listener: Callable) -> "PluginAPI": ...
    def remove_listener(
        self, event: APIEventType, listener: Callable
    ) -> "PluginAPI": ...
    def remove_all_listeners(
        self, event: Optional[APIEventType] = None
    ) -> "PluginAPI": ...


# base plugin
class BasePlugin(ABC):
    @abstractmethod
    async def on_form_submit(self, action_id: str, payload: Any) -> Optional[dict]:
        pass

    @abstractmethod
    def configure_cameras(
        self, cameras: List[Any]
    ) -> None:  # todo: replace Any with Camera Device
        pass
