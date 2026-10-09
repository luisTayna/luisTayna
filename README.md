```
        /\                      /\
       /  \      /\            /  \    /\
      /    \    /  \  /\      /    \  /  \        luis tayña
  ___/      \__/    \/  \____/      \/    \___    cusco, perú
```

Hola, soy Jose Luis. Hago backend, sobre todo con Laravel y últimamente con Next.js y TypeScript.
Acabo de terminar la carrera de Ingeniería Informática y de Sistemas en la UNSAAC.

Lo que más disfruto es meterle mano a sistemas que ya están en uso: entender por qué algo falla
con datos reales y arreglarlo sin romper lo que ya funciona.

### En qué ando

Estoy armando el **Centro Electoral Cusco**, una plataforma para llevar el control de personeros,
actas y resultados por región, provincia y distrito. Next.js 15, PostgreSQL y Prisma.
Lo más entretenido ha sido el tema de permisos: un coordinador solo puede ver su territorio, y si
algo no cuadra, el sistema no le muestra nada en vez de mostrarle todo.

### Lo que hice antes

Hice mis prácticas en **Noretel**, un proveedor de internet de Cusco, trabajando en su CRM (Laravel).
Cuando llegué, cada pago por Yape se validaba a mano: alguien abría la captura que el cliente mandaba
por WhatsApp y la comparaba con el celular de la empresa. Terminamos con una pasarela de WhatsApp,
OCR para leer las capturas y una conciliación automática contra la notificación del banco.
En agosto, los pagos por Yape ya se cerraban solos.

También me tocó una auditoría de seguridad y rendimiento. Mi favorito: un reporte que hacía
601 consultas a la base de datos para mostrar 20 facturas. Ahora hace 3.

Ese código es privado porque es de la empresa, pero si te interesa te lo puedo mostrar.

### Otras cosas en las que he trabajado

- **SIMU-UNSAAC**, un simulador del examen de admisión de la UNSAAC que armamos entre tres:
  backend en Go con Gin, frontend en Next.js, landing en Astro y MongoDB. Sigue en desarrollo.
- **Una red social universitaria** para un curso de Ingeniería de Software (React, Node.js con Express
  y MariaDB). Me tocó el módulo de publicaciones.
- **Mi tesis**: una app móvil que reconoce billetes peruanos con la cámara y los anuncia por voz, para
  personas con discapacidad visual. Estoy comparando modelos ligeros para que funcione sin internet.
- En los cursos de IA comparé redes para clasificar gestos de piedra, papel o tijera (MobileNetV2 ganó con
  93,65 %, probando con fotos mías y del conjunto original) y probé un clasificador cuántico con Qiskit
  contra un SVM. Quedó 63 % contra 61 %: interesante como experimento, nada más.

### Bugs que me enseñaron algo

- **Clientes fantasma.** WhatsApp empezó a mandar un identificador interno (LID) en lugar del número
  de teléfono, y el CRM lo guardaba como si fuera un celular. Desde ahí no confío en un dato externo
  sin verificar de dónde viene.
- **La factura que se cobraba dos veces.** Un mes escrito como `01/08/2026 al 31/08/2026` y otro como
  `agosto 2026` eran, para el sistema, dos meses distintos. Lo resolví normalizando el periodo y
  validándolo dentro de la misma transacción que crea la factura.
- **`Undefined constant "key"`.** Un gráfico mezclaba una variable de JavaScript dentro de una directiva
  de Blade. El reporte tiraba error 500 y nadie sabía por qué.
- **La terminal que cualquiera podía usar.** La consola SSH de los routers solo pedía haber iniciado
  sesión. Ahora pide un permiso y deja registro de cada comando.

### Herramientas

Uso a diario: Laravel, PHP, TypeScript, Next.js, MySQL, PostgreSQL, Git.
Las he usado en algo real: Prisma, Docker, NestJS, Python, Tailwind, PHPUnit.
Me falta mucho por aprender, pero me gusta escribir la prueba antes que el arreglo.

---

Si quieres conversar sobre algún proyecto o tienes una oportunidad, escríbeme a **luis113654@gmail.com**.
