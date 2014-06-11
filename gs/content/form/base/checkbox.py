# -*- coding: utf-8 -*-
##############################################################################
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
##############################################################################
from __future__ import unicode_literals
from zope.app.form.browser import MultiCheckBoxWidget
from zope.app.form.browser.widget import renderElement


class NotBrokenMultiCheckBoxWidget(MultiCheckBoxWidget):
    _joinButtonToMessageTemplate = \
        '<span class="checkboxGroup" id="checkboxgroup-%s">%s&nbsp;%s</span>'

    def renderItem(self, index, text, value, name, cssClass):
        widgetId = '%s.%s' % (name, index)
        elem = renderElement('input',
                             type="checkbox",
                             cssClass=cssClass,
                             name=name,
                             id=widgetId,
                             value=value)
        label = '<label class="checkboxLabel" for="%s">%s</label>' % \
          (widgetId, text)
        gId = widgetId.replace('.', '-')

        return self._joinButtonToMessageTemplate % (gId, elem, label)

    def renderSelectedItem(self, index, text, value, name, cssClass):
        widgetId = '%s.%s' % (name, index)
        elem = renderElement('input',
                             type="checkbox",
                             cssClass=cssClass,
                             name=name,
                             id=widgetId,
                             value=value,
                             checked="checked")
        label = '<label class="checkboxLabel" for="%s">%s</label>' % \
          (widgetId, text)
        gId = widgetId.replace('.', '-')
        return self._joinButtonToMessageTemplate % (gId, elem, label)


def multi_check_box_widget(field, request):
    return NotBrokenMultiCheckBoxWidget(field,
                                        field.value_type.vocabulary,
                                        request)
