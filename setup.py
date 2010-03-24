import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(name='ice.control',
      version='0.1.0',
      author='Ilshad R. Khabibullin',
      author_email='astoon.net at gmail.com',
      url='http://astoon.zwiki.org/ice.control',
      description='System Administration and Site Management for BlueBream',
      long_description = (read('src/ice/control/doc/README')) +\
          '\n\n' + read('src/ice/control/doc/CHANGES'),
      license='GPL v.3',
      classifiers=[],
      packages=find_packages('src'),
      namespace_packages=['ice',],
      package_dir={'':'src'},
      install_requires=['setuptools',

                        'zope.testbrowser',
                        'zope.viewlet',

                        'zope.app.testing',
                        'zope.app.zcmlfiles',
                        'zope.app.apidoc',

                        'zc.resourcelibrary',

                        'z3c.testsetup',
                        'z3c.configurator',
                        'z3c.layer.pagelet',
                        'z3c.template',
                        'z3c.formui',
                        'z3c.zrtresource',
                        'z3c.contents'],
      include_package_data=True,
      zip_safe=False)
