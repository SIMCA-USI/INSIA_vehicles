from glob import glob
from setuptools import setup, find_packages

package_name = 'insia_gdels'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml'] + glob('vehicle*.yaml')),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
        ('share/' + package_name + '/conf', glob('conf/*')),
        ('share/' + package_name + '/diccionarios', glob('diccionarios/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Alfredo Valle Barrio',
    maintainer_email='alfredo.valle@upm.es',
    description='Vehiculo gdels para INSIA_control',
    license='GPL-3.0-only',
    entry_points={
        'console_scripts': [
            'brake_gdels = insia_gdels.BrakeNode:main',
            'steering_gdels = insia_gdels.SteeringNode:main',
            'telemetry_gdels = insia_gdels.TelemetryNode:main',
            'throttle_gdels = insia_gdels.ThrottleNode:main',
        ],
    },
)
