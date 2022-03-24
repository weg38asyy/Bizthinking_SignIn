from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BusinessAutoTask:
    def __init__(self):
        ## 可更動參數 ##
        # Chrome安裝路徑（預設Mac OS路徑）
        # 詳細查閱：https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
        self.chromePath = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        # ChromeDriver的路徑，預設在當前目錄（預設MAC OS執行檔，若為Win執行檔有.exe）
        self.chromeDriver = './chromedriver'
        # 要登入的信箱帳號
        self.account = '輸入你的信箱'
        # 要登入的信箱密碼
        self.password = '輸入你的密碼'

        ## 無需異動參數 ##
        # 宣告引擎
        self.driver = {}
        # 瀏覽器初始化設定
        self.__setOptions()
        # 商業思維學院登入頁面
        self.loginPage = 'https://learn.bizthinking.com.tw/auth/login'
        # 隨機跳轉頁面
        self.page1 = 'https://learn.bizthinking.com.tw/packages/74F95f/units/837267'
        self.page2 = 'https://learn.bizthinking.com.tw/packages/74F95f/units/b4E8fb'

    def main(self):
        try:
            # 登入
            self.__login()
            # 關閉瀏覽器＆離開
        except TimeoutException as e:
            print('頁面加載超時')

        except:
            print('發生異常錯誤')

        # 關閉瀏覽器
        self.driver.close()
        self.driver.quit()

    def __setOptions(self):
        driverOptions = webdriver.ChromeOptions()
        # 瀏覽器路徑
        driverOptions.binary_location = self.chromePath
        # 瀏覽器不載入圖片，提高網頁載入速度
        driverOptions.add_argument('blink-settings=imagesEnabled=false')
        # 隱藏瀏覽器GUI，僅用Command運行（後期使用，減少系統資源開支）
        # driverOptions.add_argument('--headless')
        # 最高權限運行
        driverOptions.add_argument('--no-sandbox')
        # 在Liunx上與--no-sandbox需要一起運行工作
        driverOptions.add_argument("--no-zygote")
        # 單線程（執行緒）運行
        driverOptions.add_argument('--single-process')
        # 指定瀏覽器的視窗大小
        driverOptions.add_argument('--window-size=1200,800')
        # 生成臨時目錄（用戶、資料、緩存）
        # driverOptions.add_argument(f"--user-data-dir={mkdtemp()}")
        # driverOptions.add_argument(f"--data-path={mkdtemp()}")
        # driverOptions.add_argument(f"--disk-cache-dir={mkdtemp()}")
        # docker原本的分享記憶體在 /dev/shm 是 64MB，會造成chorme crash，所以要改成寫入到 /tmp
        # driverOptions.add_argument('--disable-dev-shm-usage')
        # 指定Chromedriver的路徑，並將配置載入
        self.driver = webdriver.Chrome(
            self.chromeDriver, options=driverOptions)
        # 設置頁面加載過期時間
        self.driver.set_page_load_timeout(60)

    def __login(self):
        # 進入商業思維學院登入畫面
        self.driver.get(self.loginPage)
        # 設定信箱
        email = self.driver.find_element_by_name('email')
        email.send_keys(self.account)
        # 設定密碼
        password = self.driver.find_element_by_name('password')
        password.send_keys(self.password)
        # 進行登入
        login = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div/span/div[3]/div/button[2]')
        login.click()
        # 進到某一篇文章裡面
        self.driver.get(self.page1)
        self.driver.execute_script('window.scrollBy(0, 2000)')
        self.driver.get(self.page2)
        self.driver.execute_script('window.scrollBy(0, 2000)')


# 運行程式
process = BusinessAutoTask()
process.main()
