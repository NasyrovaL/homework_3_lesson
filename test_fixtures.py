from selene import browser, be, have

def test_successful_search(setting_browser):
    browser.open("https://duckduckgo.com")
    browser.element('[id="searchbox_input"]').should(be.blank).type('qa guru').press_enter()
    browser.element('[class="kY2IgmnCmOGjharHErah"]').should(have.text('В онлайн-школе QA.GURU '))


def test_unsuccessful_search(setting_browser):
    browser.open("https://duckduckgo.com")
    browser.element('[id="searchbox_input"]').should(be.blank).type('dfgjhjkbldfkbjs;dfjbsdjgkbn').press_enter()
    browser.element('[class="THG_yNtlhifBrJDatoUn wZ4JdaHxSAhGy1HoNVja wN0KrcRQzChXFKiMHpCZ"]').should(have.text('По запросу «dfgjhjkbldfkbjs;dfjbsdjgkbn» ничего не найдено.'))





