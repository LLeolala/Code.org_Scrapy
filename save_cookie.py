from pathlib import Path
import pickle
import logging as log

def save_cookie(path, file, chrome_driver):
    try:
        cookies = chrome_driver.get_cookies()
        # Filter out cookies without proper domain
        valid_cookies = [cookie for cookie in cookies if cookie.get('domain')]
        
        with open(path + "/" + file, "wb") as filehandler:
            pickle.dump(valid_cookies, filehandler)
    except FileNotFoundError:
        log.error("FileNotFound, Rebuild : %s", path)
        Path(path).mkdir(parents=True, exist_ok=True)
    except Exception as e:
        log.error(f"Failed to save cookies: {e}")