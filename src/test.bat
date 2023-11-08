python setup.py install --user
@REM del counter.py counter.pyc timer.py timer.pyc compositeCounter.py compositeCounter.pyc historyCounter.py historyCounter.pyc parallelCounter.py parallelCounter.pyc counterScripts.pyc counterScripts.py counterMultipleOptions.pyc counterMultipleOptions.py
del counterMultipleOptions.py counterMultipleOptions.pyc
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 counter.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 compositeCounter.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p eventloop -l python -d 1 timer.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 historyCounter.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 parallelCounter.xml
python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 counterMultipleOptions.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 counterScripts.xml