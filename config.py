"""
config.py
Parametros de configuracion del nodo de telemetria.
Todo lo que puede cambiar entre una instalacion y otra vive aqui.
Ningun otro archivo del proyecto debe contener un numero literal.

Unidad 2 - Programacion en Python para sistemas IoT
Facultad de Ingenieria de Sistemas Computacionales - UTP
"""

import os

# --------------------------------------------------------------------------
# Identificacion del nodo   <<< CAMBIA ESTOS DOS VALORES POR LOS TUYOS >>>
# --------------------------------------------------------------------------
NODO = "laptop-lab3"
UBICACION = "Laboratorio 3 - FISC"

# --------------------------------------------------------------------------
# Periodos de muestreo, en segundos.
# Cada metrica tiene el suyo: leer los procesos es caro, leer la CPU no.
# --------------------------------------------------------------------------
PERIODO_RAPIDO = 1.0        # cpu, memoria, red
PERIODO_LENTO = 5.0         # disco, procesos, bateria
PERIODO_REPORTE = 30.0      # resumen periodico hacia la bitacora
REFRESCO_MS = 200           # cada cuanto refresca el dashboard (milisegundos)

# --------------------------------------------------------------------------
# Umbrales. Dos valores por metrica: uno para entrar en alarma y otro,
# mas bajo, para salir de ella. Esa diferencia es la HISTERESIS y evita
# que una lectura oscilando en el limite genere decenas de eventos falsos.
# --------------------------------------------------------------------------
CPU_ALTO = 70.0
CPU_BAJO = 50.0
CPU_NUCLEO_SATURADO = 90.0  # un nucleo individual por encima de esto

RAM_ALTA = 85.0
RAM_BAJA = 75.0

DISCO_LLENO = 90.0          # porcentaje de ocupacion
DISCO_ALIVIADO = 85.0

RED_PICO_KBS = 500.0        # kilobytes por segundo
RED_CALMA_KBS = 200.0

BATERIA_BAJA = 20.0
BATERIA_RECUPERADA = 30.0

PROCESO_PESADO = 50.0       # % de CPU de un solo proceso

# Variacion brusca entre dos muestras consecutivas: evento de anomalia.
SALTO_ANOMALO = 40.0

# --------------------------------------------------------------------------
# Ventana movil y almacenamiento
# --------------------------------------------------------------------------
VENTANA = 10                # muestras que se promedian para evaluar el umbral
MAX_EVENTOS_LOG = 200       # eventos que se conservan en pantalla
ARCHIVO_BITACORA = "bitacora.json"

# --------------------------------------------------------------------------
# Unidad de disco a vigilar. Se detecta sola segun el sistema operativo.
# --------------------------------------------------------------------------
UNIDAD_DISCO = "C:\\" if os.name == "nt" else "/"

# Cantidad de procesos que se muestran en el ranking.
TOP_PROCESOS = 8

# Procesos del sistema que no vale la pena reportar: en Linux los
# 'kworker' y 'kthread' aparecen y desaparecen constantemente y llenarian
# la bitacora de ruido.
PROCESOS_IGNORADOS = ("kworker", "kthread", "ksoftirqd", "migration",
                      "rcu_", "irq/", "svchost")


# ==========================================================================
# LABORATORIO N.°1 - Alertas sonoras y conexion de red
# Todo lo nuevo (sonidos, tiempos, umbrales) vive aqui.
# ==========================================================================

# --- Control general del sonido  # LABORATORIO
SONIDO_ACTIVO = True            # False apaga por completo las alertas sonoras
MODO_SILENCIOSO = False         # True: no suena nada, solo se anota en la bitacora
                                # (tambien se activa con: python main.py --silencioso)
ALERTA_ENFRIAMIENTO_S = 5.0     # segundos minimos entre dos sonidos del mismo evento
ALERTAS_COLA_MAX = 4            # alertas que pueden esperar turno; si se llena, se descarta la mas antigua
SONIDO_TICK_MS = 50             # cada cuanto se avanza la cola de sonidos (dashboards y --probar-sonidos)
MS_POR_SEGUNDO = 1000.0

# --- Conexion de red  # LABORATORIO
PERIODO_CONEXION = 1.0          # cada cuanto se revisa si hay enlace de red (segundos)
RED_RECORDATORIO_S = 30.0       # recordatorio mientras la red siga caida (segundos)
# Interfaces que no cuentan como "red real": bucle local, virtuales, contenedores.
INTERFACES_IGNORADAS = ("lo", "Loopback", "vEthernet", "docker", "veth",
                        "br-", "virbr", "utun", "awdl", "llw", "bridge",
                        "gif", "stf", "anpi")

# --- Tabla de alertas sonoras  # LABORATORIO
# Cada alerta es una secuencia de notas (frecuencia_Hz, duracion_ms).
# Frecuencia SILENCIO = pausa. Rango valido de winsound.Beep: 37 a 32767 Hz.
SILENCIO = 0
SONIDOS = {
    # CPU: tres pitidos agudos y rapidos, como un motor acelerado.
    "cpu_alta": ((1200, 100), (SILENCIO, 60), (1200, 100), (SILENCIO, 60),
                 (1200, 100)),
    # Memoria: dos tonos graves, largos y lentos; suenan "pesados", como algo que se llena.
    "ram_alta": ((330, 450), (SILENCIO, 100), (330, 450)),
    # Trafico: dos tonos alternados rapidos, como una sirena de flujo intenso.
    "red_pico": ((880, 100), (660, 100), (880, 100), (660, 100)),
    # Conexion perdida: tres notas descendentes ("se pierde la senal").
    "red_desconectada": ((900, 180), (600, 180), (300, 400)),
    # Conexion recuperada: dos notas ascendentes ("vuelve la senal").
    "red_conectada": ((600, 150), (900, 300)),
    # Recordatorio: un solo tono grave y corto, discreto pero constante.
    "red_sigue_desconectada": ((440, 250),),
}
