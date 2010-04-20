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

from zope.location import Location
from zope.interface import implements
from interfaces import IControl

class Control(Location):
    implements(IControl)

    def get_content(self):
        # recursive search to avoid confusion if
        # [ ++control++/++control++ ] or something like
        def content(x):
            if IControl.providedBy(x):
                return content(x.__parent__)
            else:
                return x
        return content(self.__parent__)
