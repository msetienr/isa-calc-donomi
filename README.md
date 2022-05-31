# isa-calc-donomipagi v2

En este repositorio se realiza un diseño de aplicación basado en TDD (Test-Driven Development).

La aplicación será una calculado sencilla con operaciónes básicas, a lo que seguirán una prueba de tests.

---

Ya que el lenguaje de desarrollo es **Python**, el framework con el que se realizarán los cambios es la librería **unittest**. Para descarlo se debe ejecutar el siguiente comando:

> pip install pytest

Dentro de las carpeta tests se encuentran carpetas separadas para cada una de las pruebas con su correspondiente archivo.

Para ejecutar las pruebas dentro de los tests hay que ejecutar el siguiente comando:

> python3 -m pytest tests

La estructura de archivos es la siguiente:

    __init__.py
    calc.py //Clase unirCalculator con las operaciones
    ├── tests
        ├── test_suma
            ├── __init__.py    
            ├── test_sum.py
        ├── test_multiplication
            ├── __init__.py    
            ├── test_multiply.py
        ├── test_division
            ├── __init__.py    
            ├── test_divide.py
        ├── test_raizcuadrada
            ├── __init__.py    
            ├── test_square_root.py
        ├── test_exponencial
            ├── __init__.py    
            ├── test_exp_e.py