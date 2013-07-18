# coding=utf-8
"""Interfaces for the the help viewlets pages."""
from zope.interface.interface import Interface
from zope.schema import Text, ASCIILine, Field, Bool
from zope.contentprovider.interfaces import IContentProvider

class IFormStatus(IContentProvider):
    errors = Field(title=u'Errors',
        description=u'The errors, if any',
        required=True)

    status = Text(title=u'Status',
        description=u'The status of the form.',
        required=True)

    widgets = Field(title=u'Widgets',
        description=u'The widg',
        required=True)

    pageTemplateFileName = Text(title=u"Page Template File Name",
        description=u'The name of the ZPT file that is used to '\
        u'render the status message.',
        required=False,
        default=u"browser/templates/statusmessage.pt")

    showPageErrors = Bool(title=u"Show Page Errors",
        description=u'If True, the content provider will display page level '\
        u'errors. Otherwise, page errors will not be displayed.',
        required=False,
        default=False)

    showWidgetErrors = Bool(title=u"Show Widget Errors",
        description=u'If True, the content provider will display all of their'\
        u'errors associated with widgets on the page. Otherwise, errors'\
        u'associated with widgets will not be displayed.',
        required=False,
        default=True)

