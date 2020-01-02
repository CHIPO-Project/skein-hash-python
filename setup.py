import setuptools
from distutils.core import setup, Extension

skein_hash_module = Extension('skein_hash',
                               sources = ['skeinmodule.c',
                                          'skein.c'],
                               include_dirs=['.', './shacommon'])

setup (name = 'coin_skein_hash',
       version = '1.1',
       package_data = {
        '': ['*.h']
        },
       license="MIT",
       author = 'nakkie',
       author_email = 'nakkie@linux.jpn.com',
       maintainer='nakkie',
       maintainer_email='nakkie@linux.jpn.com',
       description = 'Binding for CHIPO skein proof of work hashing.',
       ext_modules = [skein_hash_module],
       url = 'https://github.com/CHIPO-Project/skein-hash-python',
       download_url = 'https://github.com/CHIPO-Project/skein-hash-python/archive/v1.0.tar.gz'
       )
