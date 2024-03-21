# __main__.py
import os
import sys
import shutil
from datetime import datetime
from multiprocessing import Pool
from random import choice
from anubis import feature_file_parser, arg_parser_main, results
from anubis.parallelizer import command_builder, command_runner
from anubis.copy import art, power
import logging


def main():
    # Misc Setup -------------------------------------------------------------------------------------------------------
    start = datetime.now()
    args, args_unknown = arg_parser_main.parse_arguments()
    None if args.quiet else print(choice(art) + '\nRunning Anubis  |  powered by ' + choice(power), end='\n\n')

    # Set up output dirs and files -------------------------------------------------------------------------------------
    # create a directory that will contain results and be exported
    None if args.quiet else print(f'--- Setting Up Output\n\tSending output to <{args.output}>')

    if os.path.isdir(args.output):
        shutil.rmtree(args.output)
    os.makedirs(args.output, exist_ok=True)

    # set up logging
    logging.basicConfig(
        filename=args.log_file,
        filemode='w',
        level=logging.DEBUG,
        format='[%(asctime)s] [%(levelname)s] %(message)s',
        datefmt='%H:%M:%S'
    )
    root_logger = logging.getLogger()
    root_logger.info('Args: \n\t' + "\n\t".join(a.__repr__() for a in args._get_kwargs()))

    # Run the tests ----------------------------------------------------------------------------------------------------
    if not args.quiet:
        print('\n--- Getting Tests')
        print('\ttests: ' + ", ".join(d for d in args.features))
        print(f'\ttags: {", ".join(["@" + tag for group in args.tags for tag in group]) if args.tags else "n/a"}')

    # get all testable tests and run them
    tests_to_run = feature_file_parser.get_tests(args.features, args.tags, args.unit)
    passed, failed, total = 0, 0, 0
    None if args.quiet else print(f'\n--- {"PRETENDING TO RUN" if args.dry_run else "RUNNING"} TESTS')

    best_split = -(-len(tests_to_run) // args.processes)
    max_processes = min(best_split, args.processes)
    test_split = {i: [] for i in range(max_processes)}

    # split the tests into groups
    i = 0
    while len(tests_to_run) > 0:
        test_split[i].append(tests_to_run.pop())
        i = (i + 1) % max_processes

    command_data = [command_builder(i, args, args_unknown, tests) for i, tests in test_split.items()]

    None if args.quiet else [print(f'\t{c[0]}') for c in command_data]
    args_for_map = [(command, args.quiet) for command, _ in command_data]
    output_files = [output_file for _, output_file in command_data]

    # run the tests
    if not args.dry_run:
        with Pool(processes=max_processes) as pool:
            pool.starmap(command_runner, args_for_map)

        results.write_result_aggregate(files=output_files, aggregate_out_file=args.aggregate)
        logging.info(f'output files: {output_files}')

        # do the math to print out the results summary
        results.write_junit(args.aggregate, args.junit)
        passed, failed, total = results.get_result_values(args.aggregate)
        results.print_result_summary(args, args.D, start, datetime.now(), passed, failed)
        root_logger.info(f'passed: {passed}')
        root_logger.info(f'failed: {failed}')

    print()  # this just makes the output neater
    shutil.rmtree(args.output) if args.output.endswith('.tempoutput') else None

    # exit correctly
    if args.pass_with_no_tests or total == 0:
        print(f'𓃥 {"dry run" if args.dry_run else "no tests found"} --> this run passes by default 𓃥')
        return 0
    return 0 if passed / total >= args.pass_threshold else 1


if __name__ == '__main__':
    sys.exit(main())  # run everything
