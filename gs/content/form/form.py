# -*- coding: utf-8 -*-
from zope.component import createObject
from zope.cachedescriptors.property import Lazy
try:
    from five.formlib.formbase import PageForm
except ImportError:
    from Products.Five.formlib.formbase import PageForm  # lint:ok


class SiteForm(PageForm):
    def __init__(self, context, request):
        super(PageForm, self).__init__(context, request)

    @Lazy
    def siteInfo(self):
        retval = createObject('groupserver.SiteInfo', self.context)
        return retval

    @Lazy
    def loggedInUser(self):
        retval = createObject('groupserver.LoggedInUser', self.context)
        return retval
