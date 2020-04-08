#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from zope.container.interfaces import IContained

from nti.base.interfaces import ICreated
from nti.base.interfaces import ILastModified

from nti.coremetadata.interfaces import IShouldHaveTraversablePath


class ISiteLicense(IContained, ILastModified,
                   ICreated, IShouldHaveTraversablePath):
    """
    The base interface for a site license.
    """


class ITrialSiteLicense(ISiteLicense):
    """
    A license for a trial site.
    """


class IStarterSiteLicense(ISiteLicense):
    """
    A license for a starter site.
    """


class IGrowthSiteLicense(ISiteLicense):
    """
    A license for a growth site.
    """


class IEnterpriseSiteLicense(ISiteLicense):
    """
    A license for an enterprise site.
    """
