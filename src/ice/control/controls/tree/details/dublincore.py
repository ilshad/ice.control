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
##############################################################################

from datetime import datetime
from zope.event import notify
from zope.dublincore.interfaces import IZopeDublinCore
from zope.lifecycleevent import ObjectModifiedEvent, Attributes

class EditDublinCore:

    def edit(self):
        request = self.request
        formatter = self.request.locale.dates.getFormatter('dateTime', 'medium')
        dc = IZopeDublinCore(self.context)
        message=''

        if 'dctitle' in request:
            dc.title = unicode(request['dctitle'])
            dc.description = unicode(request['dcdescription'])
            description = Attributes(IZopeDublinCore, 'title', 'description')
            notify(ObjectModifiedEvent(self.context, description))
            message = "Changed data %s" % formatter.format(datetime.utcnow())

        return {'message': message,
                'dctitle': dc.title,
                'dcdescription': dc.description,
                'modified': (dc.modified or dc.created) and \
                    formatter.format(dc.modified or dc.created) or '',
                'created': dc.created and formatter.format(dc.created) or '',
                'creators': dc.creators}
