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
from zope.interface import implements, directlyProvides
from zope.traversing.interfaces import IContainmentRoot
from zope.security.checker import ProxyFactory, NamesChecker
from interfaces import IControl

controlRoot = Location()
directlyProvides(controlRoot, IContainmentRoot)
controlRoot = ProxyFactory(controlRoot, NamesChecker("__class__"))

class Control(Location): implements(IControl)

control = Control()
control.__parent__ = controlRoot
control.__name__ = u'++etc++control'
