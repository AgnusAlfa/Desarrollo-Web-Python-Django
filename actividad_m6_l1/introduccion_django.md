1. ¿Qué es Django?

• ¿Qué tipo de framework es Django?

Django es un framework de desarrollo web escrito en Python. Se le conoce comúnmente como un framework de tipo full-stack. Esto significa que ofrece la estructura básica para programar y trae preintegradas la gran mayoría de las herramientas necesarias para construir un sitio web robusto (como conexión a bases de datos, sistema de plantillas, y enrutamiento) sin tener que buscar e instalar constantemente librerías de terceros.

• ¿Qué tipo de aplicaciones permite construir?

Gracias a su versatilidad, Django permite construir prácticamente cualquier tipo de plataforma web. Es ideal para aplicaciones que manejan grandes volúmenes de datos o tráfico. Con él se pueden desarrollar desde sistemas de gestión de contenidos (CMS) y periódicos digitales, hasta plataformas de e-commerce, redes sociales, sistemas de reservas y APIs para conectar con aplicaciones móviles.

• Menciona al menos tres ventajas de usar Django sobre trabajar con Python puro para desarrollo web.

1.Al programar con Python puro, tendríamos que construir desde cero el servidor, la seguridad, la conexión a la base de datos y el panel de administración. Django ya trae todo esto resuelto, permitiendo enfocarnos directamente en la lógica específica de nuestro proyecto.

2.Django está diseñado para ayudar a los desarrolladores a evitar errores de seguridad comunes. De manera automática, nos protege contra vulnerabilidades críticas como inyecciones SQL, Cross-Site Scripting (XSS) y Cross-Site Request Forgery (CSRF). Programar estas defensas manualmente en Python puro es complejo y propenso a errores.

3.Django nos obliga a seguir buenas prácticas y a mantener nuestro código ordenado bajo una arquitectura específica. Esto facilita enormemente el trabajo en equipo, el mantenimiento del código a largo plazo y permite que la aplicación crezca sin colapsar.

2. Entornos virtuales en Python

• ¿Qué es un entorno virtual en Python y para qué sirve?

Un entorno virtual es un espacio aislado dentro de nuestra computadora que nos permite instalar librerías y paquetes de Python de forma independiente para un proyecto específico. Sirve principalmente para evitar conflictos de dependencias; es decir, permite que un proyecto "A" use una versión antigua de una librería sin que esto interfiera con un proyecto "B" que requiere la versión más reciente de esa misma librería en el mismo equipo.

• ¿Qué ventajas tiene crear un entorno virtual para un proyecto Django?

1.Django evoluciona constantemente. Crear un entorno virtual nos asegura que la versión de Django (y de sus paquetes complementarios) se mantenga intacta y específica para ese proyecto, evitando que una actualización global del sistema rompa nuestra aplicación.

2.Facilita compartir el proyecto con otros desarrolladores. Al aislar las dependencias, podemos generar un archivo de registro (como requirements.txt) para que cualquier otra persona replique exactamente nuestro mismo entorno de trabajo en segundos.

3.Evita saturar la instalación global de Python con decenas de paquetes que solo utilizaremos en proyectos particulares, manteniendo nuestro sistema ordenado y libre de basura digital.

• Explica en tus palabras qué hace el siguiente comando (no es necesario ejecutarlo):

python -m venv: Le indica a Python que ejecute su módulo integrado llamado venv, el cual está diseñado específicamente para la creación de entornos virtuales.

env: Es el nombre que le estamos asignando a la carpeta que contendrá todo nuestro entorno aislado (los ejecutables de Python, el gestor de paquetes pip y las librerías que instalemos más adelante). Al ejecutarlo, se creará un directorio con ese nombre en nuestra ruta actual.

3. Estructura y diseño de Django

• ¿Qué es el patrón MVC y cómo se aplica en Django (MTV)?

El patrón MVC (Modelo-Vista-Controlador) es una arquitectura de diseño de software que divide una aplicación en tres componentes principales. Su objetivo es separar la lógica interna del manejo de datos de la interfaz visual que interactúa con el usuario, logrando un código más limpio y fácil de mantener.

En Django, este principio se aplica mediante una variación terminológica conocida como MTV (Modelo-Template-Vista). Aunque los nombres de las capas cambian ligeramente respecto al MVC tradicional, el propósito de separar responsabilidades se mantiene intacto.

Completa esta tabla comparativa:

Concepto tradicional (MVC) Nombre en Django (MTV) Función

Model (Concepto tradicional MVC)
Model (Nombre en en Django MTV)
Función: Es la capa de acceso a datos. Representa la estructura de la base de datos, definiendo cómo se guarda, modifica y extrae la información.

View (Concepto tradicional MVC)
Template (Nombre en en Django MTV)
Función: Es la capa de presentación. Se encarga de definir cómo se mostrarán visualmente los datos al usuario, construyendo la interfaz (generalmente combinando HTML y etiquetas de Django).

Controller (Concepto tradicional MVC)
View (Nombre en en Django MTV)
Función: Es el cerebro lógico de la aplicación. Recibe la petición del usuario, consulta al Modelo para obtener o guardar datos, y luego le pasa esa información al Template para que sea renderizada en pantalla.

• ¿Qué es el enrutador de Django y qué papel cumple en una aplicación web?
El enrutador de Django es el sistema que intercepta y analiza cada petición web que llega a la aplicación. Cumple el rol de un director de tráfico: lee la URL solicitada por el usuario en su navegador, busca una coincidencia dentro de una lista de rutas previamente configuradas por el desarrollador y, si la encuentra, dirige esa petición hacia el view correspondiente para que esta ejecute su lógica.

4. Principios del desarrollo con Django

• ¿Qué significa el principio DRY ("Don't Repeat Yourself") y cómo lo aplica Django?

El principio DRY ("No te repitas") es una filosofía de ingeniería de software que busca reducir al máximo la duplicación de código. Su premisa es que cada pieza de lógica o estructura debe tener una representación única y autoritativa dentro del sistema. Django aplica este principio de múltiples formas: a través de la herencia de plantillas (creando un "esqueleto" base y solo reescribiendo los bloques que cambian en otras páginas), fomentando la creación de aplicaciones modulares que pueden ser reutilizadas en distintos proyectos, y mediante su ORM, que nos evita escribir la misma lógica de base de datos repetidas veces.

• ¿Qué significa que Django tenga una “estructura flexible y minimalista”?

Aunque Django es famoso por ser un framework de "baterías incluidas", su diseño interno se basa en el bajo acoplamiento. Esto significa que sus distintas capas son independientes entre sí. La flexibilidad radica en que, si bien el framework te proporciona todo lo necesario, no te obliga a usar sus herramientas de forma rígida. Puedes prescindir de su motor de plantillas, cambiar el sistema de base de datos o integrar librerías externas con total libertad. El minimalismo se refleja en su filosofía de mantener el núcleo de tu código limpio, delegando la complejidad repetitiva al framework.

• ¿Qué son los Templates en Django y qué rol cumplen en la renderización de contenido?

Los Templates son archivos de texto, comúnmente estructurados con HTML, que incluyen una sintaxis especial proporcionada por el framework (el Django template language o DTL). Su rol es actuar como la capa de presentación visual. Se encargan de la renderización, que es el proceso de recibir los datos dinámicos procesados y enviados por el view, inyectarlos de manera segura en la estructura estática del HTML, y generar el documento final que el navegador del usuario podrá interpretar y mostrar.
