python setup.py install --user
python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 tests/historyCounter.xml
start cmd.exe /c python testRunner.py -s 0 -f 1

@REM @REM del counter.py counter.pyc timer.py timer.pyc compositeCounter.py compositeCounter.pyc historyCounter.py historyCounter.pyc parallelCounter.py parallelCounter.pyc counterScripts.pyc counterScripts.py counterMultipleOptions.pyc counterMultipleOptions.py

@REM @REM del counterMultipleOptions.py counterMultipleOptions.pyc

@REM @rem del model.py model.pyc

@REM @rem del sccd_no_ui.py sccd_no_ui.pyc

@REM @REM del counterMultipleOptionsUsable.py counterMultipleOptionsUsable.pyc

@REM @REM del parallelCounter.py parallelCounter.pyc

@REM @REM del parallelCounterDiff.py parallelCounterDiff.pyc
@REM @rem del compositeCounter.py compositeCounter.pyc
@REM @REM del parallelCounterWithDebug.py parallelCounterWithDebug.pyc
@REM @rem del classTest.py classTest.pyc
@REM @REM del counterNoDebug.py counterNoDebug.pyc
@REM @rem del train.py

@REM @REM del phone.py phone.pyc

@REM @REM del historyCounter.py historyCounter.pyc

@REM del trafficLights.py trafficLights.pyc

@REM @REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 phone.xml
@REM @REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 historyCounter.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 tests/trafficLights.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 tests/trafficLights.xml

@REM @rem python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 0 train.xml

@REM @rem python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 classTest.xml
@REM @REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 0 counterNoDebug.xml
@REM @REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 compositeCounter.xml
@REM @REM python -m python_sccd.python_sccd_compiler.sccdc -p eventloop -l python -d 1 timer.xml

@REM @REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 parallelCounter.xml

@REM @REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 parallelCounterDiff.xml
@REM @rem python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 compositeCounter.xml
@REM @REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 parallelCounterWithDebug.xml

@REM @REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 counterMultipleOptions.xml

@REM @rem python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 model.xml

@REM @rem python -m python_sccd.python_sccd_compiler.sccdc -p eventloop -l python -d 0 sccd_no_ui.xml
@REM @REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 0 counterMultipleOptionsUsable.xml
@REM @REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 counterScripts.xml