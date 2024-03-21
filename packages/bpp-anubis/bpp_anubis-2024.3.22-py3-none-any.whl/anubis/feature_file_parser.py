import os
from behave.model import Feature as BehaveFeature, Scenario, ScenarioOutline
from behave.model_core import FileLocation
from behave.tag_expression import TagExpression
from glob import glob
from pathlib import Path


def get_tests(paths, tags, unit) -> list[BehaveFeature]:
    parsed_gherkin = parse_with_behave_parser(paths)
    return get_testable_tests_with_behave(parsed_gherkin, tags, unit)


def parse_with_behave_parser(paths: list) -> list[BehaveFeature]:
    from behave.parser import parse_feature, parse_tags, parse_file
    parsed_gherkin = []

    # get all paths to the feature files and take care of duplicates
    all_paths = []
    for path in paths:
        if os.path.isfile(path):
            all_paths.append(path)
        else:
            all_paths.extend(glob(f'{path}/**/*.feature', recursive=True))

    all_paths = list(set([Path(str(Path(path).absolute())) for path in all_paths]))

    # parse the feature files, remove None cases
    for path in all_paths:
        parsed_gherkin.append(parse_file(path))

    return [gherkin for gherkin in parsed_gherkin if gherkin]


def get_testable_tests_with_behave(gherkin: list[BehaveFeature], tags: list[list[str]], unit) -> list[BehaveFeature]:
    # flatten the list of tags
    tags = [tag for group in tags for tag in group]

    all_testable_items = []
    expression = TagExpression(tags)
    if unit.lower() == 'feature':
        all_testable_items.extend([feature for feature in gherkin if is_testable_based_on_tags(feature.tags, expression)])
    elif unit.lower() == 'scenario':
        all_testable_items.extend([scenario for feature in gherkin for scenario in feature if is_testable_based_on_tags(scenario.effective_tags, expression)])
    else:  # unit == 'example'
        for feature in gherkin:
            for scenario in feature:
                is_testable = is_testable_based_on_tags(scenario.effective_tags, expression)
                if isinstance(scenario, ScenarioOutline) and is_testable:
                    for example in scenario.examples:
                        for row in example.table.rows:
                            setattr(row, 'location', FileLocation(f'{example.filename}', row.line))
                    all_testable_items.extend(row for ex in scenario.examples for row in ex.table.rows)
                elif isinstance(scenario, Scenario) and is_testable:
                    all_testable_items.append(scenario)

    [setattr(item, 'location', FileLocation(os.path.join(os.getcwd(), f'{item.location}'), item.line)) for item in all_testable_items]
    return all_testable_items


def is_testable_based_on_tags(tags: list, tag_expression: TagExpression) -> bool:
    # if there are no tags or no tag expression, the test is testable
    if not tag_expression:
        return True
    if not tags:
        return False

    booleans = []
    for and_group in tag_expression.ands:
        group_booleans = []
        for tag in and_group:
            if tag.startswith('-') or tag.startswith('not '):
                group_booleans.append(tag not in tags)
            else:
                group_booleans.append(tag in tags)
        booleans.append(all(group_booleans))
    return all(booleans)
