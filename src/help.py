print(colors.fg.yellow + "HELP - Available Commands:")
print("1. " + colors.fg.orange +"pause" + colors.fg.yellow + " - Pauses the execution.")
print("2. " + colors.fg.orange +"continue" + colors.fg.yellow + " - Continues the execution if it is paused.")
print("3. " + colors.fg.orange +"step" + colors.fg.yellow + " - If there exists a time-based transition, this command will skip it.")
print("4. " + colors.fg.orange +"stop" + colors.fg.yellow + " - Stops the execution completely and saves a trace with information about the simulation.")
print("5. Possible "+ colors.fg.orange +"events"+ colors.fg.yellow + " to simulate are displayed at the arrival of each state if they are available.")
print("6. To change the "+ colors.fg.orange + "Simulation Type"  + colors.fg.yellow +" and its " + colors.fg.orange +"Scale Factor" + colors.fg.yellow + ", use the flags " + colors.fg.orange + "-s" + colors.fg.yellow + " and " + colors.fg.orange + "-f" + colors.fg.yellow + ", respectively, when executing the generated file.")
print("7. The " + colors.fg.orange +  "Simulation Type" + colors.fg.yellow + ", " + colors.fg.orange + "-s" + colors.fg.yellow + " may have the following values: " + colors.fg.orange + "0" + colors.fg.yellow + " = Real-Time Simulation; "+ colors.fg.orange + "1" + colors.fg.yellow + " = Scaled Real-Time Simulation; " + colors.fg.orange + "2" + colors.fg.yellow + " = As-fast-as-possible Simulation.")
print("8. When using the Scaled Real-Time Simulation, a "+ colors.fg.orange + "Scale Factor" + colors.fg.yellow + ", " + colors.fg.orange + "-f" + colors.fg.yellow + " may be added. Its value may be any number > 0.")
print("9. To add a " + colors.fg.orange + "breakpoint" + colors.fg.yellow + ", edit the " + colors.fg.orange + "breakpoints.xml" + colors.fg.yellow +" file directly." + colors.reset)