### -*- coding: utf-8 -*- ####################################################
#
#  Copyright (C) 2010 Ilshad R. Khabibullin <astoon.net at gmail.com>
#
#  This library is free software: you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation, either version 3 of the License.
#
#  This library is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
#  or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
#  for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from zope.component import adapts, queryMultiAdapter
from zope.container.interfaces import IReadContainer
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.component.interfaces import ISite
from interfaces import IXML
from xmlbase import XMLBase
from lexeme import *

class XMLReadContainer(XMLBase):
    adapts(IReadContainer, IBrowserRequest)

    def size(self):
        return SIZE % len(self.context)

    def is_container(self):
        return IS_CONTAINER

    def length(self):
        return LENGTH % len(self.context)

class XMLSite(XMLReadContainer):
    adapts(ISite, IBrowserRequest)

    def children(self):
        # add ++etc++site
        sm = self.context.getSiteManager()
        spec = queryMultiAdapter((sm, self.request), IXML)
        lexemes = CHILD % spec.xml_lexemes()
        children = super(XMLSite, self).children()
        return lexemes + u'\n' + children
