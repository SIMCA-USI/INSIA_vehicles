# INSIA_vehicles

Configuracion de cada vehiculo para INSIA_control. **Cada vehiculo es una rama** y solo contiene sus ficheros.
El codigo comun esta en https://github.com/SIMCA-USI/INSIA_control.

| Rama | Vehiculo | Paquete ROS 2 |
|---|---|---|
| `imiev/main` | Mitsubishi i-MiEV | `insia_imiev` |
| `emt/main` | Gulliver (EMT) | `insia_emt` |
| `irizar/main` | Autobus Irizar (EMT gris) | `insia_irizar` |
| `lagarto/main` | Volvo A25 | `insia_lagarto` |
| `ascod/main` | ASCOD | `insia_ascod` |
| `gdels/main` | Simulador GDELS | `insia_gdels` |
| `jku/main` | JKU: RAV4 y robot | `insia_jku` |
| `maqueta/main` | Maqueta de laboratorio | `insia_maqueta` |
| `mutt6x6/main` | MUTT 6x6 | `insia_mutt6x6` |
| `mutt8x8/main` | MUTT 8x8 | `insia_mutt8x8` |
| `ravo/main` | Barredora RAVO | `insia_ravo` |

Esta rama `main` solo guarda este indice y la documentacion de fabricantes (`doc/`). No se clona en los vehiculos.

Instalar un vehiculo (ejemplo iMiEV):

```bash
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src
git clone -b imiev/main --single-branch https://github.com/SIMCA-USI/INSIA_vehicles.git insia_imiev
vcs import < insia_imiev/imiev.repos
```

Reglas: nunca fusionar una rama de vehiculo con otra. Lo que sirva a varios vehiculos va a INSIA_control.
