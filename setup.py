import setuptools

setuptools.setup(
    name='dobot_serial',
    version='0.0.1',
    keywords='use py3 to control dobot',
    description='Present by Virobotics',
    author='hetong',
    author_email='hetongtech@hotmail.com',
    install_requires=['pyserial'],
    url='',
    packages=setuptools.find_packages(),
    package_dir = {'': './'},
    license='GPLv3',
    python_requires='>=3',
)

