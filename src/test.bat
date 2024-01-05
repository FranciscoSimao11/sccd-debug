python setup.py install --user
@REM del counter.py counter.pyc timer.py timer.pyc compositeCounter.py compositeCounter.pyc historyCounter.py historyCounter.pyc parallelCounter.py parallelCounter.pyc counterScripts.pyc counterScripts.py counterMultipleOptions.pyc counterMultipleOptions.py
@REM del counterMultipleOptions.py counterMultipleOptions.pyc
@REM del counterMultipleOptionsUsable.py counterMultipleOptionsUsable.pyc
del parallelCounter.py parallelCounter.pyc
@REM del compositeCounter.py compositeCounter.pyc
@REM del parallelCounterWithDebug.py parallelCounterWithDebug.pyc
@REM del classTest.py classTest.pyc
@REM del counterNoDebug.py counterNoDebug.pyc
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 classTest.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 0 counterNoDebug.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 compositeCounter.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p eventloop -l python -d 1 timer.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 historyCounter.xml
python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 parallelCounter.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 compositeCounter.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 parallelCounterWithDebug.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 counterMultipleOptions.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 counterMultipleOptionsUsable.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 counterScripts.xml