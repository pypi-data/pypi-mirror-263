from setuptools import setup, find_packages

setup(
    name='django-icon-picker',
    version='0.1.0',
    description='A custom widget for Django forms that allows users to select icons from a predefined set.',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/django-icon-picker',
    packages=find_packages(),
    install_requires=[
        'Django>=3.0',
        # Add other dependencies here
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
