# coding: utf-8

from __future__ import annotations

from pathlib import Path


class Nim(object):
    def __init__(self, args, config):
        self._args = args
        self._config = config

    @property
    def code(self):
        path = Path('/data4/nim/bin/scallop')
        return path.read_bytes()


