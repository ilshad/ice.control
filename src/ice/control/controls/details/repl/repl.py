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

from zope.component import getUtility
from zope.session.interfaces import ISession
from zope.traversing.browser.absoluteurl import absoluteURL
from ice.control.repl.interfaces import IDispatcher

PREFIX = 'ice.control.repl.'

def prepare_output(source):
    source = source.replace('<', '&lt;')
    source = source.replace('>', '&gt;')
    return source

class REPL:

    def session_data(self):
        session = ISession(self.request)
        absolute_url = absoluteURL(self.context, self.request)
        return session[PREFIX + absolute_url]

    def get_repl(self):
        dispatcher = getUtility(IDispatcher)
        data = self.session_data()
        credentials = data.get('id'), data.get('password')
        session = dispatcher.get_session(*credentials)
        if session:
            return session
        credentials = dispatcher.set_session(self.context)
        data['id'], data['password'] = credentials
        return dispatcher.get_session(*credentials)

    def clear(self):
        dispatcher = getUtility(IDispatcher)
        data = self.session_data()
        try:
            dispatcher.del_session(data['id'], data['password'])
        except KeyError:
            pass

    def interact(self):
        self.request.response.setHeader('Content-Type', 'text/xml')
        source = self.request.get('source')
        repl = self.get_repl()
        result, output = repl.run(source)

        output_xml = [u'<line><![CDATA[%s]]></line>\n' %
                      prepare_output(x) for x in output]

        response_xml = u'<?xml version="1.0" ?>\n'
        response_xml += u'<doc>\n'
        response_xml += u'<output>%s</output>\n' % "".join(output_xml)
        response_xml += u'<result>%s</result>\n' % int(result)
        response_xml += u'</doc>\n'
        return response_xml

    def get_history(self):
        self.request.response.setHeader('Content-Type', 'text/xml')
        response_xml = u'<?xml version="1.0" ?>\n'
        response_xml += u'<doc>\n'
        for x in self.get_repl().get_history():
            response_xml += u'<line>%s</line>\n' % x
        response_xml += u'</doc>\n'
        return response_xml
