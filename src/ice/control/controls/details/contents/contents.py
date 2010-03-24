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

from zope.traversing import api
from zope.app.pagetemplate import ViewPageTemplateFile
from z3c.contents.browser import Contents as ContentsBase
from z3c.contents.column import RenameColumn as RenameColumnBase

class Contents(ContentsBase):

    render = ViewPageTemplateFile('contents.pt')

    allowCopy = False
    allowPaste = False

    batchSize = 10
    startBatchingAt = 10

    def __call__(self):
        self.update()
        return self.render()

    def setupCopyPasteMove(self):
        super(Contents, self).setupCopyPasteMove()
        self.supportsCut = False # hack

class RenameColumn(RenameColumnBase):

    def renderLink(self, item):
        return api.getName(item)
