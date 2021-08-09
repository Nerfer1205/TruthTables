# TruthTables

# Dependencias: 
Flask==2.0.1
truth-table-generator==1.1.2

# Crear entorno virtual:
virtualenv env

# Activar entorno virtual:
env\Scripts\activate.bat  (Windows)
source env/bin/activate  (GNU Linux)

# Instalar dependencias:
pip install truth-table-generator
pip install flask

# Actualiza la variable, será la App que iniciará el Servidor Web:
set FLASK_APP=app.py (Windows)
export FLASK_APP=app.py (GNU Linux)

# Actualiza la variable, se ejecutará en modo desarrollo el Servidor Web:
set FLASK_ENV=development    (Windows)
export FLASK_ENV=development (GNU Linux)

# Ejecutar el framework Flask (Windows/GNU Linux):
flask run

F. L. S. Bustamante, truth-table-generator - generating truth tables., 2019 - Available at: https://github.com/chicolucio/truth-table-generator
