from setuptools import setup

setup(name='NLTK 3.0 Simple API',
      version='1.0.0',
      packages=['nltk_api'],
      test_suite='tests',
      entry_points={
          'console_scripts': [
              'nltk_api = nltk_api.__main__:main'
          ]
      }, install_requires=['flask', 'gevent', 'nltk', 'nose']
      )
