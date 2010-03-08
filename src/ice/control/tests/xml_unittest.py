"""

:unittest:
"""

import unittest
import zope.component
from zope.interface.verify import verifyObject

class Test(unittest.TestCase):

    def test_lexeme(self):
        from ice.control.controls.tree import lexeme

        self.assertEqual(lexeme.NAME % u'foo',
                         u'<name>foo</name>')
        self.assertEqual(lexeme.URL % u'http://foo.com',
                         u'<url>http://foo.com</url>')
        self.assertEqual(lexeme.TITLE % u'Foo',
                         u'<title>Foo</title>')
        self.assertEqual(lexeme.ICON_URL % u'http://foo.com',
                         u'<icon_url>http://foo.com</icon_url>')
        self.assertEqual(lexeme.IS_CONTAINER,
                         u'<is_container>True</is_container>')
        self.assertEqual(lexeme.SIZE % 77,
                         u'<size>77</size>')
        self.assertEqual(lexeme.LENGTH % 77,
                         u'<length>77</length>')
        self.assertEqual(lexeme.CHILDREN % u'xxx',
                         u'<children>xxx</children>')
        self.assertEqual(lexeme.CHILD % u'xxx',
                         u'<child>xxx</child>')
        self.assertEqual(lexeme.XML_HEAD,
                         u'<?xml version="1.0" ?>')
        self.assertEqual(lexeme.XML_ROOT % u'xxx',
                         u'<document>xxx</document>')

    def test_verify(self):
        from ice.control.controls.tree.interfaces import IXML
        from ice.control.controls.tree.xmlbase import XMLBase

        zope.component.provideAdapter(XMLBase)

        from zope.site.folder import Folder
        from zope.publisher.browser import TestRequest

        f = Folder()
        r = TestRequest()
        xml = zope.component.getMultiAdapter((f, r), IXML)

        self.assertEqual(verifyObject(IXML, xml), True)
