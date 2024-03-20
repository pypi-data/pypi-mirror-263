from setuptools import setup, find_packages

setup(
    name='model_infer_utils',
    version='0.0.3',
    packages=find_packages(
        exclude=["test", "*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[
        "nacos-sdk-python==0.1.7",
        "redis"
    ],
    author='wei.zhang',
    author_email='zhangwei@singularity-ai.com',
    description='A utils package for model-inference',
    license='MIT',
    keywords='utils model inference',
    # python_requires='>=3.6',
    #url='https://github.com/yourusername/mypackage'
)
