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

import code, sys, StringIO

class Interpreter(code.InteractiveInterpreter):

    output = []

    def write(self, data):
        self.output.append(data.rstrip())

    def get_output(self):
        r = self.output[:]
        self.output = []
        return r

    def runcode(self, code):
        stdout = sys.stdout
        trap = StringIO.StringIO()
        sys.stdout = trap
        try:
            exec code in self.locals
            self.write(trap.getvalue())
        except SystemExit:
            sys.stdout = stdout
            trap.close()
            del trap
            raise
        except:
            self.showtraceback()
        sys.stdout = stdout
        trap.close()
        del trap
