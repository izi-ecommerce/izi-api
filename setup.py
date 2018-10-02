from setuptools import setup, find_packages

__version__ = "2.0.0"


setup(
    # package name in pypi
    name='izi-api',
    # extract version from module.
    version=__version__,
    description="REST API module for izi-core",
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    keywords='',
    author='Daniel Do',
    author_email='dotiendiep@gmail.com',
    url='https://github.com/izi-ecommerce/izi-api',
    license='BSD',
    # include all packages in the egg, except the test package.
    packages=find_packages(
        exclude=['ez_setup', 'examples', '*tests', '*fixtures', 'sandbox']),
    # for avoiding conflict have one namespace for all apc related eggs.
    namespace_packages=[],
    # include non python files
    include_package_data=True,
    zip_safe=False,
    # specify dependencies
    install_requires=[
        'setuptools',
        'izi-core>=2.0.0',
        'djangorestframework>=3.7',
        'six'
    ],
    # mark test target to require extras.
    extras_require={
        'dev': ['coverage', 'mock', 'twine'],
        'docs': ['sphinx', 'sphinx_rtd_theme'],
    },
)
