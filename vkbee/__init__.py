# -*- coding: utf-8 -*-
# author: asyncvk

from .vkbee import VkApi
from .exceptions import *

import sentry_sdk
sentry_sdk.init("https://330aa4e647684d3093dc58c85a1a98c0@sentry.io/3199835")

__copyright__ = "2020"
__version__ = "0.1"
__authors__ = ["YamkaFox", "sergeyfillipov1"]
