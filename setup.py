from setuptools import setup,find_packages





setup(
    name = "python_pytest",
    extra_require = dict(test=["pytest"],),
    packages = find_packages(where="scr"),
    package_dir = {"":"scr"}

)