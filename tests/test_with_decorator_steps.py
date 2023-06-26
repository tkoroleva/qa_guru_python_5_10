import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

rep = 'eroshenkoam/allure-example'
issue_number = '80'


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'tkoroleva')
@allure.feature(f'Проверка наличия Issue {issue_number} на github')
@allure.story('Тест с использованием шагов с декоратором @allure.step')
@allure.link('https://github.com', name='Testing')
def test_search_github_issue():
    open_main_page()
    search_repository(rep)
    go_to_repository(rep)
    open_issues_tab()
    check_issue_with_number(issue_number)


@allure.step('Открыть главную страницу')
def open_main_page():
    browser.open("https://github.com")


@allure.step('Найти репозиторий')
def search_repository(repository):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repository)
    s(".header-search-input").submit()


@allure.step('Открыть репозиторий')
def go_to_repository(repository):
    s(by.link_text(repository)).click()


@allure.step('Открыть вкладку Issues')
def open_issues_tab():
    s('#issues-tab').click()


@allure.step(f'Проверить наличие Issue {issue_number}')
def check_issue_with_number(number):
    s(by.partial_text(number)).click()


browser.quit()
