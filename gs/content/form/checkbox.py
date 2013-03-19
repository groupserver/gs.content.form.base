# -*- coding: utf-8 -*-
from zope.app.form.browser import MultiCheckBoxWidget
from zope.app.form.browser.widget import renderElement


class NotBrokenMultiCheckBoxWidget(MultiCheckBoxWidget):
    _joinButtonToMessageTemplate = \
      u'<span class="checkboxGroup" id="checkboxgroup-%s">%s&nbsp;%s</span>'

    def renderItem(self, index, text, value, name, cssClass):
        widgetId = u'%s.%s' % (name, index)
        elem = renderElement('input',
                             type="checkbox",
                             cssClass=cssClass,
                             name=name,
                             id=widgetId,
                             value=value)
        label = u'<label class="checkboxLabel" for="%s">%s</label>' % \
          (widgetId, text)
        gId = widgetId.replace('.', '-')

        return self._joinButtonToMessageTemplate % (gId, elem, label)

    def renderSelectedItem(self, index, text, value, name, cssClass):
        widgetId = u'%s.%s' % (name, index)
        elem = renderElement('input',
                             type="checkbox",
                             cssClass=cssClass,
                             name=name,
                             id=widgetId,
                             value=value,
                             checked="checked")
        label = u'<label class="checkboxLabel" for="%s">%s</label>' % \
          (widgetId, text)
        gId = widgetId.replace(u'.', u'-')
        return self._joinButtonToMessageTemplate % (gId, elem, label)


def multi_check_box_widget(field, request):
    return NotBrokenMultiCheckBoxWidget(field,
                                        field.value_type.vocabulary,
                                        request)
