from setuptools import setup

readme = open("./README.md", "r")


setup(
    name='termcolorEasy',
    packages=['termcolorEasy'],  # this must be the same as the name above
    version='0.1',
    description='Versión mejorada de la libreria termcolor con una mayor facilidad de uso',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='Adria Cabrera',
    author_email='adriacabrera2007@gmail.com',
    # use the URL to the github repo
    url='https://github.com/adriaCabrera',
    download_url='https://github.com/adriaCabrera/termcolorEasy',
    keywords=['testing', 'logging', 'example'],
    classifiers=[ ],
    license='MIT',
    include_package_data=True
)