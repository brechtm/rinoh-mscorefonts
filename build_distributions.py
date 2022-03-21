#!/bin/env python

import sys

from pathlib import Path
from subprocess import run


VERSION = '0.1.0'

FONTS = {
    'Andale Mono': ('2.00', 'https://en.wikipedia.org/wiki/Andal%C3%A9_Mono', 'andale32.exe',
                    '0524fe42951adc3a7eb870e32f0920313c71f170c859b5f770d82b4ee111e970'),
    'Arial': ('2.82', 'https://en.wikipedia.org/wiki/Arial', 'arial32.exe',
              '85297a4d146e9c87ac6f74822734bdee5f4b2a722d7eaa584b7f2cbf76f478f6'),
    'Arial Black': ('2.35', 'https://en.wikipedia.org/wiki/Arial_Black',
                    'arialb32.exe', 'a425f0ffb6a1a5ede5b979ed6177f4f4f4fdef6ae7c302a7b7720ef332fec0a8'),
    'Comic Sans MS': ('2.10', 'https://en.wikipedia.org/wiki/Comic_Sans_MS',
                      'comic32.exe', '9c6df3feefde26d4e41d4a4fe5db2a89f9123a772594d7f59afd062625cd204e'),
    'Courier New': ('2.82', 'https://en.wikipedia.org/wiki/Courier_New',
                    'courie32.exe', 'bb511d861655dde879ae552eb86b134d6fae67cb58502e6ff73ec5d9151f3384'),
    'Georgia': ('2.05', 'https://en.wikipedia.org/wiki/Georgia_(typeface)',
                'georgi32.exe', '2c2c7dcda6606ea5cf08918fb7cd3f3359e9e84338dc690013f20cd42e930301'),
    'Impact': ('2.35', 'https://en.wikipedia.org/wiki/Impact_(typeface)',
               'impact32.exe', '6061ef3b7401d9642f5dfdb5f2b376aa14663f6275e60a51207ad4facf2fccfb'),
    'Times New Roman': ('2.82', 'https://en.wikipedia.org/wiki/Times_New_Roman',
                        'times32.exe', 'db56595ec6ef5d3de5c24994f001f03b2a13e37cee27bc25c58f6f43e8f807ab'),
    'Trebuchet MS': ('1.22', 'https://en.wikipedia.org/wiki/Trebuchet_MS',
                     'trebuc32.exe', '5a690d9bb8510be1b8b4fe49f1f2319651fe51bbe54775ddddd8ef0bd07fdac9'),
    'Verdana': ('2.35', 'https://en.wikipedia.org/wiki/Verdana',
                'verdan32.exe', 'c1cb61255e363166794e47664e2f21af8e3a26cb6346eb8d2ae2fa85dd5aad96'),
    'Webdings': ('1.03', 'https://en.wikipedia.org/wiki/Webdings',
                 'webdin32.exe', '64595b5abc1080fba8610c5c34fab5863408e806aafe84653ca8575bed17d75a'),
}

PYPROJECT = """\
[build-system]
requires = [
    "setuptools>=36.6",
    "wheel",
    "rinoh-mscorefontinstaller>=0.1.0,<0.2.0"
]
"""

SETUP = """\
from rinoh_mscorefontinstaller import setup


setup(
    name='{name}',
    version='{version}',
    archive='{archive}',
    sha256sum='{sha256sum}',
    setup_file=__file__
)
"""

README = """\
==============={line}
rinoh-typeface-{identifier}
==============={line}

This package provides the `{name}`_ {version} typeface from Microsoft's `Core
fonts for the Web`_ for use with rinohtype_.

In order to comply with the EULA for these fonts, the font archive is
downloaded during installation of this package.


.. _{name}: {url}
.. _Core fonts for the Web: https://en.wikipedia.org/wiki/Core_fonts_for_the_Web
.. _rinohtype: https://github.com/brechtm/rinohtype#readme
"""

DIST = Path(__file__).parent / 'dist'
BUILD = Path(__file__).parent / 'build'


for name, (version, url, archive, sha256sum) in FONTS.items():
    identifier = name.lower().replace(' ', '')
    dir = BUILD / identifier
    dir.mkdir(parents=True, exist_ok=True)
    pyproject = dir / 'pyproject.toml'
    setup = dir / 'setup.py'
    readme = dir / 'README.rst'
    pyproject.write_text(PYPROJECT)
    setup.write_text(SETUP.format(name=name, version=VERSION, archive=archive,
                                  sha256sum=sha256sum), encoding='utf-8')
    readme.write_text(README.format(line="=" * len(identifier),
                                    identifier=identifier, name=name,
                                    version=version, url=url))
    run([sys.executable, 'setup.py', 'sdist', '--dist-dir', DIST], cwd=dir)
