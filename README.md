# Code.org、CodeSpark 和 Typing.com 自動化註冊工具

這是一個強大的自動化工具，用於同時在三個教育平台（Code.org、CodeSpark 和 Typing.com）上為學生創建帳戶。通過 Selenium 實現網頁自動化操作，能大幅提升批量註冊學生帳號的效率。

## 核心功能

- 在 Code.org 自動註冊學生帳號並獲取密碼
- 在 CodeSpark 自動註冊相同學生的帳號
- 在 Typing.com 自動註冊帳號並設置與 Code.org 相同的密碼
- 智能生成使用者名稱（結合學生姓名和出生年份後四位數）
- 自動化流程，減少人工操作

## 系統要求

- Python 3.6 或更高版本
- Chrome 瀏覽器
- 穩定的網路連接
- 各平台的教師帳號

## 安裝步驟

1. 安裝必要的 Python 套件：

```bash
pip install -r requirements.txt
```

或者手動安裝：

```bash
pip install selenium python-dotenv webdriver-manager
```

2. 設定環境變數：在專案根目錄建立 `.env` 檔案，包含以下內容：

```
CODE_ORG_ACCOUNT=你的 Code.org 帳號
CODE_ORG_PASSWORD=你的 Code.org 密碼
CODE_ORG_CLASS_NAME=Code.org 班級名稱
CODESPARK_ACCOUNT=你的 CodeSpark 帳號
CODESPARK_PASSWORD=你的 CodeSpark 密碼
CODESPARK_CLASS_NAME=CodeSpark 班級名稱
TYPING_ACCOUNT=你的 Typing.com 帳號
TYPING_PASSWORD=你的 Typing.com 密碼
TYPING_CLASS_NAME=Typing.com 班級名稱
EMAIL=Email 帳號
EMAIL_PASSWORD=Email 密碼
GOOGLE_ADDRESS=Google 用戶資料目錄路徑
```

## 使用方法

運行以下命令來註冊一個學生：

```bash
python main.py [學生姓名] [出生年月日]
```

### 參數說明

- `學生姓名`：學生的英文名字，不含空格（例如：JohnDoe）
- `出生年月日`：8位數字的日期格式（YYYYMMDD，例如：20150101）

### 使用範例

```bash
python main.py JaneDoe 20160415
```

這將在三個平台上創建用戶名為 "JaneDoe0415" 的帳號。

## 工作流程

1. 首先在 Code.org 創建學生帳號並獲取生成的密碼
2. 然後在 CodeSpark 創建同名學生帳號
3. 最後在 Typing.com 創建同名帳號，並設置與 Code.org 相同的密碼
4. 整個過程在同一個瀏覽器工作階段中完成

## 技術說明

### 檔案結構

- `main.py` - 主程式入口，協調整體流程
- `code_org.py` - Code.org 平台的自動化操作模組
- `codespark.py` - CodeSpark 平台的自動化操作模組
- `typing_com.py` - Typing.com 平台的自動化操作模組
- `create_driver.py` - 設定並創建 Selenium WebDriver
- `globals.py` - 全域變數管理
- `input_script.py` - 命令列參數處理

### 關鍵技術

- 使用 Selenium 進行網頁自動化
- 使用 WebDriverWait 確保元素正確載入
- 採用 XPath 和 CSS 選擇器定位元素
- 使用 dotenv 管理敏感資訊
- 使用 Google Chrome 用戶配置文件保存登入狀態

## 故障排除

### 常見問題

1. **無法啟動瀏覽器**
   - 確認 Chrome 是否正確安裝
   - 檢查 ChromeDriver 版本是否與 Chrome 版本匹配

2. **無法登入平台**
   - 確認 `.env` 檔案中的帳號密碼是否正確
   - 檢查網路連接狀態
   - 嘗試手動登入一次，然後重新運行腳本

3. **元素定位失敗**
   - 網站可能更新了界面，需要更新選擇器
   - 增加等待時間 `WebDriverWait` 參數（目前設為 10 秒）

4. **創建帳號失敗**
   - 檢查學生名稱是否已存在
   - 確認班級名稱是否設置正確

## 注意事項

- 初次運行時，可能需要手動登入各平台（取消注釋相關代碼）
- 運行過程中請勿手動干預瀏覽器操作
- 請勿關閉自動打開的瀏覽器窗口
- 保管好 `.env` 檔案中的敏感資訊
- 每次批量處理多名學生時，建議使用腳本而非手動運行多次

## 進階使用

- 若需批量處理多名學生，可創建包含學生資訊的 CSV 檔案，並編寫讀取該檔案的腳本
- 可根據需要修改 `globals.py` 添加更多全域參數
- 可修改 `create_driver.py` 調整瀏覽器設置

## 開發與貢獻

如需進一步開發或自訂功能，可修改相應的平台模組檔案：

- `code_org.py` - 針對 Code.org 平台功能的修改
- `codespark.py` - 針對 CodeSpark 平台功能的修改
- `typing_com.py` - 針對 Typing.com 平台功能的修改

### 待開發功能

- 批量處理學生名單
- 自動化報告生成
- 錯誤處理和重試機制增強
- 界面美化和操作提示增強

## 授權信息

此專案為私人使用，版權所有。未經授權，禁止分發或商業使用。