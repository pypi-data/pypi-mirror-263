#!/usr/bin/env python
#   -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'pybuilder-bandit',
        version = '0.3.2',
        description = 'Pybuilder plugin for bandit security linter',
        long_description = "# pybuilder-bandit\n[![GitHub Workflow Status](https://github.com/soda480/pybuilder-bandit/workflows/build/badge.svg)](https://github.com/soda480/pybuilder-bandit/actions)\n[![coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://pybuilder.io/)\n[![complexity](https://img.shields.io/badge/complexity-A-brightgreen)](https://radon.readthedocs.io/en/latest/api.html#module-radon.complexity)\n[![PyPI version](https://badge.fury.io/py/pybuilder-bandit.svg)](https://badge.fury.io/py/pybuilder-bandit)\n[![python](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-teal)](https://www.python.org/downloads/)\n\nA pybuilder plugin that analyzes your project for common security issues using `bandit`. Bandit is a security linter for Python code, for more information refer to the [bandit pypi page](https://pypi.org/project/bandit/).\n\nTo add this plugin into your pybuilder project, add the following line near the top of your build.py:\n```python\nuse_plugin('pypi:pybuilder_bandit')\n```\n\n**NOTE** if you are using Pybuilder version `v0.11.x`, then specify the following version of the plugin:\n```python\nuse_plugin('pypi:pybuilder_bandit', '~=0.1.3')\n```\n\n### Pybuilder bandit properties\n\nThe pybuilder task `pyb bandit` will use bandit to scan your project to find common security issues, verbose mode will display to the screen any issues found. The following plugin properties are available to further configure the scan.\n\nName | Type | Default Value | Description\n-- | -- | -- | --\nbandit_break_build | bool | False | Fail build if scan detects any issues\nbandit_confidence_level | str | LOW | Report only issues of a given confidence level or higher: LOW, MEDIUM, HIGH\nbandit_severity_level | str | LOW | report only issues of a given severity level or higher: LOW, MEDIUM, HIGH\nbandit_skip_ids | str | None | comma-separated list of test IDs to skip\nbandit_include_testsources | bool | False | include scanning of project test sources\nbandit_include_scripts | bool | False | include scanning of project scripts\n\nThe plugin properties are set using `project.set_property`, the following is an example of how to set the properties:\n\n```Python\nproject.set_property('bandit_break_build', True)\nproject.set_property('bandit_confidence_level', 'LOW')\nproject.set_property('bandit_severity_level', 'MEDIUM')\nproject.set_property('bandit_skip_ids', 'B110,B315')\nproject.set_property('bandit_include_testsources', True)\nproject.set_property('bandit_include_scripts', True)\n```\n\n### Development\n\nClone the repository and ensure the latest version of Docker is installed on your development server.\n\nBuild the Docker image:\n```sh\ndocker image build \\\n-t pybbandit:latest .\n```\n\nRun the Docker container:\n```sh\ndocker container run \\\n--rm \\\n-it \\\n-v $PWD:/code \\\npybbandit:latest \\\nbash\n```\n\nExecute the build:\n```sh\npyb -X\n```\n",
        long_description_content_type = 'text/markdown',
        classifiers = [
            'Development Status :: 4 - Beta',
            'Environment :: Other Environment',
            'Environment :: Plugins',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Topic :: Software Development :: Build Tools'
        ],
        keywords = '',

        author = 'Emilio Reyes',
        author_email = 'soda480@gmail.com',
        maintainer = '',
        maintainer_email = '',

        license = 'Apache License, Version 2.0',

        url = 'https://github.com/soda480/pybuilder-bandit',
        project_urls = {},

        scripts = [],
        packages = ['pybuilder_bandit'],
        namespace_packages = [],
        py_modules = [],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = ['bandit'],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        python_requires = '',
        obsoletes = [],
    )
