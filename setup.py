# -*- coding: utf-8 -*-
"""Scientific Python libraries documentation"""

from distutils.core import setup
import os
import os.path as osp

def get_data_files(dirname):
    """Return data files in directory *dirname*"""
    flist = []
    for dirpath, _dirnames, filenames in os.walk(dirname):
        for fname in filenames:
            flist.append(osp.join(dirpath, fname))
    return flist

PROJECT_NAME = 'Scidoc'

setup(name=PROJECT_NAME, version='1.9.3',
      description='%s installs scientific Python libraries documentation' % PROJECT_NAME,
      long_description="""%s installs scientific Python libraries documentation (NumPy, SciPy, Matplotlib and others) in sys.prefix\Doc directory on Windows.
%s version is indexed to NumPy version.

%s is part of the WinPython distribution project.
""" % (PROJECT_NAME, PROJECT_NAME, PROJECT_NAME),
      data_files=[(r'Doc', get_data_files('doc'))],
      author = "Pierre Raybaut",
      author_email = 'pierre.raybaut@gmail.com',
      url = 'https://github.com/PierreRaybaut/Scidoc',
      classifiers=['Operating System :: Microsoft :: Windows'])
