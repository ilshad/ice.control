##############################################################################
#
# Copyright (c) 2002 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
#  Project homepage: <http://launchpad.net/ice.control>
#
##############################################################################

from datetime import datetime
from zope.event import notify
from zope.dublincore.interfaces import IZopeDublinCore
from zope.lifecycleevent import ObjectModifiedEvent, Attributes

class EditDublinCore:

    def edit(self):
        try:
            dc = IZopeDublinCore(self.context)
        except TypeError:
            return None

        request = self.request
        formatter = self.request.locale.dates.getFormatter('dateTime', 'medium')
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
