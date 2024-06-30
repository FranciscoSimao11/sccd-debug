python setup.py install --user
python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 tests/task5.xml
python task5runner.py -s 0 -f 1