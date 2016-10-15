# -*- coding: utf-8 -*-
from __future__ import (print_function, unicode_literals, division, absolute_import)

class Request():
    def __init__(self, project, token, package, block, params, base_endpoint):
        self.project = project
        self.token = token
        self.package = package
        self.block = block
        self.params = params
        self.base_endpoint = base_endpoint

        return self.call


    @property
    def urlBuilder(self):
        return self.base_endpoint + self.package + "/" + self.block

    @property
    def call(self):
        return self.urlBuilder