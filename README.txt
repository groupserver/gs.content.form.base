Introduction
============

This product contains many useful functions and classes for dealing with
``zope.formlib`` forms [#formlib]_ in `GroupServer`_.

``gs.content.form.SiteForm``:
  An abstract base-class for a that provides the ``siteInfo`` and
  ``loggedInUser`` properties.

``groupserver.FormStatusMessage``:
  A *content provider* for displaying the status-message of a form, after
  it submits.

``gs.content.form.radio_widget``:
  A factory for creating a non-broken radio-widget.

``gs.content.form.select_widget``:
  A factory for creating a select-widget that is slightly larger than the
  normal widget (15 items).

``gs.content.form.disabled_text_widget``:
  A factory for creating text widget that is always disabled.

.. [#formlib] See <http://docs.zope.org/zope.formlib/>
.. _GroupServer: http://groupserver.org/
