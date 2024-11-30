# Code.org 和 CodeSpark 自動化註冊腳本

這個專案提供了一個自動化腳本，用於同時在 Code.org 和 CodeSpark 平台上註冊學生帳號。腳本使用 Selenium 進行網頁自動化操作。

## 功能特點

- 自動在 Code.org 註冊新學生帳號
- 自動在 CodeSpark 註冊新學生帳號
- 自動生成學生帳號名稱（結合姓名和出生年份）
- 支援批量處理

## 環境需求

- Python 3.6+
- Chrome 瀏覽器
- ChromeDriver（腳本會自動安裝）

## 必要套件

```bash
pip install selenium
pip install python-dotenv
pip install webdriver-manager
```

## 環境設置

1. 建立 `.env` 檔案在專案根目錄，包含以下內容：

```plaintext
CODE_ORG_ACCOUNT=你的 Code.org 帳號
CODE_ORG_PASSWORD=你的 Code.org 密碼
CODESPARK_CLASS_NAME=Code.org 班級名稱
CODESPARK_ACCOUNT=你的 Codespark 帳號
CODESPARK_PASSWORD=你的 Codespark 密碼
CODESPARK_CLASS_NAME=Codespark 班級名稱
```

## 檔案結構

```
├── main.py            # 主程式入口
├── input_script.py    # 處理命令列參數
├── code_org.py        # Code.org 自動化腳本
├── codespark.py       # CodeSpark 自動化腳本
├── globals.py         # 全域變數
└── .env              # 環境變數設定
```

## 使用方法

1. 確保所有必要套件都已安裝
2. 設定好 `.env` 檔案
3. 執行指令：

```bash
python main.py [學生姓名] [出生年月日] [程度]
```

例如：
```bash
python main.py JohnDoe 20150101 1
```

### 參數說明

- `學生姓名`：學生的英文名字
- `出生年月日`：8位數字的日期格式（YYYYMMDD）
- `程度`：學生程度（目前未使用，保留擴充用）

## 注意事項

1. 執行腳本前請確保：
   - 網路連線正常
   - Chrome 瀏覽器已安裝
   - 環境變數設定正確

2. 腳本執行過程中：
   - 請勿關閉自動開啟的瀏覽器視窗
   - 等待腳本完全執行完成

3. 安全性考量：
   - 請妥善保管 `.env` 檔案
   - 不要分享含有帳號密碼的設定檔

## 故障排除

如果遇到以下問題：

1. **瀏覽器無法啟動**
   - 確認 Chrome 瀏覽器已正確安裝
   - 確認網路連線正常

2. **登入失敗**
   - 檢查 `.env` 檔案中的帳號密碼是否正確
   - 確認帳號未被鎖定

3. **元素無法點擊**
   - 可能是網頁載入時間較長，請調整程式中的等待時間
   - 檢查網站是否有更新導致元素選擇器改變

## 授權

此專案為私人使用，未指定開源授權。

## 支援

如有問題，請提交 Issue 或聯繫專案維護者。