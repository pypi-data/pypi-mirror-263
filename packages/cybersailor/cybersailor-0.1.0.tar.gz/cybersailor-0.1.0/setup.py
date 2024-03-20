from setuptools import setup, find_packages

setup(
    name='cybersailor',
    version='0.1.0',
    packages=find_packages(),
    description='A simple example package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Carthooks',
    author_email='developer@carthooks.com',
    license='MIT',
    install_requires=[
        # 列出你的包的依赖，例如
        'requests>=2.23.0',
        'carthooks>=0.1.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)