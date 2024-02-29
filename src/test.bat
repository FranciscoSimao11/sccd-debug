python setup.py install --user
@REM del counter.py counter.pyc timer.py timer.pyc compositeCounter.py compositeCounter.pyc historyCounter.py historyCounter.pyc parallelCounter.py parallelCounter.pyc counterScripts.pyc counterScripts.py counterMultipleOptions.pyc counterMultipleOptions.py

@REM del counterMultipleOptions.py counterMultipleOptions.pyc

@rem del model.py model.pyc

@rem del sccd_no_ui.py sccd_no_ui.pyc

@REM del counterMultipleOptionsUsable.py counterMultipleOptionsUsable.pyc

@REM del parallelCounter.py parallelCounter.pyc

@REM del parallelCounterDiff.py parallelCounterDiff.pyc
@rem del compositeCounter.py compositeCounter.pyc
@REM del parallelCounterWithDebug.py parallelCounterWithDebug.pyc
@rem del classTest.py classTest.pyc
@REM del counterNoDebug.py counterNoDebug.pyc
@rem del train.py

@REM del phone.py phone.pyc

@REM del historyCounter.py historyCounter.pyc

del trafficLights.py trafficLights.pyc

@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 phone.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 historyCounter.xml
python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 trafficLights.xml


@rem python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 0 train.xml

@rem python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 classTest.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 0 counterNoDebug.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 compositeCounter.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p eventloop -l python -d 1 timer.xml

@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 parallelCounter.xml

@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 parallelCounterDiff.xml
@rem python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 compositeCounter.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 parallelCounterWithDebug.xml

@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 counterMultipleOptions.xml

@rem python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 model.xml

@rem python -m python_sccd.python_sccd_compiler.sccdc -p eventloop -l python -d 0 sccd_no_ui.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 0 counterMultipleOptionsUsable.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 counterScripts.xml