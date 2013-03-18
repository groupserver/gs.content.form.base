===================
``gs.content.form``
===================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Form support for GroupServer pages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2013-03-18
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 3.0 New Zealand License`_
  by `OnlineGroups.Net`_.

Introduction
============

This product contains many useful functions and classes for dealing with
``zope.formlib`` forms [#formlib]_ in `GroupServer`_.

* An `abstract base class`_ for forms,
* A standard `status message`_ content provider, and
* Some widgets_ that enhance the forms.

Abstract Base Class
===================

The abstract base-class ``gs.content.form.SiteForm`` is a Zope ``PageForm``
provides the ``siteInfo`` and ``loggedInUser`` properties::

  from gs.content.form.form import SiteForm

  class Change(SiteForm):
      def __init__(self, context, request):
          super(Change, self).__init__(context, request)

Status Message
==============

The content provider ``groupserver.FormStatusMessage`` displays the status
of a form (``self.status`` and ``self.errors``), after it submits. It
provides a standard markup for the form, and normally sits in the
``messages`` slot::

    <tal:block content="structure provider:groupserver.FormStatusMessage"
      define="errors view/errors; status view/status; widgets view/widgets"
      metal:fill-slot="messages">&#160;</tal:block>

Widgets
=======

Four custom widgets are provided: `radio buttons`_, `check boxes`_, a
select_, and a `disabled text`_ entry.

Radio Buttons
-------------

The widget ``gs.content.form.radio_widget`` is a variant of the standard
``zope.formlib`` raido button, but it has the correct association between
the label and the button::


  from gs.content.form import radio_widget

  ...

      @Lazy
      def form_fields(self):
          retval = form.Fields(IChange, render_context=False)
          retval['field'].custom_widget = radio_widget

Check Boxes
-----------

Rather than a select_, it is often nicer to present a list of
checkboxes. This is especially true if the user is supposed to select
*multiple* items (which is normally done using the *Control* key in a
select-box, but few people know this). The
``gs.content.form.multi_check_box_widget`` widget displays a list of
checkboxes based on a vocabulary::

  from gs.content.form import multi_check_box_widget

  ...

      @Lazy
      def form_fields(self):
          retval = form.Fields(IChange, render_context=False)
          retval['field'].custom_widget = multi_check_box_widget


Select
------

The standard Zope select widget annoying sets the size too small. The
``gs.content.form.select_widget`` creates a select box that shows 15
items. If fewer items are desired then `radio buttons`_ or `check boxes`_
should be used::

  from gs.content.form import select_widget

  ...

      @Lazy
      def form_fields(self):
          retval = form.Fields(IChange, render_context=False)
          retval['field'].custom_widget = select_widget

Disabled Text
-------------
  
The ``gs.content.form.disabled_text_widget`` factory creates a text widget
that has the CSS class set to ``disabled``.

Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.content.form
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
.. _Creative Commons Attribution-Share Alike 3.0 New Zealand License:
   http://creativecommons.org/licenses/by-sa/3.0/nz/

.. [#formlib] See <http://docs.zope.org/zope.formlib/>
