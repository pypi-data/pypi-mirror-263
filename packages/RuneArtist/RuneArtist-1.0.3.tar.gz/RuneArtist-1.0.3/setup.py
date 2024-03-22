from setuptools import setup, find_packages

setup(
    name='RuneArtist',
    version='1.0.3',
    author='kekwak',
    author_email='kekwak@mail.ru',
    long_description_content_type='text/markdown',
    packages=find_packages(),
    package_data={
        'RuneArtist': ['pictures/*'],
    },
    install_requires=['requests>=2.25.1'],
    classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: Microsoft :: Windows',
    ],
    keywords='python',
    python_requires='>=3.7'
)