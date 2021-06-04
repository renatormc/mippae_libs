from setuptools import find_packages, setup
setup(
    name='mippae_libs',
    packages=find_packages(include=['mippae_libs']),
    version='0.1.1',
    description='Helpers for mippae project',
    author='Renato Martins',
    license='MIT',
    install_requires=[],
    setup_requires=[
        'pytest-runner',
        'click',
        'Flask',
        'itsdangerous',
        'Jinja2',
        'MarkupSafe',
        'PyJWT',
        'Werkzeug',
    ],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
