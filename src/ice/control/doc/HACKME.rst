ice.control development
***********************

Fork author's branch on GitHub repository. Install it (see below) but
use your own repository's private URL.


Install from Git repository
---------------------------

Download sources from GitHub repository using `mr.developer` buildout
extension. You have much more control on the source code using this way.

It requires number of steps first time, but simple to maintain in
futher. First, add follow lines into buildout.cfg, section [buildout]::

  [buildout]
  ...

  extensions = mr.developer
  sources-dir = dev
  sources = sources

then run buildout to create `develop` script::

  $ bin/buildout

then add section [sources] into buildout.cfg::

  [sources]
  ice.control = git git://github.com/astoon/ice.control.git

and run the script to download the branch::

  $ bin/develop checkout ice.*

You'll see now the package branch in /dev directory. Allow to run tests
from ice.control package. For this, edit buildout.cfg again::

  [test]
  ...
  eggs = sample
         ice.control

and add dependency for your project in setup.py::

   install_requires=[...
                    'ice.control'
                    ],

Finally, run buildout::

  $ bin/buildout


Issues, Blueprints
------------------

* https://bugs.launchpad.net/ice.control
* https://blueprints.launchpad.net/ice.control
* https://answers.launchpad.net/ice.control
* http://github.com/astoon/ice.control/issues
* For free discussions - Goole Wave ID: googlewave.com!w+r7PkMjhxA
  (https://wave.google.com/wave/?#restored:wave:googlewave.com!w%252Br7PkMjhxA)

Collaboration
-------------

1. Open page of mainstream repository (http://github.com/astoon/ice.control) (or other, not mainstream), and click button "Fork".

2. Use mr.developer extension (see above) to clone repository within your project. But use your own URL in [sources] section of buildout.cfg

3. Add mainstream repository into into the list of remotes::

     $ cd dev/ice.control
     $ git remote add main git://github.com/astoon/ice.control.git
     $ git fetch main

4. To synchronize the code from mainstream, merge::

     $ git fetch main
     $ git merge main/master

5. Publish your changes::

     $ git push origin master

6. Press button "Pull Request" to make merge proposal into the next release.
