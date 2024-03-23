from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='pyweb_moderator_api',
  version='1.2.0',
  author='pywebsol',
  author_email='pywebsolutions.ru@gmail.com',
  description='Library for using the API for PyWeb AI Moderator.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/pywebsol',
  packages=find_packages(),
  install_requires=['requests', 'aiohttp', 'urllib3'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='antispam moderator ai api pyweb pywebsol',
  project_urls={
    # 'GitHub': 'pywebsol',
    'Telegram': 'https://t.me/RuModeratorAI_API_Bot'
  },
  python_requires='>=3.6'
)