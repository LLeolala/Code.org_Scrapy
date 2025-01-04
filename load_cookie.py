import pickle

def load_cookie(path, file, driver):
    # 禁用所有重定向
    driver.execute_script("""
        window.onbeforeunload = function() { return false; };
        window.onunload = function() { return false; };
        window.location.replace = function() { return false; };
        window.location.assign = function() { return false; };
        history.pushState = function() { return false; };
        history.replaceState = function() { return false; };
    """)
    
    try:
        with open(path + "/" + file, "rb") as cookiesfile:
            cookies = pickle.load(cookiesfile)
            for cookie in cookies:
                if cookie.get('domain'):
                    try:
                        if 'expiry' in cookie:
                            del cookie['expiry']
                        driver.add_cookie(cookie)
                    except Exception as e:
                        print(f"無法添加 cookie: {cookie.get('name')} - {str(e)}")
    
    except Exception as e:
        print(f"載入 cookies 失敗: {str(e)}")
    
    # 恢復正常導航功能
    driver.execute_script("""
        window.onbeforeunload = null;
        window.onunload = null;
        delete window.location.replace;
        delete window.location.assign;
        delete history.pushState;
        delete history.replaceState;
    """)