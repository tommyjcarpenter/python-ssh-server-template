from setuptools import setup, find_packages

setup(
    name='server',
    version='0.0.1',
    packages=find_packages(exclude=["tests.*", "tests"]),
    author="",
    author_email="",
    description="",
    license="",
    keywords="",
    url="",
    zip_safe=False,
    install_requires=["asyncssh"],
    entry_points={
        'console_scripts': [
            'start = server.__main__:main'
        ]
    },
)
