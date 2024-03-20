from setuptools import setup, find_packages


VERSION = '0.0.1' 
DESCRIPTION = 'Re-Usable Utils'
LONG_DESCRIPTION = 'Re-Usable Utils to Be Used on Our Django Projects'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name='rahavard',
        version=VERSION,
        author="Davoud Arsalani",
        author_email="d_arsalani@yahoo.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
                             # needs to be installed along with your package.

        keywords=['python',],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
