from setuptools import setup, find_packages

setup(
    name='bugswarm-cfg',
    version='0.2.0',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'bugswarm-cfg=bugswarm_cfg.main:main',
        ],
    },
    install_requires=[
        'beautifulsoup4',
        'requests',
    ],
    package_data={
        'bugswarm_cfg': ['*.sh'],
    },
    # Meta data
    author="Apratim Shukla",
    author_email="apratimshukla6@gmail.com",
    description="A tool to run BugSwarm Docker containers with sandbox environments for CFG generation using various tools.",
    license="MIT",
    keywords="bugswarm cfg",
    url="https://github.com/apratimshukla6/bugswarm-cfg",   # project home page
)