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

import zope.interface

ICONS = 'control_icon'

XMLDOC = u'<?xml version="1.0" ?>\n<document>\n%s\n</document>'

XMLNODE = u'''<node name="%s" path="%s" title="%s" icon_url="%s"
                    size="%s" length="%s" is_container="%s" />'''

ACCESS_DENIED = u'ACCESS DENIED'

class IXML(zope.interface.Interface):
    """XML specification for content object"""

    def name():
        """Return unicode string: location name or empty string"""

    def path():
        """Return unicode string: URL or empty string"""

    def title():
        """Return unicode string: title or empty string"""

    def icon_url():
        """Return unicode string: icon URL or empty string"""

    def is_container():
        """Return boolean: container or none"""

    def size():
        """Return unicode string: size for dispaly or empty string"""

    def length():
        """Return unicode string with number of children to display in
        tree or empty string"""

    def sort_key():
        """Return any type, key for sorting (within parent container)"""

    def to_xml():
        """Return xml node:
          <node name=".." path=".." title=".."
                icon_url=".." is_container="..true/..false" 
                size=".." length=".." />"""

    def node_xmldoc():
        """Return valid XML document with one node for navigation tree:
        <?xml version="1.0" ?>
        <document>
          <node ... />
        </document>"""

    def children_xmldoc():
        """Return valid XML document with number of nodes to create
        children: 
        <?xml version="1.0" ?>
        <document>
          <node ... />
          <node ... />
          <node ... />
        </document>
        Sorted by size for sorting."""
