# Misión excursión: planifica la aventura

Ejemplo resuelto con datos hipotéticos. No es la única respuesta válida: el docente debe revisar el razonamiento y confirmar los datos antes de organizar una salida real.

## Problema

Planificar una visita de dos horas a un centro de ciencias para 24 estudiantes y dos acompañantes. El grupo debe regresar a la escuela antes de las 11:45 y no gastar más de $180.

## Entradas

- Participantes: 24 estudiantes y dos acompañantes, 26 personas en total.
- Transporte propuesto: autobús con 30 plazas, costo total de ida y vuelta de $100 y trayectos de 30 minutos.
- Entrada hipotética: $2 por persona; el centro abre a las 08:30.
- Horario disponible: salida de la escuela a las 08:00 y regreso antes de las 11:45.
- Presupuesto: $180; se requiere confirmar permisos y reserva antes de salir.

## Salidas

- Lista de 26 participantes con sus permisos y dos responsables.
- Itinerario: 08:00 salida; 08:30 llegada; 08:45–10:45 visita; 11:00 regreso; 11:30 llegada a la escuela.
- Presupuesto: entradas $52 más transporte $100, total $152 y reserva de $28.
- Una alternativa elegida y una explicación de por qué respeta tiempo, capacidad y presupuesto.

## Subproblemas

- Confirmar participantes, permisos y responsables antes de reservar.
- Comparar capacidad, costo y duración de las opciones de transporte.
- Calcular el costo de las 26 entradas y el transporte completo.
- Distribuir los horarios de traslado, ingreso y visita de dos horas.
- Revisar que el regreso sea anterior a las 11:45 y el costo no supere $180.
- Asignar un acompañante al frente y otro al final, y contar al grupo al salir, cambiar de lugar y regresar.

## Pseudocódigo

```text
LEER participantes, permisos, plazas, precios y horarios confirmados
SI faltan permisos o no están disponibles los dos acompañantes
    POSPONER la salida y completar esos requisitos
SI NO
    CALCULAR entradas = 26 * 2
    CALCULAR total = entradas + 100
    PROPONER salida 08:00, visita 08:45 a 10:45 y regreso 11:30
    SI plazas >= 26 Y total <= 180 Y regreso < 11:45
        RESERVAR el transporte y el ingreso con los datos confirmados
        REGISTRAR responsables, lista de participantes e itinerario
        INFORMAR total 152 y reserva 28
    SI NO
        COMPARAR otra alternativa o reprogramar; no confirmar un plan inviable
```

## Alternativas

- Autobús reservado: 30 plazas para 26 personas, trayectos de 30 minutos y total de $152. Permite la visita completa y el regreso a las 11:30.
- Caminar: se supone un trayecto de 75 minutos por sentido. Ahorraría $100, pero salir a las 08:00, comenzar la visita a las 09:30, terminarla a las 11:30 y caminar de regreso llevaría hasta las 12:45; no cumple el límite de regreso.

## Justificación

Se elige el autobús porque deja cuatro plazas libres, permite dos horas completas de visita y regresa con 15 minutos de margen. El costo de $152 queda $28 por debajo del presupuesto. Caminar cuesta menos, pero incumple el horario y no es una alternativa equivalente bajo las restricciones dadas. Los precios, tiempos, disponibilidad y permisos son supuestos del ejemplo que deben confirmarse antes de una salida real.
