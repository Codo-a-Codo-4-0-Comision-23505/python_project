# python_project

Lo primero que tienen que hacer siempre es lo siguiente:

pip install -r requirements.txt

### Posibles escenarios que no hagan funcionar el pip install
1- python puede NO estar instalado
2- puede pasar que python este usando un alias llamado py
3- puede pasar que python este usando un alias llamado python3
4- puede pasar que python este instalado y no haya problemas

Necesitamos comprobar que el comando

py -V
Python3 -V
python -V

### El mejor camino dado los escenarios anteriores... es hacer lo siguiente

{ segun 2, 3 o 4 }  -m pip install -r requirements.txt

Por ejemplo

py -m pip install -r requirements.txt


### Si no llegara a existir pip correr el siguiente commando

{ segun 2, 3 o 4 } get-pip.py

Y repetir punto anterior

Luego para correrlo deben ejecutar

python -m flask --app hello run