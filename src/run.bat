python setup.py install --user
python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 tests/counter.xml
start cmd.exe /c python runner.py -s 0 -f 2 