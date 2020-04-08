#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id: model.py 123306 2017-10-19 03:47:14Z carlos.sanchez $
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from zope.container.contained import Contained

from zope import interface

from nti.dublincore.datastructures import PersistentCreatedModDateTrackingObject

from nti.externalization.representation import WithRepr

from nti.schema.fieldproperty import createDirectFieldProperties

from nti.schema.schema import SchemaConfigured

from nti.site.license.interfaces import ITrialSiteLicense
from nti.site.license.interfaces import IGrowthSiteLicense
from nti.site.license.interfaces import IStarterSiteLicense
from nti.site.license.interfaces import IEnterpriseSiteLicense


logger = __import__('logging').getLogger(__name__)


class AbstractSiteLicense(PersistentCreatedModDateTrackingObject,
                          Contained, SchemaConfigured):

    __parent__ = None
    __name__ = None


@WithRepr
@interface.implementer(ITrialSiteLicense)
class TrialSiteLicense(AbstractSiteLicense):
    createDirectFieldProperties(ITrialSiteLicense)

    mimeType = mime_type = "application/vnd.nextthought.site.triallicense"


@WithRepr
@interface.implementer(IStarterSiteLicense)
class StarterSiteLicense(AbstractSiteLicense):
    createDirectFieldProperties(IStarterSiteLicense)

    mimeType = mime_type = "application/vnd.nextthought.site.starterlicense"


@WithRepr
@interface.implementer(IGrowthSiteLicense)
class GrowthSiteLicense(AbstractSiteLicense):
    createDirectFieldProperties(IGrowthSiteLicense)

    mimeType = mime_type = "application/vnd.nextthought.site.growthlicense"


@WithRepr
@interface.implementer(IEnterpriseSiteLicense)
class EnterpriseSiteLicense(AbstractSiteLicense):
    createDirectFieldProperties(IEnterpriseSiteLicense)

    mimeType = mime_type = "application/vnd.nextthought.site.enterpriselicense"
