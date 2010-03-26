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

import random
import datetime
from zope.interface import implements
from zope.component import getUtility
from zope.password.interfaces import IPasswordManager
from interfaces import IDispatcher
from session import Session

class Dispatcher:
    implements(IDispatcher)
    
    _nextid = None
    _sessions = {}
    _credentials = {}
    _pwd_manager = 'SSHA'

    def _authenticate(self, id, pwd):
        try:
            pm = getUtility(IPasswordManager, name=self._pwd_manager)
            return pm.checkPassword(self._credentials[id], pwd)
        except KeyError:
            return False

    def _generate_id(self):
        while True:
            if self._nextid is None:
                self._nextid = random.randrange(0, 2**31)
            id = self._nextid
            self._nextid += 1
            if id not in self._credentials.keys():
                return id
            self._nextid = None

    def _generate_password(self):
        now = "".join(datetime.datetime.now().ctime().split())
        chars = []
        for i in range(30):
            chars.extend(random.sample(now ,1))
        return "".join(chars)

    def set_session(self, context):
        id = self._generate_id()
        pwd = self._generate_password()
        pm = getUtility(IPasswordManager, name=self._pwd_manager)
        self._credentials[id] = pm.encodePassword(pwd)
        self._sessions[id] = Session(context)
        return id, pwd

    def get_session(self, id, password):
        if self._authenticate(id, password):
            return self._sessions[id] 
        return None

    def del_session(self, id, password):
        if self._authenticate(id, password):
            del self._sessions[id]
            del self._credentials[id]
