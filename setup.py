from glob import glob
from setuptools import setup, find_packages

package_name = 'insia_jku'

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
    description='Vehiculo jku para INSIA_control',
    license='GPL-3.0-only',
    entry_points={
        'console_scripts': [
            'accel_jku_car = insia_jku.Car.AccelNode:main',
            'joy_transformer = insia_jku.JoyTransformerNode:main',
            'joy_transformer_pet = insia_jku.JoyTransformerPetNode:main',
            'speed_jku_robot = insia_jku.Robot.SpeedNode:main',
            'steering_jku_car = insia_jku.Car.SteeringNode:main',
            'steering_jku_robot = insia_jku.Robot.SteeringNode:main',
            'telemetry_jku_car = insia_jku.Car.Telemetry:main',
            'telemetry_jku_robot = insia_jku.Robot.Telemetry:main',
        ],
    },
)
