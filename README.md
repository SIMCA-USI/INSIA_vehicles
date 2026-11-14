# Vehiculo jku (insia_jku)

Rama `jku/main` del repositorio INSIA_vehicles. Contiene solo lo propio de este vehiculo.
El codigo comun esta en INSIA_control, que se descarga con `jku.repos`.

## Instalar en el ordenador del vehiculo

```bash
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src
git clone -b jku/main --single-branch https://github.com/SIMCA-USI/INSIA_vehicles.git insia_jku
vcs import < insia_jku/jku.repos
ln -sf ~/ros2_ws/src/insia_jku/vehicle_car.yaml ~/ros2_ws/vehicle.yaml
cd ~/ros2_ws && colcon build --symlink-install
```

## Arrancar

```bash
source ~/ros2_ws/install/setup.bash
export ROS_WS=~/ros2_ws
ros2 launch insia_jku <lanzador>
```

Lanzadores: `JKU.launch.py`, `JKU_Car.launch.py`, `JKU_Pet_pruebas.launch.py`, `JKU_Robot.launch.py`.
