from setuptools import find_packages
from setuptools import setup
from setuptools.command.install import install

class CustomCommands(install):

	def RunCustomCommand(self, command_list):
		p = subprocess.Popen(
        command_list,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
		stdout_data, _ = p.communicate()
		logging.info('Log command output: %s', stdout_data)
		if p.returncode != 0:
			raise RuntimeError('Command %s failed: exit code: %s' %
                         (command_list, p.returncode))

	def run(self):
		self.RunCustomCommand(['apt-get', 'update'])
		self.RunCustomCommand(
          ['apt-get', 'install', '-y', 'python-tk'])
		install.run(self)

REQUIRED_PACKAGES = ['matplotlib']

setup(
    name='trainer',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='My trainer application package.'
)
