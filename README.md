# Vehiculo maqueta (insia_maqueta)

Rama `maqueta/main` del repositorio INSIA_vehicles. Contiene solo lo propio de este vehiculo.
El codigo comun esta en INSIA_control, que se descarga con `maqueta.repos`.

## Instalar en el ordenador del vehiculo

```bash
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src
git clone -b maqueta/main --single-branch https://github.com/SIMCA-USI/INSIA_vehicles.git insia_maqueta
vcs import < insia_maqueta/maqueta.repos
ln -sf ~/ros2_ws/src/insia_maqueta/vehicle.yaml ~/ros2_ws/vehicle.yaml
cd ~/ros2_ws && colcon build --symlink-install
```

## Arrancar

```bash
source ~/ros2_ws/install/setup.bash
export ROS_WS=~/ros2_ws
ros2 launch insia_maqueta <lanzador>
```

Lanzadores: `prueba_can.launch.py`.
