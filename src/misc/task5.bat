python setup.py install --user

@REM TASK 5

python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 tests/task5.xml
start cmd.exe /c python task5runner.py -s 0 -f 1