# Vehiculo mutt6x6 (insia_mutt6x6)

Rama `mutt6x6/main` del repositorio INSIA_vehicles. Contiene solo lo propio de este vehiculo.
El codigo comun esta en INSIA_control, que se descarga con `mutt6x6.repos`.

## Instalar en el ordenador del vehiculo

```bash
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src
git clone -b mutt6x6/main --single-branch https://github.com/SIMCA-USI/INSIA_vehicles.git insia_mutt6x6
vcs import < insia_mutt6x6/mutt6x6.repos
ln -sf ~/ros2_ws/src/insia_mutt6x6/vehicle.yaml ~/ros2_ws/vehicle.yaml
cd ~/ros2_ws && colcon build --symlink-install
```

## Arrancar

```bash
source ~/ros2_ws/install/setup.bash
export ROS_WS=~/ros2_ws
ros2 launch insia_mutt6x6 <lanzador>
```

Lanzadores: `mutt.launch.py`, `mutt_actuators.launch.py`.
