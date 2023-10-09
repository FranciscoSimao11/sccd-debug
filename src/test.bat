python setup.py install --user
del counter.py
del counter.pyc
del timer.py
del timer.pyc
python -m sccd.compiler.sccdc -p threads -l python counter.xml
python -m sccd.compiler.sccdc -p eventloop -l python timer.xml