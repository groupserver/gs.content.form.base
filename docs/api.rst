:mod:`gs.content.form.base` API Reference
=========================================

The package exports the following API symbols.

.. _siteform:

Site form
---------

The abstract base-class ``gs.content.form.SiteForm`` is a Zope
``PageForm`` provides the ``siteInfo`` and ``loggedInUser``
properties.

.. autoclass: gs.content.form.base.SiteForm
   :members:

Example
~~~~~~~

.. code-block:: python

  from gs.content.form.form import SiteForm

  class Change(SiteForm):
      def __init__(self, context, request):
          super(Change, self).__init__(context, request)

.. _widgets:

Widgets
-------

Four custom widgets are provided: `radio buttons`_, `check
boxes`_, a select_, and a `disabled text`_ entry.

Radio buttons
~~~~~~~~~~~~~

The widget :func:`gs.content.form.base.radio_widget` is a variant
of the standard :mod:`zope.formlib` raido button, but it has the
correct association between the label and the button.

.. autofunction:: gs.content.form.base.radio_widget

Example
'''''''

.. code-block:: python

    @Lazy
    def form_fields(self):
        retval = form.Fields(IChange, render_context=False)
        retval['field'].custom_widget = radio_widget

Check Boxes
~~~~~~~~~~~

Rather than a select_, it is often nicer to present a list of
checkboxes. This is especially true if the user is supposed to
select *multiple* items (which is normally done using the
*Control* key in a select-box, but few people know this). The
:func:`gs.content.form.base.multi_check_box_widget` widget
displays a list of checkboxes based on a vocabulary

.. autofunction:: gs.content.form.base.multi_check_box_widget

Example
'''''''

.. code-block:: python

    @Lazy
    def form_fields(self):
        retval = form.Fields(IChange, render_context=False)
        retval['field'].custom_widget = multi_check_box_widget

Select
~~~~~~

The standard Zope select widget annoying sets the size too
small. The :func:`gs.content.form.base.select_widget` creates a
select box that shows 15 items. If fewer items are desired then
`radio buttons`_ or `check boxes`_ should be used:

.. autofunction:: gs.content.form.base.select_widget

Example
'''''''

.. code-block:: python

    @Lazy
    def form_fields(self):
        retval = form.Fields(IChange, render_context=False)
        retval['field'].custom_widget = select_widget

Disabled Text
~~~~~~~~~~~~~
  
The ``gs.content.form.base.disabled_text_widget`` factory creates
a text widget that has the CSS class set to ``disabled``.
