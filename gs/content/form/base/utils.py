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
from zope.schema import (getFieldsInOrder, Text, TextLine, ASCII, ASCIILine,
                         URI, Bool, Float, Int, Datetime, Date)
from zope.interface import alsoProvides
import logging
log = logging.getLogger('gs.content.form.utils')


TYPE_MAP = {
    Text: 'text',
    TextLine: 'string',
    ASCII: 'text',
    ASCIILine: 'string',
    URI: 'string',
    Bool: 'boolean',
    Float: 'float',
    Int: 'int',
    Datetime: 'date',
    Date: 'date',
}


def enforce_schema(inputData, schema):
    """
    SIDE EFFECTS
      * "inputData" is stated to provide the "schema" interface
      * "inputData" will provide all the properties defined in "schema"
    """

    fields = [field[0] for field in getFieldsInOrder(schema)]
    for field in fields:
        if not hasattr(inputData, field):
            m = '%s has no attr %s' % (inputData.getId(), field)
            log.info(m)
            default = schema.get(field).default or ''
            t = TYPE_MAP.get(type(schema.get(field)), 'ustring')
            inputData.manage_addProperty(field, default, t)
    alsoProvides(inputData, schema)
