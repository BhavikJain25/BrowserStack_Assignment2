import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

USERNAME = "bhav_KpDYax"
ACCESS_KEY = "Wg37amyxiJdqp4zkGGRS"

URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

# Capability builder for desktop browsers
def create_options(browser, os_name, os_version, session_name):
    if browser == "Chrome":
        options = webdriver.ChromeOptions()
    elif browser == "Firefox":
        options = webdriver.FirefoxOptions()
    elif browser == "Edge":
        options = webdriver.EdgeOptions()
    elif browser == "Safari":
        options = webdriver.SafariOptions()
    else:
        options = webdriver.ChromeOptions()  # fallback

    options.set_capability("browserName", browser)
    options.set_capability("bstack:options", {
        "os": os_name,
        "osVersion": os_version,
        "sessionName": session_name,
        "buildName": "MultiBrowser+Android Build"
    })
    return options

# ✅ 4 desktop + 1 mobile browser
browsers = [
    create_options("Chrome", "Windows", "11", "Windows Chrome - 11"),
    create_options("Firefox", "Windows", "10", "Windows Firefox - 10"),
    create_options("Edge", "Windows", "11", "Windows Edge - 11"),
    create_options("Safari", "OS X", "Ventura", "macOS Safari - Ventura"),

    # Android device manually added
    webdriver.ChromeOptions()
]
browsers[-1].set_capability("browserName", "Chrome")
browsers[-1].set_capability("bstack:options", {
    "deviceName": "Samsung Galaxy S22",
    "realMobile": "true",
    "osVersion": "12.0",
    "sessionName": "Android Chrome - Galaxy S22",
    "buildName": "MultiBrowser+Android Build"
})

# Worker function
def run_browserstack_test(options):
    session_name = options.capabilities['bstack:options']['sessionName']
    print(f"🚀 Starting test: {session_name}")

    driver = RemoteWebDriver(command_executor=URL, options=options)

    try:
        driver.get("https://elpais.com/opinion/")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "article a"))
        )
        print(f"[{session_name}] ✅ Loaded: {driver.title}")
    except Exception as e:
        print(f"[{session_name}] ❌ Error: {e}")
    finally:
        driver.quit()

# Launch tests in parallel
if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(run_browserstack_test, browsers)
