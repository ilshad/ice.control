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
    credentials: id and password, bind session to id, calculate SSHA
    encoding for password, store it for id, send id and password to
    you.

    When you try to get your session, I ask you for the id and
    password. Thus I am wrapper around of REPL sessions and I provide
    my own security level on frontier of getting the REPL sessions.
    """

    def set_session(context):
        """Create new session with given context, bind it to new
        credentials and return credentials, tuple id and password.
        """

    def get_session(id, password):
        """Get session. If the session is not exist for given id or
        password is wrong - return None. Else return ISession object.
        """
    
    def del_session(id, password):
        """Delete session.
        """

class ISession(zope.interface.Interface):
    """Advanced read-eval-print loop for BlueBream.
    Environment: context.
    """

    def run(source):
        """Run code.
        Return tuple: boolean and output. Boolean is True if the
        source argument contains incomplete python input, and
        False in other cases.
        """

    def get_history():
        """Get console input history in list.
        """
