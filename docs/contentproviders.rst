:mod:`gs.content.form.base` Content Providers
=============================================

Two content providers are used for standard parts of forms in
GroupServer. One displays the `status message`_ at the top of the
page, while the other displays the widgets_.

Status message
--------------

The ``groupserver.FormStatusMessage`` content provider displays
the status of a form (the ``status`` and ``errors`` properties of
the form-view class) after it submits. It provides a standard
markup for the form, and normally sits in the ``messages`` slot.

.. code-block:: xml

    <tal:block 
      metal:fill-slot="messages"
      content="structure provider:groupserver.FormStatusMessage"
      define="errors view/errors; 
              status view/status;
              widgets view/widgets">&#160;</tal:block>

Two optional Boolean arguments — ``showPageErrors`` and
``showWidgetErrors`` — can be passed to the content provider to
control whether page and widget errors are displayed by the
content provider

.. code-block:: xml

    <tal:block 
      content="structure provider:groupserver.FormStatusMessage"
      define="errors view/errors; 
              status view/status;
              widgets view/widgets;
              showPageErrors python:True; 
              showWidgetErrors python:False"
      metal:fill-slot="messages">&#160;</tal:block>

``showPageErrors`` defaults to ``False`` while
``showWidgetErrors`` defaults to ``True``.

Widgets
-------

The ``groupserver.FormWidgets`` content provider displays the
widgets themselves. The ``widgets`` parameter is used to provide
a :type:`list` of widgets to the content provider.

.. code-block:: xml

    <tal:block define="widgets view/widgets">
      <tal:block replace="structure provider:groupserver.FormWidgets"/>
    </tal:block>

By default each widget is placed in a ``<div>`` that is marked as
required, or not.
