# -*- coding: utf-8 -*-
#
# Licensed under the terms of the BSD 3-Clause
# (see cdlclient/LICENSE for details)

"""
DataLab Simple Client
=====================

DataLab Simple Client (`cdlclient`) is a Python library providing a proxy to `DataLab`_
application through XML-RPC protocol.

.. _DataLab: https://datalab-platform.com/
"""

# pylint: disable=unused-import
from cdlclient.baseproxy import SimpleBaseProxy  # noqa: F401
from cdlclient.remote import SimpleRemoteProxy  # noqa: F401

__version__ = "0.10.0"
__required_server_version__ = "0.14.2"
__docurl__ = "https://cdlclient.readthedocs.io/en/latest/"
__homeurl__ = "https://github.com/DataLab-Platform/DataLabSimpleClient/"
