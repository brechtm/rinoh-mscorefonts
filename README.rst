rinoh-mscorefontinstaller
=========================

.. image:: http://img.shields.io/pypi/v/rinoh-mscorefontinstaller.svg
   :target: https://pypi.python.org/pypi/rinoh-mscorefontinstaller
   :alt: PyPI

.. image:: https://img.shields.io/pypi/pyversions/rinoh-mscorefontinstaller.svg
   :target: https://pypi.python.org/pypi/rinoh-mscorefontinstaller
   :alt: Python version


This is a helper package to download and extract Microsoft's `Core fonts for the
Web`_. The fonts cannot be distributed as part of plain Python packages due the
restrictions imposed by the EULA_ for these fonts.

This package is set as a build/install-time requirement for the font packages,
so you should never need to install it yourself. Instead, you can install the
individual typefaces from PyPI:

- Andale Mono: `rinoh-typeface-andalemono <https://pypi.org/project/rinoh-typeface-andalemono>`_
- Arial: `rinoh-typeface-arial <https://pypi.org/project/rinoh-typeface-arial>`_
- Arial Black: `rinoh-typeface-arialblack <https://pypi.org/project/rinoh-typeface-arialblack>`_
- Comic Sans MS: `rinoh-typeface-comicsansms <https://pypi.org/project/rinoh-typeface-comicsansms>`_
- Courier New: `rinoh-typeface-couriernew <https://pypi.org/project/rinoh-typeface-couriernew>`_
- Georgia: `rinoh-typeface-georgia <https://pypi.org/project/rinoh-typeface-georgia>`_
- Impact: `rinoh-typeface-impact <https://pypi.org/project/rinoh-typeface-impact>`_
- Times New Roman: `rinoh-typeface-timesnewroman <https://pypi.org/project/rinoh-typeface-timesnewroman>`_
- Trebuchet MS: `rinoh-typeface-trebuchetms <https://pypi.org/project/rinoh-typeface-trebuchetms>`_
- Verdana: `rinoh-typeface-verdana <https://pypi.org/project/rinoh-typeface-verdana>`_
- Webdings: `rinoh-typeface-webdings <https://pypi.org/project/rinoh-typeface-webdings>`_

The `repository for this package`_ contains a script to create the distribution
packages for the fonts. See `DEVELOPING.rst`__ for more information.

.. __: ./DEVELOPING.rst


.. _Core fonts for the Web: https://en.wikipedia.org/wiki/Core_fonts_for_the_Web
.. _EULA: https://github.com/brechtm/corefonts/blob/master/LICENSE
.. _repository for this package: https://github.com/brechtm/rinoh-mscorefonts
