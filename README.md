# Vehiculo ravo (insia_ravo)

Rama `ravo/main` del repositorio INSIA_vehicles. Contiene solo lo propio de este vehiculo.
El codigo comun esta en INSIA_control, que se descarga con `ravo.repos`.

## Instalar en el ordenador del vehiculo

```bash
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src
git clone -b ravo/main --single-branch https://github.com/SIMCA-USI/INSIA_vehicles.git insia_ravo
vcs import < insia_ravo/ravo.repos
ln -sf ~/ros2_ws/src/insia_ravo/vehicle.yaml ~/ros2_ws/vehicle.yaml
cd ~/ros2_ws && colcon build --symlink-install
```

## Arrancar

```bash
source ~/ros2_ws/install/setup.bash
export ROS_WS=~/ros2_ws
ros2 launch insia_ravo <lanzador>
```

Lanzadores: `ravo.launch.py`, `ravo_actuators.launch.py`, `ravo_socketcan.launch.py`, `ravo_telemetry.launch.py`, `ravo_test_ethernet.launch.py`, `ravo_test_socketcan.launch.py`, `ravo_trigger_manual.launch.py`.
