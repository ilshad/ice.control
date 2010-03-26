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
import pprint

class Interpreter(code.InteractiveInterpreter):

    def __init__(self, locals):
        self.output = []
        code.InteractiveInterpreter.__init__(self, locals)

    def write(self, data):
        data = pprint.pformat(data)
        if not data.endswith("\n"):
            data += "\n"
        self.output.append(data)

    def get_output(self):
        output = "".join(self.output)
        self.output = []
        return output
