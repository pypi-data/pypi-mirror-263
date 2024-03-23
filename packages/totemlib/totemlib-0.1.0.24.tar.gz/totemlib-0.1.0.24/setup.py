from setuptools import setup, find_packages


setup(
    name='totemlib',
    version='0.1.0.24',
    packages=find_packages(),
    install_requires=[
        # lista de dependencias
        'jproperties==2.1.1',
        'certifi==2023.7.22',
        'charset-normalizer==3.3.2',
        'docutils==0.20.1',
        'idna==3.4',
        'importlib-metadata==6.8.0',
        'jaraco.classes==3.3.0',
        'jproperties==2.1.1',
        'keyring==24.2.0',
        'markdown-it-py==3.0.0',
        'mdurl==0.1.2',
        'more-itertools==10.1.0',
        'nh3==0.2.14',
        'pkginfo==1.9.6',
        'Pygments==2.16.1',
        'readme-renderer==42.0',
        'requests==2.31.0',
        'requests-toolbelt==1.0.0',
        'rfc3986==2.0.0',
        'rich==13.6.0',
        'SQLAlchemy==2.0.23',
        'totemlib==0.1.0.22',
        'twine==4.0.2',
        'typing_extensions==4.8.0',
        'urllib3==2.0.7',
        'zipp==3.17.0'
    ],
    author='Totem Bear',
    author_email='info@totembear.com',
    description='Base library for general uses',
)
