#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id: model.py 123306 2017-10-19 03:47:14Z carlos.sanchez $
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from zope import component

from nti.site_license.interfaces import ISiteLicense

logger = __import__('logging').getLogger(__name__)


def get_site_license_feature_policy(feature_policy_iface, site_license=None):
    """
    Fetch the corresponding feature policy adapter given by
    `feature_policy_iface`, using the current :class:`ISiteLicense`
    in play. If none, is found, this function returns `None`.
    """
    if not site_license:
        site_license = component.queryUtility(ISiteLicense)
    if not site_license:
        return
    # First we query for a named adapter keyed off the site license
    # version. If not, we fall back to a regular adapter.
    result = None
    if site_license.version:
        result = component.queryAdapter(site_license,
                                        feature_policy_iface,
                                        name=site_license.version)
    if result is None:
        result = feature_policy_iface(site_license, None)
    return result

