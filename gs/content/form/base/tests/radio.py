# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2016 OnlineGroups.net and Contributors.
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
from __future__ import absolute_import, unicode_literals, print_function
from mock import (MagicMock, )
from unittest import TestCase
from gs.content.form.base.radio import NotBrokenRadioWidget


class TestNotBrokenRadioWidget(TestCase):
    'Test the ``NotBrokenRadioWidget`` class'

    def test_renderItem(self):
        field = MagicMock()
        field.__name__ = 'ethel'
        n = NotBrokenRadioWidget(field, MagicMock(), MagicMock())
        r = n.renderItem(0, 'Putting the boot in', 'boot', 'violence', 'frog')

        self.assertIn('<div', r)
        self.assertIn('<label', r)
        self.assertIn('>Putting the boot in</label>', r)
        self.assertIn('<input', r)
        self.assertIn('radioItem', r)
        self.assertIn('radioLabel', r)
        self.assertIn('radioType', r)
        self.assertIn('for="violence.0"', r)
        self.assertIn('id="violence.0"', r)
        self.assertIn('value="boot"', r)
        self.assertIn('name="violence"', r)
        self.assertIn('class="frog radioType"', r)

    def test_renderSelectedItem(self):
        field = MagicMock()
        field.__name__ = 'ethel'
        n = NotBrokenRadioWidget(field, MagicMock(), MagicMock())
        r = n.renderSelectedItem(0, 'Putting the boot in', 'boot', 'violence', 'frog')
        self.assertIn('checked="checked"', r)
