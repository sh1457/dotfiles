import setuptools

setuptools.setup(
    name='dotfiles',
    version='0.1.0',
    description='Manages literate markdown dotfiles',
    long_description='Manages literate markdown dotfiles',
    long_description_content_type='text/markdown',
    author='Sujith Sudarshan',
    author_email='sh1457@gmail.com',
    python_requires='>=3.7.0',
    url='https://github.com/sh1457/dotfiles',
    py_modules=['dotfiles'],
    entry_points={
        'console_scripts': ["df=dotfiles:main"],
    },
    install_requires=['click'],
    extras_require={},
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
