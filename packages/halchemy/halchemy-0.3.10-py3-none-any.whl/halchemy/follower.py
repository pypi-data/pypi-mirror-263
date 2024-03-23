from .resource import HalResource
from .requester import Requester


class Follower:
    def __init__(self, api, resource: HalResource):
        self.api = api
        self.resource = resource

    def to(self, rel):
        return Requester(self.api, (self.resource, rel))
