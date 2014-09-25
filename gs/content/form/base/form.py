# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import unicode_literals
from abc import abstractproperty
from zope.component import createObject
from zope.cachedescriptors.property import Lazy
try:
    from five.formlib.formbase import PageForm
except ImportError:
    from Products.Five.formlib.formbase import PageForm  # lint:ok


class SiteForm(PageForm):
    '''An abstract base-class for forms on a site

:param object context: The context of the form.
:param object request: The current HTTP request.'''
    def __init__(self, context, request):
        super(PageForm, self).__init__(context, request)

    @abstractproperty
    def form_fields(self):
        'The form fields. **Must be set** by concrete classes.'

    @Lazy
    def siteInfo(self):
        '''Information about the current site.'''
        retval = createObject('groupserver.SiteInfo', self.context)
        return retval

    @Lazy
    def loggedInUser(self):
        '''Information about the currently logged-in user.'''
        retval = createObject('groupserver.LoggedInUser', self.context)
        return retval
