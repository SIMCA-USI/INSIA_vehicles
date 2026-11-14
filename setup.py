from glob import glob
from setuptools import setup, find_packages

package_name = 'insia_mutt8x8'

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
    description='Vehiculo mutt8x8 para INSIA_control',
    license='GPL-3.0-only',
    entry_points={
        'console_scripts': [
            'canadac_mutt = insia_mutt8x8.CANADAC_MUTT:main',
            'control_mutt = insia_mutt8x8.MUTTControl:main',
            'decision_mutt = insia_mutt8x8.decision_MUTT:main',
            'device_mutt = insia_mutt8x8.MUTT_Device_Node:main',
            'telemetry_mutt = insia_mutt8x8.Telemetry_Basic:main',
        ],
    },
)
