from setuptools import setup, find_packages

setup(
    name='KafkaRobotLibrary',
    version='0.1.0',
    author='Andre Nunes',
    author_email='andre.nunes@gmail.com',
    description='Uma biblioteca do Robot Framework para interação com o Kafka.',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'kafka-python',
        'robotframework'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Robot Framework',
    ],
    keywords='robotframework kafka testing',
)