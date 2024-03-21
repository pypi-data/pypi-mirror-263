import setuptools

with open("README.md", "r",encoding='UTF-8') as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="LdShell",  # 模块名称
    version="1.5",  # 当前版本
    author="LdShell",  # 作者
    author_email="83892778@vbblog.com",  # 作者邮箱
    description="LdShell",  # 模块简介
    long_description=long_description,  # 模块详细介绍
    long_description_content_type="text/markdown",  # 模块详细介绍格式
    packages=setuptools.find_packages(),  # 自动找到项目中导入的模块
    # 模块相关的元数据
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # 依赖模块
    install_requires=[
        'json','requests'
    ],
    python_requires='>=3',
)
