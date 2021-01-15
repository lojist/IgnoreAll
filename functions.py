import time

def login(username, password, browser):
    # go to site
    browser.get('https://incels.co')

    # log in
    browser.find_element_by_xpath("//span[text()='Log in']/..").click()
    time.sleep(2)
    loginInput = browser.find_element_by_name('login')
    passwordInput = browser.find_element_by_name('password')

    loginInput.send_keys(username)
    passwordInput.send_keys(password)
    browser.find_element_by_css_selector(
        'button[class="button--primary button button--icon button--icon--login"]').click()

def ignoreUsers(browser, start=1, end=32500):
    for i in range(start, end):
        browser.get(f'https://incels.co/members/{i}')
        time.sleep(1)
        if (
                browser.current_url != 'https://incels.co/members/sergeantincel.1/' and browser.current_url != 'https://incels.co/members/mental_out.19/' and
                browser.current_url != 'https://incels.co/members/knajjd.63/' and browser.current_url != 'https://incels.co/members/i_a_m_i.148/' and
                browser.current_url != 'https://incels.co/members/master.162/' and browser.current_url != 'https://incels.co/members/cocksucker.4991/' and
                browser.current_url != 'https://incels.co/members/goffsystemqb.23944/' and browser.current_url != f'https://incels.co/members/{i}'):

            ignore_button = browser.find_element_by_xpath(
                "//div[contains(@class, 'memberHeader-buttons')]/div/a[contains(@data-sk-ignore, 'Ignore')]")

            if (ignore_button.get_attribute('textContent') == '\nIgnore\n'):
                ignore_button.click()

