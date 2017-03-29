--- 
title_meta  : Chapter 1
title       : Introducción
description : "En este ejercicio conocerás los conceptos básicos de programación en python. Además conocerás la herramienta con la que impartiremos en linea los materiales del curso."
attachments:
  slides_link: http://link.to.slides/

--- type:NormalExercise xp:100 skills:1 key:15d729634a
## Como funciona

En el editor de la derecha deberás ver el código a resolver. Cuando presionas el botón "Submit" cada linea del código se evalua por el compilador de python, si obtienes un mensaje de error no se considera completa la actividad. La salida del código se muestra en la consola de la derecha.

Para los comentarios `#`se utiliza al inicio de las lineas de python, te recomiendo que escribas el menor código posible para que tu navegador no se vea ralentizado.

De igual manera que ipython en la consola puedes probar algunos comandos relacionados con la actividad.


*** =instructions
- En el editor de la derecha aparece la función calcular que reciba como argumento un entero, reescribe la función para que reciba una lista de valores.
- Agrega , and hit the 'Submit Answer' button.

*** =hint
Agrega un ciclo `for` para iterar sobre los elementos de la lista

*** =pre_exercise_code

```{python}
# no pec
```

*** =sample_code
```{python}
# Create x


# Print x

```

*** =solution
```{python}
# Create x
x = 5

# Print x
print(x)
```

*** =sct
```{python}
test_object('x')
test_output_contains('5')
success_msg('Great job!')
```