python setup.py install --user
del counter.py counter.pyc timer.py timer.pyc
python -m sccd.compiler.sccdc -p threads -l python -d 1 counter.xml
python -m sccd.compiler.sccdc -p eventloop -l python -d 1 timer.xml