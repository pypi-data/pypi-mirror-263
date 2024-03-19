from typing import Dict, Any


class Endpoints(object):
    """
    A Singleton containing a dictionary with string keys and endpoint values
    currently not in use
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Endpoints, cls).__new__(cls)
            cls._endpoints_dict = {}
        return cls._instance

    def __add__(self, other: Dict[str, Any]):
        """
        allows you to add a dictionary by using + because why not
        :param other: a dictionary with string key and either string or function as value
        :return:
        """

    def __getitem__(self, key: str) -> Any | None:
        """
        returns the item found at the given key using obj[key] as accessor
        :param key: a string key corresponding to a dictionary
        :return: either the endpoint corresponding to the key or None
        """
        if key in self._endpoints_dict.keys():
            return self._endpoints_dict.get(key)

    def __setitem__(self, key, value):
        """
        sets the enpoint the item at the given key using obj[key]=value as accessor
        :param key: a string key corresponding to a dictionary
        :return:
        """
        self._endpoints_dict[key] = value

    def update_dict(self, other: Dict[str, Any]):
        """
        updates the Endpoints using a dictionary with endpoints
        :param other: a dictionary with string keys and endpoints as values
        :return:
        """
        self._endpoints_dict.update(other)

    def add_endpoint(self, key: str, value: Any):
        self._endpoints_dict[key] = value

    def get_endpoint(self, key: str) -> Any | None:
        if key in self._endpoints_dict.keys():
            return self._endpoints_dict.get(key)

    def get_all_endpoint(self):
        """
        gets all registered endpoints
        :return: all currently registered endpoints as a dict
        """
        return self._endpoints_dict.copy()
