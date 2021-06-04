from setuptools import find_packages, setup
setup(
    name='mippae_libs',
    packages=find_packages(include=['mippae_libs']),
    version='0.1.0',
    description='Helpers for mippae project',
    author='Renato Martins',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)