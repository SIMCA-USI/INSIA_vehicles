# Vehiculo irizar (insia_irizar)

Rama `irizar/main` del repositorio INSIA_vehicles. Contiene solo lo propio de este vehiculo.
El codigo comun esta en INSIA_control, que se descarga con `irizar.repos`.

## Instalar en el ordenador del vehiculo

```bash
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src
git clone -b irizar/main --single-branch https://github.com/SIMCA-USI/INSIA_vehicles.git insia_irizar
vcs import < insia_irizar/irizar.repos
ln -sf ~/ros2_ws/src/insia_irizar/vehicle.yaml ~/ros2_ws/vehicle.yaml
cd ~/ros2_ws && colcon build --symlink-install
```

## Arrancar

```bash
source ~/ros2_ws/install/setup.bash
export ROS_WS=~/ros2_ws
ros2 launch insia_irizar <lanzador>
```

Lanzadores: `bus_irizar.launch.py`.
