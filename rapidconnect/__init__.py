# -*- coding: utf-8 -*-

from __future__ import (print_function, unicode_literals, division, absolute_import)

from rapidconnect.settings import DEFAULT_BASE_ENDPOINT
from rapidconnect.request  import Request


class RapidConnect(object):

    def __init__(self, project, token, base_endpoint=DEFAULT_BASE_ENDPOINT):
        self.project = project
        self.token = token
        self.base_endpoint = base_endpoint

    def call(self, package, block, params):
        request = Request(project=self.project,
                          token=self.token,
                          package=package,
                          block=block,
                          params=params,
                          base_endpoint=self.base_endpoint)

        return request.call