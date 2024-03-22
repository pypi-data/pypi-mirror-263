from distutils.core import setup
from setuptools import find_packages

setup(
    name = 'niologsimjobcreator',
    version = '0.1',
    description = '任务创建查询工具',
    author = 'sankin.su',
    author_email = '1298237220@qq.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'}
)