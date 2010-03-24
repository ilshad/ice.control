### -*- coding: utf-8 -*- ####################################################
#
#  Copyright (C) 2010 Ilshad R. Khabibullin <astoon.net at gmail.com>
#
#  This library is free software: you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation, either version 3 of the License.
#
#  This software is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
#  or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
#  for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this software.  If not, see <http://www.gnu.org/licenses/>.
#
#  Project homepage: <http://launchpad.net/ice.control>
#
##############################################################################

from zope.component import adapts, queryMultiAdapter
from zope.container.interfaces import IReadContainer
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.component.interfaces import ISite
from interfaces import IXML, XMLDOC
from xmlbase import XMLBase

class XMLReadContainer(XMLBase):
    adapts(IReadContainer, IBrowserRequest)

    def is_container(self):
        return True

    def size(self):
        return len(self.context)

    def length(self):
        return len(self.context)

class XMLSite(XMLReadContainer):
    adapts(ISite, IBrowserRequest)

    def children_xmldoc(self):
        try:
            rc = IReadContainer(self.context)
        except TypeError:
            return XMLDOC % u''
        specs = [queryMultiAdapter((value, self.request), IXML)
                for value in rc.values()]
        specs = filter(lambda x:x, specs)
        specs.sort(key = lambda x: x.sort_key())

        nodes = [x.to_xml() for x in specs]

        # add ++etc++site
        sm = self.context.getSiteManager()
        sm_spec = queryMultiAdapter((sm, self.request), IXML)
        nodes.append(sm_spec.to_xml())

        return XMLDOC % u'\n'.join(nodes)
