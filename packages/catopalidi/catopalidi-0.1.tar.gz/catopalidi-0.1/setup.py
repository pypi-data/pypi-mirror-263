from setuptools import setup, find_packages

setup(
    name='catopalidi',
    version='0.1',
    author='Aleksandra',
    author_email='topalidia@gmail.com',
    description='Библиотека для генерации LaTeX кода для таблиц и изображений',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Enc0der/PythonCourse',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6', 
)
