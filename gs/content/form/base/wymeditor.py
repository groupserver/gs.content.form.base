# coding=utf-8
from __future__ import absolute_import, unicode_literals
from zope.app.form.browser import TextAreaWidget


def wym_editor_widget(field, request):
    retval = TextAreaWidget(field, request)
    retval.cssClass = 'wymeditor'
    return retval
