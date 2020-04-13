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
from nti.base.interfaces import ITitledDescribed

from nti.coremetadata.interfaces import IShouldHaveTraversablePath

from nti.schema.field import TextLine


class ISiteLicense(IContained, ILastModified, ITitledDescribed,
                   ICreated, IShouldHaveTraversablePath):
    """
    The base interface for a site license.
    """

    version = TextLine(title=u"The site license version",
                       required=False)


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
