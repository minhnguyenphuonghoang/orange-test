from steps_login import *
from steps_vacancies_search import *
from pytest_bdd import scenarios

scenarios("../features/login.feature", "../features/vacancies-search.feature")
