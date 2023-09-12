from setuptools import setup, find_packages

# Get the directory where setup.py is located
current_directory = os.path.abspath(os.path.dirname(__file__))

# Use that directory to construct the absolute path to README.rst
with open(os.path.join(current_directory, 'README.rst'), 'r') as f:
    long_description = f.read()


setup(
    name = 'troppo',
    version = '0.0.5',
    package_dir = {'':'src'},
    packages = find_packages('src'),
    install_requires = ["cobamp"],

    author = 'Jorge Ferreira & Vítor Vieira',
    author_email = 'jorge.ferreira@ceb.uminho.pt & vvieira@ceb.uminho.pt',
    description = 'TROPPO - Tissue-specific RecOnstruction and Phenotype Prediction using Omics data',
    license = 'GNU General Public License v3.0',
    keywords = 'pathway analysis metabolic model',
    url = 'https://github.com/BioSystemsUM/troppo',
    long_description = long_description,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
