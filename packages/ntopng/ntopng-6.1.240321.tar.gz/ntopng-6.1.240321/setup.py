from setuptools import setup

setup(
    name='ntopng',
    version='6.1.240321',
    description='ntopng Python package',
    url='https://github.com/ntop/ntopng',
    author='ntop',
    author_email='packager@ntop.org',
    license='GPL',
    packages=['ntopng'],
    install_requires=['requests', 'simplejson', 'numpy', 'pandas', 'kaleido', 'fpdf', 'plotly', 'redmail'],
 )
