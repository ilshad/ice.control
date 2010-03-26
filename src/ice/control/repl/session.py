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

import code
from zope.interface import implements
from zope.component import getUtilitiesFor
from interfaces import ISession, IPlugin

class Session:
    implements(ISession)

    _context = None

    def __init__(self):
        self._shell = code.InteractiveConsole()

    def setup(self):
        self._shell.runcode("import transaction")

    def run(self, code):
        return self._shell.runcode(code)

    def commit(self):
        self._shell.runcode("transaction.commit()")

    def set_context(self, context):
        self._context = context

    def get_context(self):
        return self._context

    def get_plugins(self):
        return dict((k,v) for k,v in getUtilitiesFor(
                IPlugin, self.get_context()))

    def apply_plugin(self, name, **kwargs):
        plugin = self.get_plugins().get(name)
        self._shell.runcode(plugin(**kwargs))
