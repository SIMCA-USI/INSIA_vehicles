from glob import glob
from setuptools import setup, find_packages

package_name = 'insia_imiev'

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
    description='Vehiculo imiev para INSIA_control',
    license='GPL-3.0-only',
    entry_points={
        'console_scripts': [
            'brake_imiev = insia_imiev.BrakeNode:main',
            'steering_imiev = insia_imiev.SteeringNode:main',
            'telemetry_imiev = insia_imiev.TelemetryNode:main',
            'telemetry_imiev_srv = insia_imiev.TelemetryNodeSRV:main',
            'throttle_imiev = insia_imiev.ThrottleNode:main',
            'throttle_imiev_new = insia_imiev.ThrottleNode_new:main',
        ],
    },
)
