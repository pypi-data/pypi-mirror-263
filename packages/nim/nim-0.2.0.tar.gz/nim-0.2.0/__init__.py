# coding: utf-8

from __future__ import print_function, absolute_import, division, unicode_literals

_package_data = dict(
    full_package_name="nim",
    version_info=(0, 2, 0),
    __version__="0.2.0",
    author="Anthon van der Neut",
    author_email="a.van.der.neut@ruamel.eu",
    description="python to nim interfacing",
    # keywords="",
    entry_points="nim=nim.__main__:main",
    # entry_points=None,
    license="Copyright Ruamel bvba 2007-2024",
    since=2017,
    # status="α|β|stable",  # the package status on PyPI
    # data_files="",
    # universal=True,
    install_requires=dict(
        any=["ruamel.appconfig", "ruamel.std.argparse"],
    ),
    python_requires='>=3',
)


version_info = _package_data['version_info']
__version__ = _package_data['__version__']
