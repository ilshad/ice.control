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
import zope.component
from zope.password.interfaces import IPasswordManager
from zope.cachedescriptors.property import Lazy
from interfaces import IDispatcher
from session import Session

class Dispatcher:
    zope.interface.implements(IDispatcher)
    
    def __init__(self):
        self._sessions = {}
        self._credentials = {}

    @Lazy
    def _pm(self):
        return zope.component.getUtility(IPasswordManager, name='SSHA')

    def _authenticate(self, id, pwd):
        try:
            return self._pm.checkPassword(self._credentials[id], pwd)
        except KeyError:
            return None

    def set_session(self, context):
        pwd = None
        id = None
        self._credentials[id] = self._pm.encodePassword(pwd)
        session = Session()
        session.setup()
        session.set_context(context)
        self._sessions[id] = Session()

    def get_session(self, id, password):
        return self._authenticate(id, password) and self._sessions[id] 
    
    def del_session(self, id, password):
        if self._authenticate(id, password):
            del self._sessions[id]
            del self._credentials[id]
