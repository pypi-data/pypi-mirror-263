import enum
from typing import Optional, Callable

class SpotflowError(Exception):
    pass

class DeviceClientOptions:
    def __init__(self,
                 database_file: str,
                 provisioning_token: ProvisioningToken,
                 device_id: Optional[str] = None) -> None: ...

    @property
    def database_file(self) -> str: ...

    @database_file.setter
    def database_file(self, value: str) -> None: ...

    @property
    def provisioning_token(self) -> ProvisioningToken: ...

    @provisioning_token.setter
    def provisioning_token(self, value: ProvisioningToken) -> None: ...

    @property
    def device_id(self) -> Optional[str]: ...

    @device_id.setter
    def device_id(self, value: Optional[str]) -> None: ...

    @property
    def instance(self) -> Optional[str]: ...

    @instance.setter
    def instance(self, value: Optional[str]) -> None: ...

    @property
    def display_provisioning_operation_callback(self) -> Optional[Callable[[ProvisioningOperation], None]]: ...

    @display_provisioning_operation_callback.setter
    def display_provisioning_operation_callback(self, value: Optional[Callable[[ProvisioningOperation], None]]) -> None: ...

    @property
    def desired_properties_updated_callback(self) -> Optional[Callable[[DesiredProperties], None]]: ...

    @desired_properties_updated_callback.setter
    def desired_properties_updated_callback(self, value: Optional[Callable[[DesiredProperties], None]]) -> None: ...

class ProvisioningToken:
    def __init__(self, token: str) -> None: ...

class ProvisioningOperation:
    def __init__(self) -> None: ...

    @property
    def id(self) -> str: ...

    @property
    def verification_code(self) -> str: ...

    @property
    def expiration_time(self) -> str: ...

class Compression(enum.Enum):
    UNCOMPRESSED = 0
    FASTEST = 1
    SMALLEST_SIZE = 2

class DeviceClient:
    @staticmethod
    def start(options: DeviceClientOptions) -> DeviceClient: ...

    @property
    def device_id(self) -> str: ...

    def create_stream_sender(self,
                             stream_group: Optional[str] = None,
                             stream: Optional[str] = None,
                             compression: Optional[Compression] = Compression.UNCOMPRESSED) -> StreamSender:
        ...

    @property
    def pending_messages_count(self) -> int: ...

    def get_desired_properties(self) -> DesiredProperties: ...

    def get_desired_properties_if_newer(self, version: Optional[int] = None) -> Optional[DesiredProperties]: ...

    def update_reported_properties(self, properties: dict) -> None: ...

    @property
    def any_pending_reported_properties_updates(self) -> bool: ...

class StreamSender:
    def send_message(self, 
                     payload: str | bytes,
                     batch_id: Optional[str] = None,
                     message_id: Optional[str] = None,
                     batch_slice_id: Optional[str] = None,
                     chunk_id: Optional[str] = None) -> None:
        ...

    def complete_batch(self, batch_id: str) -> None: ...

    def complete_message(self, batch_id: str, message_id: str) -> None: ...

class DesiredProperties:
    @property
    def version(self) -> int: ...

    @property
    def values(self) -> dict: ...
