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

from zope.dublincore.interfaces import IZopeDublinCore
from zope.app.component.browser.registration import IRegistrationDisplay
from zope.component import getSiteManager, getMultiAdapter

def _registrations(context, comp):
    sm = getSiteManager(context)
    for r in sm.registeredUtilities():
        if r.component == comp or comp is None:
            yield r
    for r in sm.registeredAdapters():
        if r.factory == comp or comp is None:
            yield r
    for r in sm.registeredSubscriptionAdapters():
        if r.factory == comp or comp is None:
            yield r
    for r in sm.registeredHandlers():
        if r.factory == comp or comp is None:
            yield r

class DetailsInfoBase:

    def getTitle(self):
        dc = IZopeDublinCore(self.context, None)
        return dc and dc.title

    def getRegistrations(self):
        return [getMultiAdapter((r, self.request), IRegistrationDisplay)
                for r in sorted(_registrations(self.context, self.context))]
