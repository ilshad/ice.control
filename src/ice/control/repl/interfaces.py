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

import zope.interface

class IDispatcher(zope.interface.Interface):
    """Store and dispatch sessions.

    For new session, I create and store ISession object, create new
    credential: id and password, bind session to id, calculate SSHA
    encoding for password, store it for id, send id and password to
    you.

    When you try to get your session, I ask you for the id and
    password. Thus I am wrapper around of REPL sessions and I provide
    my own security level on frontier of getting the REPL sessions.
    """

    def set_session(context):
        """Create new session with given context, bind it to new
        credential and return credential, tuple id and password.
        """

    def get_session(id, password):
        """Get session. If the session is not exist for given id or
        password is wrong - return None. Else return ISession object.
        """
    
    def del_session(id, password):
        """"Delete session.
        """

class ISession(zope.interface.Interface):
    """Advanced read-eval-print loop for BlueBream.
    """

    def setup():
        """Setup environment.
        """

    def authenticate(id, password):
        """Authenticate within this session, for zope security system.
        """

    def run(code):
        """Run code.
        """

    def commit():
        """Commit transaction.
        """

    def set_context(context):
        """Set current context.
        """

    def get_context():
        """Get current context.
        """

    def get_plugins():
        """Get plugins.
        """

class IPlugin(zope.interface.Interface):
    """REPL plug-in.
    """