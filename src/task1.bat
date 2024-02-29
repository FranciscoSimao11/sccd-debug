python setup.py install --user

@REM TASK 1
python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 tests/trafficLights.xml
@rem del trafficLights.py trafficLights.pyc

@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 phone.xml
@REM python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 historyCounter.xml
@rem python -m python_sccd.python_sccd_compiler.sccdc -p threads -l python -d 1 tests/trafficLights.xml


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