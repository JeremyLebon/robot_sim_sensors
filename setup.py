from setuptools import setup
import os
from glob import glob

package_name = 'robot_sim_sensors'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf/basic_sensors'), glob('urdf/basic_sensors/*.xacro')),
        (os.path.join('share', package_name, 'urdf/brand_sensors'), glob('urdf/brand_sensors/*.xacro')),
        (os.path.join('share', package_name, 'urdf/'), glob('urdf/*.xacro')),
                
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='jeremy.lebon@vives.be',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
