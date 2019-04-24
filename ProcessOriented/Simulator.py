from constants import *

# *************************************************
#   Simulator
# *************************************************


def main():
    from engine import scheduler, reset_simulation
    from input import initialize_simulation
    from output import output_record

    # # STEADY STATE TRANSIENT ANALYSIS
    # for e in range(110, 1201, 10):
    #     set_end_time(e)
    #     print(end_time(), end='\t')
    #
    #     for _ in range(3):
    #         output_record.set_record_time(0)
    #
    #         initialize_simulation()
    #         scheduler.start()
    #         output_record.done()
    #
    #         output_record.average(end='\t')
    #
    #         reset_simulation()
    #         output_record.reset()
    #     print()

    # SIMULATION TIME DURATION DISTRIBUTION
    output_record.set_record_time(200)
    set_end_time(10000)

    initialize_simulation()
    scheduler.start()
    output_record.done()

    output_record.show(bins=22)

if __name__ == '__main__':
    main()
