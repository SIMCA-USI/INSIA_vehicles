# Vehiculo mutt8x8 (insia_mutt8x8)

Rama `mutt8x8/main` del repositorio INSIA_vehicles. Contiene solo lo propio de este vehiculo.
El codigo comun esta en INSIA_control, que se descarga con `mutt8x8.repos`.

## Instalar en el ordenador del vehiculo

```bash
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src
git clone -b mutt8x8/main --single-branch https://github.com/SIMCA-USI/INSIA_vehicles.git insia_mutt8x8
vcs import < insia_mutt8x8/mutt8x8.repos
ln -sf ~/ros2_ws/src/insia_mutt8x8/vehicle.yaml ~/ros2_ws/vehicle.yaml
cd ~/ros2_ws && colcon build --symlink-install
```

## Arrancar

```bash
source ~/ros2_ws/install/setup.bash
export ROS_WS=~/ros2_ws
ros2 launch insia_mutt8x8 <lanzador>
```

Lanzadores: `mutt.launch.py`.
