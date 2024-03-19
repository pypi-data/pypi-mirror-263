from setuptools import setup, find_packages

setup(
    name='PyAnanyo',
    version='1.0.0',
    author='Ananyo Bhattacharya',
    author_email='ananyobhattacharya.14.15.0012@gmail.com',
    description='PyTools is a versatile Python library designed to provide developers with a wide range of tools and utilities for various tasks. From basic mathematical operations to complex geometry calculations, PyTools aims to simplify coding tasks and enhance productivity. With its intuitive API and comprehensive documentation, PyTools is suitable for beginners and experienced developers alike.',
    long_description='''
    PyTools is a versatile Python library designed to provide developers with a wide range of tools and utilities for various tasks. From basic mathematical operations to complex geometry calculations, PyTools aims to simplify coding tasks and enhance productivity. With its intuitive API and comprehensive documentation, PyTools is suitable for beginners and experienced developers alike.

    PyTools includes modules for basic mathematical operations (pymath.basic), geometric calculations (pymath.geometry), and utility functions (pyutils). The pymath.basic module provides functions for addition, subtraction, multiplication, and division, while the pymath.geometry module offers functions for calculating areas, volumes, and surface areas of various geometric shapes such as rectangles, squares, cuboids, cubes, circles, spheres, and cylinders. The pyutils module includes functions for handling user input, such as automatic conversion of string inputs to integer or float values.

    Whether you're working on a simple scripting task or a complex software project, PyTools can help streamline your development process and make your code more efficient and readable.
''',
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)