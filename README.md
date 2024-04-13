#Web50 – Project 1 - 2024
> El proyecto actual es una aplicación web de enciclopedia construida con Django. En el archivo views.py de la aplicación encyclopedia, tenemos varias vistas que manejan diferentes aspectos de la funcionalidad de la enciclopedia a implementar.
Las vistas incluyen:
-	index: Muestra la página principal con una lista de todas las entradas de la enciclopedia.
-	entrada: Muestra una entrada específica de la enciclopedia.
-	buscar: Maneja la funcionalidad de búsqueda, permitiendo a los usuarios buscar entradas en la enciclopedia.
-	nueva_entrada: Permite a los usuarios crear nuevas entradas.
-	editar: Permite a los usuarios editar entradas existentes.
-	eliminar: Un método adicional que permite a los usuarios eliminar entradas existentes.
-	md_to_html: Es una función que convierte texto en formato Markdown a HTML.

> Las plantillas **HTML* correspondientes a estas vistas se encuentran en el directorio de plantillas de la aplicación encyclopedia. Estas plantillas utilizan el lenguaje de plantillas de Django para generar HTML dinámico basado en el contexto proporcionado por las vistas.
>
> El método **eliminar** es una adición extra a la funcionalidades básica de nuestra enciclopedia. Este método permite a los usuarios eliminar entradas existentes de la enciclopedia. Cuando un usuario solicita eliminar una entrada, la vista eliminar elimina la entrada de la base de datos y redirige al usuario a la página principal.
