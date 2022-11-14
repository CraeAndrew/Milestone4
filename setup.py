from setuptools import setup
import os
from glob import glob

package_name = "mile4"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (os.path.join("share", package_name), glob("launch/*_launch.py")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="crae",
    maintainer_email="craeandrew@ufl.edu",
    description="building controller",
    license="N/A",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
        'joy = mile4.joy:main',
        ],
    },
)
