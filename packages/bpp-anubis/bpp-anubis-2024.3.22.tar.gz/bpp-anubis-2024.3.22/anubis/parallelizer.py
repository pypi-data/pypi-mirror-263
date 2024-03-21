from os.path import join
from subprocess import call, STDOUT, DEVNULL
from typing import NoReturn


def command_builder(*data) -> (str, str):
    # set up vars
    p_index, args, args_unknown, tests = data
    args.unit = 'scenario' if args.unit not in ['feature', 'example', 'scenario'] else args.unit
    feature_files = set(thing.location.filename.split(':')[0] for thing in tests)

    # get arguments and construct the behave command
    user_defs = ' '.join('-D "{}"'.format(arg) for arg in args.D if arg) if args.D else ''
    tags = ' '.join('--tags "{}"'.format(','.join(t for t in g)) for g in args.tags)
    stage = f'--stage="{args.stage}"' if args.stage else ''
    output = f'-f json -o "{(results_json_file := join(args.output, str(p_index) + ".json"))}"'

    command = f'behave {stage} -D "parallel={p_index}" {user_defs} {tags} {output} {" ".join(args_unknown)} '
    command += ' '.join(feature_files) if args.unit == 'feature' else ' '.join(test.location.filename for test in tests)
    return command, results_json_file


def command_runner(*data) -> NoReturn:
    command, is_quiet = data
    call(command, shell=True, stdout=DEVNULL, stderr=STDOUT) if is_quiet else call(command, shell=True)


def context_builder_for_behave():
    pass


def run_with_behave_runner():
    pass
