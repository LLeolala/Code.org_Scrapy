import subprocess
import os

def run_input_script():
    subprocess.run(["python", "input.py"])
def run_web():
    subprocess.run(["python", "webdriver_test.py"], check=True)
def run_spider():
    os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'leo_web.settings')
    from scrapy.crawler import CrawlerProcess
    from scrapy.utils.project import get_project_settings
    from leo_web.spiders.leo_spider import LeoSpider  # 更新这行

    process = CrawlerProcess(get_project_settings())
    process.crawl(LeoSpider)  # 更新这行
    process.start()

if __name__ == "__main__":
    run_input_script()
    run_web()
    