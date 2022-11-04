import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read().split('\n')

setuptools.setup(
    name='sqlalchemy-utils',
    version='0.0.1',
    author='Tom Antonov',
    author_email='artyom.antnv@gmail.com',
    description='...',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/skipp1/S954_Skipp3_0/rabbitmq_client',
    packages=setuptools.find_packages(),
    install_requires=[

    ],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.10',
)
