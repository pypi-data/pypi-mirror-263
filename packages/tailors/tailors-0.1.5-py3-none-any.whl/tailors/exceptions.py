# -*- coding: utf-8 -*-


class TailorsError(Exception):
    """Raise on issues in config/class/params in train/val/infer loops..."""


class InvalidExample(Exception):
    """Raise on issues invalid train/val example"""
