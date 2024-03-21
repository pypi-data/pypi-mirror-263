from setuptools import setup, find_packages
 
setup(name='mitcf',
      version='1.0.0',
      url='https://github.com/...',
      license='MIT',
      author='Florian Metzler',
      author_email='fmetzler@mit.edu',
      description='Log to Postgres DB',
      packages=find_packages(),
      install_requires=['psycopg2','numpy'],
      zip_safe=False)