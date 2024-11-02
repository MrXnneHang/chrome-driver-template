from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webrowser_config import Wish
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from get_smms_img import download
from util import setup_directory
from selenium.webdriver.common.action_chains import ActionChains


def upload(upload_url):

    # 使用webdriver_manager来自动管理ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # 访问目标网页
    driver.get(upload_url)

    # 获取网页内容
    content = driver.page_source
    a = input("enter to quit...")
    driver.quit()


if __name__ == "__main__":

    fps = Wish()
    driver = webdriver.Chrome(service=fps.service, options=fps.option)
    driver.get(
        "https://www.google.com/search?q=Tic+Tac+toe&oq=Tic+Tac+toe&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDILCAEQABgKGAwYgAQyBwgCEAAYgAQyBwgDEAAYgAQyBwgEEAAYgAQyBggFEEUYPDIGCAYQRRg8MgYIBxBFGDzSAQgzNDMyajBqN6gCALACAA&sourceid=chrome&ie=UTF-8"
    )
    # 初始化driver
    while True:
        sleep(3)
        try:
            # 等待网页加载完成（可选，可以根据需要使用显式等待）

            # 使用 XPath 或其他选择器找到 `<td>` 元素
            td_element = driver.find_element(
                By.XPATH, "//td[@data-col='0' and @data-row='0']"
            )

            # 创建一个 `ActionChains` 对象，用于模拟鼠标操作
            actions = ActionChains(driver)

            # 使用 `click()` 方法模拟左键点击
            actions.move_to_element(td_element).click().perform()

            print("点击操作成功！")

        except Exception as e:
            print(f"遇到错误: {e}")
