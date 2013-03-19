#coding: utf-8
from zope.schema import *
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
            m = u'%s has no attr %s' % (inputData.getId(), field)
            log.info(m)
            default = schema.get(field).default or ''
            t = TYPE_MAP.get(type(schema.get(field)), 'ustring')
            inputData.manage_addProperty(field, default, t)
    alsoProvides(inputData, schema)
