import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser

rep = 'tkoroleva/qa_guru_python_5_10'
issue_number = '#2'


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'tkoroleva')
@allure.feature(f'Проверка наличия Issue {issue_number} на github')
@allure.story('Тест на чистом Selene (без шагов)')
@allure.link('https://github.com', name='Testing')
def test_search_github_issue():
    browser.open('https://github.com/')
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type(rep)
    browser.element('.header-search-input').press_enter()
    browser.element(by.link_text(rep)).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text(issue_number)).should(be.visible)

