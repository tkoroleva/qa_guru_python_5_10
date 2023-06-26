import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser

rep = 'eroshenkoam/allure-example'
issue_number = '80'


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'tkoroleva')
@allure.feature(f'Проверка наличия Issue {issue_number} на github')
@allure.story('Тест с использованием лямбда-шагов через with allure.step')
@allure.link('https://github.com', name='Testing')
def test_search_github_issue():
    with allure.step('Открыть главную страницу'):
        browser.open('https://github.com/')
    with allure.step('Найти репозиторий'):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').type(rep)
        browser.element('.header-search-input').press_enter()
    with allure.step('Открыть репозиторий'):
        browser.element(by.link_text(rep)).click()
    with allure.step('Открыть вкладку Issues'):
        browser.element('#issues-tab').click()
    with allure.step(f'Проверить наличие Issue {issue_number}'):
        browser.element(by.partial_text(issue_number)).should(be.visible)

    browser.quit()
