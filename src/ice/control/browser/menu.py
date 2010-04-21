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

from zope.security import canAccess
from zope.interface import implements
from zope.component import getAdapters, getMultiAdapter
from zope.contentprovider.interfaces import IContentProvider
from zope.authentication.interfaces import IUnauthenticatedPrincipal
from z3c.template.interfaces import IContentTemplate
from interfaces import IControlPagelet

class Menu:
    implements(IContentProvider)
    
    def __init__(self, context, request, view):
        self.context = context
        self.request = request
        self.__parent__ = view

    def update(self):
        pagelets = getAdapters((self.context, self.request), IControlPagelet)
        self.pagelets = [v for k,v in pagelets if canAccess(v, '__call__')]
        self.pagelets.sort(key = lambda x: x.weight)

    def render(self):
        template = getMultiAdapter((self, self.request), IContentTemplate)
        return template(self)

    def noauth(self):
        return IUnauthenticatedPrincipal.providedBy(self.request.principal)
