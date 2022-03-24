<p align="center">
<a href="https://github.com/vuejs/vue">
    <img src="https://img.shields.io/badge/python-3.9.7-brightgreen.svg" alt="vue">
  </a>
  <a href="https://github.com/ElemeFE/element">
    <img src="https://img.shields.io/badge/selenium-4.1.3-brightgreen.svg" alt="element-ui">
  </a>
  <a href="https://github.com/ElemeFE/element">
    <img src="https://img.shields.io/badge/webdriver-99.0.4844.51-brightgreen.svg" alt="element-ui">
  </a>
  <a href="https://github.com/ElemeFE/element">
    <img src="https://img.shields.io/badge/platform-macOS--64-lightgrey" alt="element-ui">
  </a>
</p>


## 🎯目的：
這隻小程式是為了確保每一天都能登入商業思維學院，取得商值，努力升級成為大佬！

---

![](https://i.imgur.com/PHLFLPA.gif)

## 目錄：

#### 1. 使用說明

#### 2. 參數介紹

---

## 1. 使用說明

- 需要安裝[Python](https://www.python.org/downloads/)
- 透過Python安裝[Selenium]套件
- 需要安裝Chrome ＆ [ChromeDriver](https://chromedriver.chromium.org/)
- 這隻程式於Mac撰寫，Win請自行修改。

---

## 2. 參數介紹

```python
BusinessAutoTask.py 的 __init__中提供以下參數可自行修改

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
```

其它更多配置可參閱源碼內部註解。