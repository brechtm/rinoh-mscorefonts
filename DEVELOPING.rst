
rinoh-mscorefontinstaller
-------------------------

Build and publish source and wheel distributions::

    poetry install
    poetry build
    poetry publish


Font packages
-------------

Given the EULA restrictions, it is important that we **do not distribute wheel
distributions** since these include the TTF files directly.

The ``build_distributions.py`` builds source distributions for each of the
fonts. After this, use Twine to publish the packages on PyPI::


    poetry install
    poetry run python build_distributions.py
    twine upload dist/rinoh-typeface-*.tar.gz
