# -*- coding:utf-8 -*-

"""
WPTools Request module
~~~~~~~~~~~~~~~~~~~~~~

Makes WMF API HTTP requests.
"""

from __future__ import print_function

import requests

from . import __title__, __contact__, __version__


class WPToolsRequest(object):
    """
    WPToolsRequest class
    """

    DISABLED = False  # disable requests when testing

    info = None
    silent = False

    def __init__(self, silent=False, verbose=False, proxy=None, timeout=None):
        """
        Returns a WPToolsRequest object.

        Arguments:
        - [proxy]: <str> HTTP proxy to use
        - [silent]: <bool> silent if True
        - [timeout]: <int> connection timeout (0=wait forever)
        - [verbose]: <bool> verbose if True
        """
        self.silent = silent
        self.verbose = verbose

    def get(self, url, status):
        """
        in favor of python-requests for speed
        """

        # consistently faster than requests by 3x
        #
        r = requests.get(url,
                         headers={'User-Agent': user_agent()})
        return r.text


def user_agent():
    """
    returns the wptools user-agent string
    """
    return "%s/%s (%s) 1.0" % (__title__,
                               __version__,
                               __contact__)
