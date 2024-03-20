from setuptools import setup, find_packages

setup(
    name='sklearn_testing_demo',
    version='0.1',
    packages=find_packages(),
    install_requires=['requests'],
    author='p4nd4m4n',
    author_email='p4nd4m4n@example.com',
    description='This is merely to show what can happen if you are not careful about what packages you install via '
                'pip. DO NOT USE THIS',
    license='MIT',
)