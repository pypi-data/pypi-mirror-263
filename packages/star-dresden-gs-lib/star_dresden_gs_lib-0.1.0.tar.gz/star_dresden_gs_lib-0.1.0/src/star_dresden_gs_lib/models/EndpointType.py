from enum import Enum


class EndpointType(Enum):
    GRPC = 1
    REST = 2
    OTHER = 3
