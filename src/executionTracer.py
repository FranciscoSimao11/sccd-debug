currDir = os.getcwd()
for entry in os.listdir(currDir):
    if os.path.isfile(os.path.join(currDir, entry)) and entry == outputName:
        outputName = outputName + "_1"

simTime = "Total Simulation Time: " + str(float(self.getSimulatedTime())) + " ms (includes Debug Time)"
exTime = "Execution Time: " + str(self.executionTime) + " ms"
debugTime = "Total Debug Time: " + str(self.cumulativeDebugTime) + " ms"

f = FileWriter(outputName)
f.write("Execution Info")
f.write("")
f.write(simTime)
f.write(exTime)
f.write(debugTime)
f.write("")
f.write("Events")
for ide, event in enumerate(self.tracedEvents):
    eventName = event.getEventName()
    timestamp = event.getTimestamp()
    attributeValues = ""
    for v in event.getAttributeValues():
        attributeValues += v[0] + ": " + str(v[1]) + "; "
    eventInfo = str(ide) + ". Timestamp: " + str(timestamp) +  "; Name: " + eventName + ";  Attributes: ["  + attributeValues + "]"
    print(ide)
    print(eventName)
    f.write(eventInfo)
f.close() 