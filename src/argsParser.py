parser = argparse.ArgumentParser(prog="python -m sccd.compiler.sccdc")
parser.add_argument('-s','--simType', help='Simulation type which has 3 different variations: 0 = default simulation, scale factor of 1; 1 = scaled real-time simulation, takes one extra arg to set the scale factor; 2 = as-fast-as-possible simulation, scale factor = infinity', default=0)
parser.add_argument('-f','--factor', help='Scale factor: default value is 1; if the factor is 2, the simulation 2x faster', default=1)
args = vars(parser.parse_args())

if args['simType'] is not None:
        if args['simType'] is 0:
            print("Real-time Simulation")
            self.scaleFactor = 1
        if args['simType'] is 1:
            print("As-fast-as-possible Simulation")
            self.scaleFactor = float('inf')
        if args['simType'] is 2:
            print("Scaled Real-time Simulation")
            if args['factor'] is not None and args['factor'].isNumeric() and args['factor'] > 0:
                self.scaleFactor = args['factor']
        else:
            print("Invalid simulation type. Defaulting to Real-time Simulation")
            self.scaleFactor = 1