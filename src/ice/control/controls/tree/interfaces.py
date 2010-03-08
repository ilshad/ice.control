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

import zope.interface

ICON_ADAPTER_NAME = 'control_icon'

class IXML(zope.interface.Interface):
    """XML specification for content object"""

    def name():
        """Location name: <name>...</name>. Or None"""

    def url():
        """URL: <url>...</url> or empty string"""

    def title():
        """Title: <title>...</title> or empty string"""

    def icon_url():
        """Content Type Icon URL: <icon_url>...</icon_url>
        or empty string."""

    def size():
        """Size for dispaly: <size>...</size> or empty string"""

    def is_container():
        """Container or none: <is_container>True</is_container>
        or empty string."""

    def length():
        """Number of children if it is container:
        <length>...</length> or empty string."""

    def sort_key():
        """Return key for sorting (within parent container)
        or empty string."""

    def children():
        """XML describes my children: <children>...</children>
        or empty string. Use <child>...</child> xml tag to describe
        each child. Use xml_lexemes to populate this tag. Sorted by
        size for sorting."""

    def xml_lexemes():
        """All xml lexemes concatenated into string,
        except of children."""

    def xml_document():
        """Valid XML document: entire XML definition
        in valid xml document."""
