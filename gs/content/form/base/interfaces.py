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
from zope.schema import Text, Field, Bool
from zope.contentprovider.interfaces import IContentProvider


class IFormStatus(IContentProvider):
    errors = Field(
        title='Errors',
        description='The errors, if any',
        required=True)

    status = Text(
        title='Status',
        description='The status of the form.',
        required=True)

    widgets = Field(
        title='Widgets',
        description='The widgets',
        required=True)

    pageTemplateFileName = Text(
        title="Page Template File Name",
        description='The name of the ZPT file that is used to '
                    'render the status message.',
        required=False,
        default="browser/templates/statusmessage.pt")

    showPageErrors = Bool(
        title="Show Page Errors",
        description='If True, the content provider will display page level '
                    'errors. Otherwise, page errors will not be displayed.',
        required=False,
        default=False)

    showWidgetErrors = Bool(
        title="Show Widget Errors",
        description='If True, the content provider will display all of '
                    'their errors associated with widgets on the page. '
                    'Otherwise, errors associated with widgets will not '
                    'be displayed.',
        required=False,
        default=True)
