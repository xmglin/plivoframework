from setuptools import find_packages
import sys

requires = ['gevent', 'flask==0.10.1', 'ujson==1.33', 'redis==2.8.0']

if sys.prefix == '/usr':
    etc_prefix = '/etc'
else:
    etc_prefix = sys.prefix + '/etc'


author = "Plivo Inc"
author_email = "hello@plivo.com"
maintainer = "Plivo Inc"
maintainer_email = "hello@plivo.com"
license = "MPL 1.1"

setup_args = {
      'name':'plivo',
      'version':'0.1.0',
      'description':'Plivo Framework - Rapid Telephony Application Prototyping Framework',
      'url':'http://github.com/plivo/plivoframework',
      'author':author,
      'author_email':author_email,
      'maintainer':maintainer,
      'maintainer_email':maintainer_email,
      'platforms':['linux'],
      'long_description':'Framework to prototype telephony applications rapidly in any language',
      'package_dir':{'': 'src'},
      'packages':find_packages('src'),
      'include_package_data':True,
      'scripts':['src/bin/plivo-rest',
                 'src/bin/plivo-outbound',
                 'src/bin/plivo-cache',
                 'src/bin/plivo-postinstall',
                 'src/bin/wavdump.py',
                 'src/bin/wavstream.sh',
                 'src/bin/cacheserver',
                 'src/bin/plivo'],
      'data_files':[(etc_prefix+'/plivo/', ['src/config/default.conf', 'src/config/cache.conf', 
                    'src/initscripts/centos/plivo', 'src/initscripts/centos/plivocache']),
                   ],
      'keywords':"telecom voip telephony freeswitch ivr rest",
      'license':license,
      'zip_safe':False,
      'classifiers':[
        "Programming Language :: Python",
        "Operating System :: POSIX",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications",
        "Topic :: Multimedia",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Intended Audience :: Telecommunications Industry",
        "License :: OSI Approved :: Mozilla Public License 1.1 (MPL 1.1)",
        "Development Status :: 1 - Beta"]
}


try:
    from setuptools import setup
    setup_args['install_requires'] = requires
except ImportError:
    from distutils.core import setup
    setup_args['requires'] = requires

# setup
setup(**setup_args)
