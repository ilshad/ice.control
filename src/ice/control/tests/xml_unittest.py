"""

:unittest:
"""

import unittest
import zope.component
from zope.interface.verify import verifyObject

class Test(unittest.TestCase):

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
