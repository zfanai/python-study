#!/usr/bin/python
 
from distutils.core import setup, Extension
 
__version__ = "0.2"
 
macros = [('MODULE_VERSION', '"%s"' % __version__)]
 
setup(name         = "wrap2",
      version      = __version__,
      author       = "fk",
      author_email = "gf0842wf@gmail.com",
      url          = "",
      download_url = "",
      #description  = "XOR encrypt/decrypt for Python",
      description  = "C ext for Python",
      long_description = open('README').read(),
      license      = "LGPL",
      platforms    = ["Platform Independent"],
      classifiers  = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"
      ],
      ext_modules  = [
        Extension(name='wrap2', sources=['wrap.cpp'], define_macros=macros)
      ]
)