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

import os
from zope.interface import implements
from zope.component import getUtilitiesFor
from interfaces import ISession, IPlugin
from interpreter import Interpreter

class Session:
    implements(ISession)

    input_buffer = ''
    history = []
    h_max = 50

    def __init__(self, context):
        self.interpreter = Interpreter(
            {"__name__": "__console__",
             "__doc__": None,
             "context": context})

#        code = file(os.path.join(os.path.dirname(__file__), "bootstrap.py")).read()
#        self.run(code)

    def run(self, source):
        self.history.append(source)
        if len(self.history) > self.h_max:
            self.history = self.history[1:]
        self.input_buffer += source
        result = self.interpreter.runsource(self.input_buffer)
        if result: # code is incomplete
            self.input_buffer += '\n'
        else:
            self.input_buffer = ''
        return result, self.interpreter.get_output()

    def commit(self):
        return self.run("transaction.commit()")

    def get_plugins(self):
        return dict((k,v) for k,v in getUtilitiesFor(IPlugin))

    def apply_plugin(self, name, **kwargs):
        pass

    def get_history(self):
        return self.history
