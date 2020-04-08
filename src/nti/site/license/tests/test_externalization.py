#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# pylint: disable=protected-access,too-many-public-methods,arguments-differ

from hamcrest import is_
from hamcrest import not_none
from hamcrest import assert_that

from nti.testing.matchers import validly_provides
from nti.testing.matchers import verifiably_provides

import unittest

from nti.externalization.externalization import to_external_object
from nti.externalization.interfaces import StandardExternalFields

from nti.externalization.internalization import update_from_external_object

from nti.externalization.internalization import find_factory_for

from nti.site.license.interfaces import ITrialSiteLicense

from nti.site.license.license import TrialSiteLicense

from nti.site.license.tests import SharedConfiguringTestLayer

CLASS = StandardExternalFields.CLASS
ITEMS = StandardExternalFields.ITEMS
MIMETYPE = StandardExternalFields.MIMETYPE


class TestCompletion(unittest.TestCase):

    layer = SharedConfiguringTestLayer

    def test_externalization(self):
        trial_license = TrialSiteLicense()

        assert_that(trial_license, validly_provides(ITrialSiteLicense))
        assert_that(trial_license, verifiably_provides(ITrialSiteLicense))

        ext_obj = to_external_object(trial_license)
        assert_that(ext_obj[CLASS], is_('TrialSiteLicense'))
        assert_that(ext_obj[MIMETYPE],
                    is_('application/vnd.nextthought.site.triallicense'))
        assert_that(ext_obj['CreatedTime'], not_none())
        assert_that(ext_obj['Last Modified'], not_none)

        factory = find_factory_for(ext_obj)
        assert_that(factory, not_none())
        new_io = factory()
        update_from_external_object(new_io, ext_obj, require_updater=True)
