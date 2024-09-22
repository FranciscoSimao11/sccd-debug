python setup.py install --user
python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 tests/phone.xml
start cmd.exe /c python runner.py -s 2 -f 2 