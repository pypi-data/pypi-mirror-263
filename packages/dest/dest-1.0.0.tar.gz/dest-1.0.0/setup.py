# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  setup.py
@Description    :
@CreateTime     :  2023/3/22 12:18
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/3/22 12:18
"""

from setuptools import setup, find_packages

from weeeTest.version import version

"""
打包命令: python setup.py sdist bdist_wheel
上传服务命令: twine upload dist/*
"""


def _process_requirements():
    packages = open('requirements.txt', encoding='utf-8').read().strip().split('\n')
    requires = []
    for pkg in packages:
        requires.append(pkg)
    return requires


setup(
    name='weeeTest',
    version=version,
    url='https://www.weee.com',
    license='Apache License 2.0',
    author='yingqing.shan, jialing.chen',
    author_email='yingqing.shan@sayweee.com, jialing.chen@sayweee.com',
    description="weeeTest automation testing framework based on pytest.",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    data_files=[],
    # 依赖的三方库的版本
    install_requires=_process_requirements(),
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        # 发展时期,常见的如下
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        # 开发的目标用户
        'Intended Audience :: Developers',
        # 属于什么类型
        'Topic :: Software Development :: Build Tools',
        # 许可证信息
        'License :: OSI Approved :: MIT License',
        # 目标 Python 版本
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Framework :: Pytest',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        # "Topic :: Software Development :: Testing",
    ],
    python_requires=">=3.9",
    entry_points={
        'pytest11': [
            'weee-pytest= weeeTest.pytest_plugin',
        ],
        'console_scripts': [
            'weeeTest=weeeTest.cli:main',
        ]
    },

)
