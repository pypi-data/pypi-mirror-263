from pytest_insper.fixtures import *
__version__="0.1.4"


class DependencyLevelTests:
    def __init__(self):
        self.tests_by_level = {}
        self.passed_tests_by_level = {}
    
    def add_test(self, test, level):
        self.tests_by_level.setdefault(level, []).append(test)
    
    def add_passed_test(self, level):
        self.passed_tests_by_level.setdefault(level, 0)
        self.passed_tests_by_level[level] += 1

    def dependencies_passed(self, level):
        all_levels = sorted(self.tests_by_level.keys())
        for prev_level in all_levels:
            if prev_level >= level:
                break

            if self.passed_tests_by_level.get(prev_level, 0) < len(self.tests_by_level[prev_level]):
                return False
        return True


_dependency_level_tests = DependencyLevelTests()


def pytest_configure(config):
    """Register the "run" marker."""

    provided_by_pytest_insper = 'Provided by pytest-insper.'

    # Add dependency_level marker
    config_line = (
        'dependency_level(level): specify the dependency level '
        'of the test. ' + provided_by_pytest_insper
    )
    config.addinivalue_line('markers', config_line)

    # Add max_points marker
    config_line = (
        'max_points(max_pts): specify the maximum points awarded '
        'by this test. ' + provided_by_pytest_insper
    )
    config.addinivalue_line('markers', config_line)


def add_max_points(items):
    for item in items:
        mark = item.get_closest_marker('max_points')
        if mark:
            if len(mark.args) > 0:
                max_points = mark.args[0]
            else:
                max_points = mark.kwargs.get('max_pts', 0)
            item.max_points = max_points
        else:
            item.max_points = 1


def pytest_collection_modifyitems(session, config, items):
    add_max_points(items)

    grouped_items = {}

    for item in items:
        mark = item.get_closest_marker('dependency_level')

        if mark:
            if len(mark.args) > 0:
                level = mark.args[0]
            else:
                level = mark.kwargs.get('level', -1)
            _dependency_level_tests.add_test(item, level)
        else:
            level = None

        grouped_items.setdefault(level, []).append(item)

    items_without_level = grouped_items.pop(None, [])
    sorted_items = []
    for key in sorted(grouped_items.keys()):
        sorted_items.append(grouped_items[key])
    sorted_items.append(items_without_level)

    items[:] = [item for sublist in sorted_items for item in sublist]


@pytest.hookimpl(hookwrapper=True)
def pytest_pyfunc_call(pyfuncitem):
    # Execute test
    outcome = yield

    mark = pyfuncitem.get_closest_marker('dependency_level')
    if mark:
        if len(mark.args) > 0:
            level = mark.args[0]
        else:
            level = mark.kwargs.get('level', -1)
        try:
            res = outcome.get_result()
            if res:
                _dependency_level_tests.add_passed_test(level)
        except:
            pass
        
        if not _dependency_level_tests.dependencies_passed(level):
            try:
                pytest.fail('The test passed, but some test from a previous level failed.')
            except BaseException as e:
                outcome.force_exception(e)

    return outcome