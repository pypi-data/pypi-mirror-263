# !usr/bin/env python
# -*- coding:utf-8 -*-

'''
 Author       : Huang zh
 Email        : jacob.hzh@qq.com
 Date         : 2024-03-22 09:43:44
 LastEditTime : 2024-03-22 09:46:13
 FilePath     : \\hzh\\setup.py
 Description  : 
'''
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="hzh",  # 模块名称
    version="1.0",  # 当前版本
    author="leander",  # 作者
    author_email="1034235826@qq.com",  # 作者邮箱
    description="Get the high-frequency words in the paper to the local txt file, which is convenient to pass the word book to recite",  # 模块简介
    long_description=long_description,  # 模块详细介绍
    # long_description_content_type="text/markdown",  # 模块详细介绍格式
    # url="https://github.com/wupeiqi/fucker",  # 模块github地址
    packages=setuptools.find_packages(),  # 自动找到项目中导入的模块
    # 模块相关的元数据
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # 依赖模块
    install_requires=[
        "pypdf",
        "tqdm",
        "nltk"
    ],
    python_requires='>=3',
)