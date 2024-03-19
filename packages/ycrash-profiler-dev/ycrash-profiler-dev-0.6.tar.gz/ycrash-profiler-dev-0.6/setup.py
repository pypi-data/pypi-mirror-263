from setuptools import setup, find_packages

setup(
    name='ycrash-profiler-dev',
    version='0.6',
    packages=find_packages(exclude=['tests*']),
    description='yCrash Python Agent',
    install_requires=['pyyaml', 'requests', 'memory_profiler','psutil'],
    url='https://ycrash.io',
    author='YCrash Team',
    author_email='team@tier1app.com'
)
