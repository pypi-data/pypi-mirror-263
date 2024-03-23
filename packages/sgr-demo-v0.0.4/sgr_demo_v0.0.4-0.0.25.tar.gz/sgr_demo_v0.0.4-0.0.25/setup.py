from setuptools import setup

VERSION = '0.0.25'
DESCRIPTION = 'SGr demo'

# Setting up
setup(
    name="sgr_demo_v0.0.4",
    version=VERSION,
    author="zupeuc(CLEMAP)",
    author_email="<daniel@clemap.ch>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=['sgr_library', 'sgr_library.data_classes', 'sgr_library.data_classes.generic',
              'sgr_library.data_classes.product', 'sgr_library.data_classes.communicator',
              'sgr_library.data_classes.functional_profile', 'sgr_library.api', 'sgr_library.validators',
              'sgr_library.converters'],
    install_requires=[
    'Jinja2>=3.0.0,<4.0.0',
    'jmespath>=1.0.0,<2.0.0',
    'numpy>=1.20.3', 
    'pymodbus>=3.0.0,<4.0.0',
    'setuptools>=68.0.0,<69.0.0',
    'xsdata>=22.0.0,<23.0.0',
    'aiohttp>=3.0.0,<4.0.0',
    'certifi',  
    'cachetools>=5.0.0,<6.0.0',
    ],
    keywords=['python', 'SGr'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)