import string
import typing
from EndpointType import EndpointType


class EndpointConfig:

    def __init__(self, endpoint: string, endpoint_type: EndpointType = EndpointType.GRPC):
        """

        :param endpoint: must be
        :param endpoint_type:
        """
        self.endpointType = endpoint_type
        self.endpoint = endpoint
