# Vehiculo ascod (insia_ascod)

Rama `ascod/main` del repositorio INSIA_vehicles. Contiene solo lo propio de este vehiculo.
El codigo comun esta en INSIA_control, que se descarga con `ascod.repos`.

## Instalar en el ordenador del vehiculo

```bash
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src
git clone -b ascod/main --single-branch https://github.com/SIMCA-USI/INSIA_vehicles.git insia_ascod
vcs import < insia_ascod/ascod.repos
ln -sf ~/ros2_ws/src/insia_ascod/vehicle.yaml ~/ros2_ws/vehicle.yaml
cd ~/ros2_ws && colcon build --symlink-install
```

## Arrancar

```bash
source ~/ros2_ws/install/setup.bash
export ROS_WS=~/ros2_ws
ros2 launch insia_ascod <lanzador>
```

Lanzadores: `ascod.launch.py`, `ascod_actuators.launch.py`, `gdels.launch.py`, `pruebaascodfile.launch.py`, `simulador_ascod.launch.py`.
