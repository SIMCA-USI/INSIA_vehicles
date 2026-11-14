# Vehiculo emt (insia_emt)

Rama `emt/main` del repositorio INSIA_vehicles. Contiene solo lo propio de este vehiculo.
El codigo comun esta en INSIA_control, que se descarga con `emt.repos`.

## Instalar en el ordenador del vehiculo

```bash
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src
git clone -b emt/main --single-branch https://github.com/SIMCA-USI/INSIA_vehicles.git insia_emt
vcs import < insia_emt/emt.repos
ln -sf ~/ros2_ws/src/insia_emt/vehicle.yaml ~/ros2_ws/vehicle.yaml
cd ~/ros2_ws && colcon build --symlink-install
```

## Arrancar

```bash
source ~/ros2_ws/install/setup.bash
export ROS_WS=~/ros2_ws
ros2 launch insia_emt <lanzador>
```

Lanzadores: `emt.launch.py`, `emt_ia.launch.py`, `emt_tele.launch.py`, `emt_test_gears.launch.py`, `test_LonC.launch.py`.
