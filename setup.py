from setuptools import setup

setup(
    name="ccli",
    version="1.0",
    py_modules=['ccli'],
    install_requires=[
        'Click'
    ],
    entry_points="""
        [console_scripts]
        ccli=ccli:main
    """
)
