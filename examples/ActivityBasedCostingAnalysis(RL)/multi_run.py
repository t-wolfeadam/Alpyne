import os
import time
from argparse import ArgumentParser, Namespace

import numpy as np

from alpyne.outputs import UnitValue
from alpyne.sim import AnyLogicSim
from alpyne.timetracker import TimeTracker
from alpyne.utils import next_num


def run(args: Namespace) -> list:
    """
    Execute a single run of the ABCA model, printing relevant information.

    Note that there is no argument validation (i.e., it assumes all values are of the correct type/in acceptable range)
    """
    sim = AnyLogicSim("ModelExported/model.jar",
                      engine_overrides=dict(seed=next_num, stop_time=UnitValue(args.stop_time, "DAY")),
                      config_defaults=dict(sizeBufferQueues=args.queue)
                      )
    if not args.no_print:
        print(sim.schema)
    if args.no_run:
        return []

    outputs_all = []

    for _ in range(args.num_runs):
        status = sim.reset(arrivalRate=args.rate)
        if not args.no_print:
            print(status)
            print(sim._engine())

        status = sim.take_action(numResourceA=args.num_a, numResourceB=args.num_b, processDelay=args.delay,
                                 conveyorSpeed=args.speed)
        if not args.no_print:
            print(status)

        outputs = sim.outputs()
        if not args.no_print:
            print(outputs)

        outputs_all.append(outputs)

    return outputs_all


if __name__ == '__main__':
    assert os.path.exists(r"ModelExported/model.jar"), r"Missing file 'ModelExported/model.jar'. To fix, create the folder if it does not exist and export/unzip in-place."

    parser = ArgumentParser(prog="ABCA-SingleRun",
                            description="Execute multiple runs of the ABCA model, for timing purposes; uses a different seed each run")
    parser.add_argument("-n", "--num-runs", default=3, type=int,
                        help="Number of times to run the sim")
    parser.add_argument("-r", "--rate", default=1.0, type=float,
                        help="Arrival rate (per day); typical range [0.1, 2]")
    parser.add_argument("-a", "--num-a", default=10, type=int,
                        help="Number of Resource A agents; typical range [1, 20]")
    parser.add_argument("-b", "--num-b", default=10, type=int,
                        help="Number of Resource B agents; typical range [1, 20]")
    parser.add_argument("-d", "--delay", default=1.0, type=float,
                        help="Delay (seconds) of machine; typical range [1, 12]")
    parser.add_argument("-c", "--speed", default=0.001, type=float,
                        help="Speed (m/s) of conveyor; typical range [1e-6, 15]")
    parser.add_argument("-q", "--queue", default=90, type=int,
                        help="Size of auxiliary queues before each resource's seize block; typical size [1, 90]")
    parser.add_argument("-t", "--stop-time", default=180, type=float,
                        help="Stop time (days)")

    prevent_group = parser.add_mutually_exclusive_group()
    prevent_group.add_argument("--no-run", action="store_true",
                               help="Do not execute a simulation run (i.e., only print schema and quit)")
    prevent_group.add_argument("--no-print", action="store_true",
                               help="Suppress schema and other events from being printed")

    args = parser.parse_args()
    start = time.time()
    outs = run(args)
    finish = time.time()

    cpps = np.array([out['outputTotalCostPerProduct'] for out in outs])

    print(f"{args.num_runs} runs in {finish-start:.2f} secs ~= {(finish-start)/args.num_runs:.4f} secs/run")
    print(f"Outputs: {cpps.min():.4f} - {cpps.mean():.4f} - {cpps.max():.4f}")

    for key, times in TimeTracker.timers.items():
        print(f"{key}: {sum(times):.4f} | {sum(times)/len(times):.4f}")




