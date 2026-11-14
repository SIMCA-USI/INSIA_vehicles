# Vehiculo imiev (insia_imiev)

Rama `imiev/main` del repositorio INSIA_vehicles. Contiene solo lo propio de este vehiculo.
El codigo comun esta en INSIA_control, que se descarga con `imiev.repos`.

## Instalar en el ordenador del vehiculo

```bash
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src
git clone -b imiev/main --single-branch https://github.com/SIMCA-USI/INSIA_vehicles.git insia_imiev
vcs import < insia_imiev/imiev.repos
ln -sf ~/ros2_ws/src/insia_imiev/vehicle.yaml ~/ros2_ws/vehicle.yaml
cd ~/ros2_ws && colcon build --symlink-install
```

## Arrancar

```bash
source ~/ros2_ws/install/setup.bash
export ROS_WS=~/ros2_ws
ros2 launch insia_imiev <lanzador>
```

Lanzadores: `calibracion_freno_maxon.launch.py`, `control_imiev.launch.py`, `control_todo.launch.py`, `demo_pista_imiev.launch.py`, `enrique.launch.py`, `imiev.launch.py`, `imiev_IA.launch.py`, `imiev_con_drivercan_servicio.launch.py`, `imiev_new.launch.py`, `imiev_test_actuators.launch.py`, `imiev_test_throttle.launch.py`, `test_imiev.launch.py`, `test_maleta.launch.py`, `testio.launch.py`.
