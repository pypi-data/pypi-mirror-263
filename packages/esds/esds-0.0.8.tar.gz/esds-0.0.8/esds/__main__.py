import sys, argparse, os
from .platform import YAMLPlatformFile
from .debug import *
from esds import __version__

def run(platform):
    simulation=YAMLPlatformFile(platform)
    # Allow importlib (in simulator.run()) to import file from the platform.yaml directory
    sys.path.insert(0, simulation.location)
    simulation.run()

def debug(args):
    debug_infos(args.file)

def main():
    ##### Main parser
    parser = argparse.ArgumentParser(
        description='ESDS simulator command line interface. Run simulations and perform various simulation tasks.',
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--version", help="Show esds version", action="store_true")
    subparsers = parser.add_subparsers(dest="command", help='Execute the specified command')

    ##### Run subparser
    run_parser=subparsers.add_parser("run", description='Run a simulation')
    run_parser=run_parser.add_argument("platform", help="Platform file")

    ##### Debug subparser
    debug_parser=subparsers.add_parser("debug", description='Analyze debug files')
    debug_parser=debug_parser.add_argument("file", help="Debug file to analyze")

    ##### Execute commands
    args = parser.parse_args()
    if args.command:
        if args.command == "run":
            run(args.platform)
        elif args.command == "debug":
            debug(args)
    elif args.version:
        print("ESDS v"+__version__)
    else:
        parser.print_help()
