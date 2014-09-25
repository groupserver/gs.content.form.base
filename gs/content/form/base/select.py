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
from zope.app.form.browser import SelectWidget


def select_widget(field, request):
    '''Create a select-widget that is larget than normal

:param field: The field that the radio-widget is created for.
:param request: The current HTTP request.
:returns: A select widget.
:rtype: :class:`zope.app.form.brower.SelectWidget`'''
    retval = SelectWidget(field, field.vocabulary, request)
    retval.size = 15  # Because there are a lot of items.
    return retval
