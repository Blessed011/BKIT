from pytest_bdd import *
from sort import sort_bdd

@scenario("C:/Users/5/PycharmProjects/Lab_5/features/behave.feature", 'sorting of list')
def testing_sort():
    pass

@given('list', target_fixture = 'given_list')
def given_list():
    return [5, -7, 13, 2, -9, 10]

@when('we sort it', target_fixture = 'sorting')
def sorting(given_list):
    return sort_bdd(given_list)

@then('we shall get sorted list')
def final_list(sorting):
    assert(sorting == [13, 10, -9, -7, 5, 2])