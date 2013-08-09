# -*- coding: utf-8 -*-
from abc import abstractproperty
from zope.component import createObject
from zope.cachedescriptors.property import Lazy
try:
    from five.formlib.formbase import PageForm
except ImportError:
    from Products.Five.formlib.formbase import PageForm  # lint:ok


class SiteForm(PageForm):
    def __init__(self, context, request):
        super(PageForm, self).__init__(context, request)

    @abstractproperty
    def form_fields(self):
        u'The form fields.'

    @Lazy
    def siteInfo(self):
        retval = createObject('groupserver.SiteInfo', self.context)
        return retval

    @Lazy
    def loggedInUser(self):
        retval = createObject('groupserver.LoggedInUser', self.context)
        return retval
