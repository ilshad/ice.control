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

from rfc822 import formatdate, time
from zope.component import getMultiAdapter
from interfaces import IXML

def setHeaders(response):
    response.setHeader('Content-Type', 'text/xml')
    response.setHeader('Pragma', 'no-cache')
    response.setHeader('Cache-Control', 'no-cache')
    response.setHeader('Expires', formatdate(time.time() - 7 * 86400))

class Ajax:

    def getControlTreeNode(self):
        setHeaders(self.request.response)
        node = getMultiAdapter((self.context, self.request), IXML)
        return node.node_xmldoc()

    def getControlTreeChildren(self):
        setHeaders(self.request.response)
        node = getMultiAdapter((self.context, self.request), IXML)
        return node.children_xmldoc()
