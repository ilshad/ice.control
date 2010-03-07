### -*- coding: utf-8 -*- ####################################################
#
#  Copyright (C) 2010 Ilshad Khabibullin <astoon.net at gmail.com>
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

from zope.interface import implements
from zope.component import getAdapters, getMultiAdapter
from zope.contentprovider.interfaces import IContentProvider
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
        self.pagelets = [v for n,v in pagelets]
        self.pagelets.sort(key=lambda x:x.weight)

    def render(self):
        template = getMultiAdapter((self, self.request), IContentTemplate)
        return template(self)
