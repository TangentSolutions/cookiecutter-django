from setuptools import setup, find_packages


setup(
    name='',
    description='',
    install_requires=['django', 'djangorestframework'],
    extras_require={
        'dev': [
            'pytest',
            'pytest-sugar',
            'factory-boy',
            'django-coverage-plugin',
            'pytest-django',
            'pytest-profiling',
        ]
    },
)
