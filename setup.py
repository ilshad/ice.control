from setuptools import setup, find_packages

setup(name='ice.control',
      version='0.1.0',
      author='Ilshad Khabibullin',
      author_email='astoon.net at gmail.com',
      url='',
      description='',
      long_description='',
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

                        'z3c.testsetup',
                        'z3c.layer.pagelet',
                        'z3c.template',
                        'z3c.formui'],
      include_package_data=True,
      zip_safe=False)
