from glob import glob
from setuptools import setup, find_packages

package_name = 'insia_maqueta'

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
    description='Vehiculo maqueta para INSIA_control',
    license='GPL-3.0-only',
    entry_points={
        'console_scripts': [
            'brake_maqueta = insia_maqueta.BrakeNode:main',
            'steering_maqueta = insia_maqueta.SteeringNode:main',
            'telemetry_maqueta = insia_maqueta.TelemetryNode:main',
            'throttle_maqueta = insia_maqueta.ThrottleNode:main',
        ],
    },
)
