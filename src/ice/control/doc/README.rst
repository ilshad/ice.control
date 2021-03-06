.. contents:: Table of Contents
   :depth: 2

ice.control - System Administration and Site Management for BlueBream
*********************************************************************

ice.control is package for:

- BlueBream application developers: `developer kit` and `starter kit`.
- System administrators: `site management`.
- Site managers: just define views for these tasks.

FAQ: https://answers.launchpad.net/ice.control/+faqs

Package overview
----------------

This package does provide:

- treeview ZODB browser
- views for simple manipulate objects (remove, rename)
- introspector
- ajax based python shell with REPL to interact the application in
  selected ZODB context
- configurator plugin forms to manage ZODB, edit metadata, other
  ajax based views and ability to add new views
- other controls like generations and ZODB pack
- optional simple skin (as part of `starter kit`)
- optional module with all needed zcml registrations

Each facility is optional. Include needed components using zcml, or
include root configuration file to use entire functionality of the
package.

IMPORTANT NOTE: use Mozilla Firefox (Google Chrome also supported now,
but still possible bugs in UI. Please report.)

Getting started
---------------

(I assume you have empty BlueBream project from Paster template,
i.e. paster create -t bluebream.)

Add `ice.control` into dependencies of your project.

Add these directives into etc/site.zcml file, before of
`includeOvverides file="overrides.zcml"`::

  `include package="ice.control.zcml"`
  `include package="ice.control"`
  `include package="ice.control.repl"`

Run the server::

  $ bin/paster serve debug.ini

Open management skin: http://localhost:8080/++skin++control/
and log in admin account and learn UI.

Ajax based REPL
---------------

You might open, close, minimize number of 'Details' pseudo-windows
in the same time, and each plseudo-window will contain its own REPL
session. Session is defined for user and context. So, each context
has its own session.

Predefined variables and methods:

- `context` variable is current context in ZODB tree
- `getObject` method from zope.security.proxy
- `transaction` module import

Key bindings:

- `up` - up to history
- `down` - down to history
- `Tab` - tab indent
- `Ctrl+E` - go to line's end (in Firefox)


More options
------------

- If you like to install the package from Git repository, see HACKME,
  section ``Install from Git repository``.

- There are number of options to use ice.control. You have define this
  including certain modules in zcml, instead of entire. I.e. instead of
  `include package="ice.control"` - include needed nested modules.


Permissions
-----------

This package does define two permissions:

- ice.control.View
- ice.control.REPL

Different views have different permissions like zope.ManageService,
zope.ManageApplication and etc. You need to know about this only if you
going to use controls not only by bootstrap user zope.Manager.
