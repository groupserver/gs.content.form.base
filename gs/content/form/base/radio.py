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
from __future__ import absolute_import, unicode_literals
from zope.app.form.browser import RadioWidget
from zope.app.form.browser.widget import renderElement


class NotBrokenRadioWidget(RadioWidget):
    '''Radio Widget

The main difference between the standard radio widget and this radio
widget is the ``for`` attribute of the label is set in this radio
widget. This makes the widget easier to use, as it allows the radio
button to be toggled by clicking on the label.

To use this radio widget import ``radio_widget`` and assign it as the
``custom_widget`` for the field::
    formFields['basicPrivacy'].custom_widget = radio_widget'''
    _joinButtonToMessageTemplate = '<div class="radioItem">%s&nbsp;%s</div>\n'

    def renderItem(self, index, text, value, name, cssClass):
        widgetId = '%s.%s' % (name, index)
        elem = renderElement('input',
                             type="radio",
                             cssClass=cssClass,
                             name=name,
                             id=widgetId,
                             value=value)
        label = '<label class="radioLabel" for="%s">%s</label>' % (widgetId, text)
        return self._joinButtonToMessageTemplate % (elem, label)

    def renderSelectedItem(self, index, text, value, name, cssClass):
        """Render a selected item of the list."""
        widgetId = '%s.%s' % (name, index)
        elem = renderElement('input',
                             value=value,
                             name=name,
                             id=widgetId,
                             cssClass=cssClass,
                             checked="checked",
                             type='radio')
        label = '<label class="radioLabel" for="%s">%s</label>' % (widgetId, text)
        return self._joinButtonToMessageTemplate % (elem, label)


def radio_widget(field, request):
    '''Create a radio-widget with a clickable label.

:param field: The field that the radio-widget is created for.
:param request: The current HTTP request.
:returns: A radio widget.'''
    return NotBrokenRadioWidget(field, field.vocabulary, request)
