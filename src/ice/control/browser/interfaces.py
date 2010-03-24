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

from zope.interface import Interface
from zope.schema import TextLine, Int
from z3c.pagelet.interfaces import IPagelet

class IControl(Interface):
    """Location for system control"""

class IControlPagelet(IPagelet):
    """I am response for control views.
    Your pagelets should provide me."""

    title = TextLine(
        title=u'Title',
        default=u'',
        required=False)

    weight = Int(
        title=u'Weight',
        default=99,
        required=False)
