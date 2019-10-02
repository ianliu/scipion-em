"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Load requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='scipion-em',  # Required
    version='1.0.0',  # Required
    description='This modules contains classes related with EM',  # Required
    long_description=long_description,  # Optional
    url='https://github.com/scipion-em/scipion-em',  # Optional
    author='J.M. De la Rosa Trevin, '
           'Roberto Marabini, '
           'Grigory Sharov, '
           'Josue Gomez Blanco, '
           'Pablo Conesa, '
           'Yunior Fonseca Reyna',  # Optional

    # This should be a valid email address corresponding to the author listed
    # above.
    author_email='delarosatrevin@scilifelab.se, '
                 'roberto@cnb.csic.es, '
                 'gsharov@mrc-lmb.cam.ac.uk, '
                 'josue.gomez-blanco@mcgill.ca, '
                 'pconesa@cnb.csic.es, '
                 'fonsecareyna@cnb.csic.es',  # Optional

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 2 - Pre-Alpha',
        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        # Pick your license as you wish
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering'
    ],
    keywords='scipion cryoem imageprocessing scipion-2.0',  # Optional
    packages=find_packages(),
    install_requires=[requirements],
    # package_data={  # Optional
    # #    '': [''],
    # }
)
