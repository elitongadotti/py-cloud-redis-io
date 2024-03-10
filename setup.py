from distutils.core import setup

setup(
    name='py-cloud-redis-io',
    version='1.0',
    packages=['py_cloud_redis_io'],
    url='https://github.com/elitongadotti/py-cloud-redis-io',
    license='Apache v2',
    author='py-cloud-redis-io',
    author_email='py-cloud-redis-io@github.com',
    description='A Python library for cloud-based Redis I/O operations using Apache Beam.',
    install_requires=[
        'redis',
        'apache-beam[gcp]'
    ],
)
