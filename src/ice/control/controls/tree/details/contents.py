### -*- coding: utf-8 -*- ####################################################
#
#  Copyright (C) 2010 Ilshad R. Khabibullin <astoon.net at gmail.com>
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

from zope.app.pagetemplate import ViewPageTemplateFile
from z3c.contents.browser import Contents as ContentsBase

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
        self.supportsCut = False # this is hack
