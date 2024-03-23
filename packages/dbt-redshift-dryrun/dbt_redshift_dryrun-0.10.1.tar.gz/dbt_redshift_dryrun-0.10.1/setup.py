from setuptools import setup

setup(
    name='dbt_redshift_dryrun',
    version='0.10.1',  
    entry_points = {
        'console_scripts': ['dryrun=dbt_redshift_dryrun.app:cli'],
    },
    description='Python package dry running redshift queries',
    url='https://github.com/shassaan/dbt-redshift-dryrun',
    author='Syed Hassaan Ahmed',
    author_email='syedhassaan.103@gmail.com',
    license='BSD 2-clause',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=['dbt_redshift_dryrun'],
    install_requires=[],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)