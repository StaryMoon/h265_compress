from setuptools import setup, find_packages

setup(
    name="h265_compress",  # 库名
    version="0.1",  # 版本
    packages=find_packages(),
    install_requires=[
        'ffmpeg-python',  # 依赖库
    ],
    description="A Python library to compress YUV files to H.265 MP4.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Minghao Liu",  # 你的名字
    author_email="minghao13187@gmail.com",  # 你的邮箱
    url="https://github.com/yourusername/h265_compress",  # 项目的GitHub URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # 许可证信息
        'Operating System :: OS Independent',
    ],
    license="MIT",  # 许可证类型
)
