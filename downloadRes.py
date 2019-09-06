from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import os
import sys
from shutil import move

# Creates a new folder to house course folders in 'destFolder' 
# Moves into coures directory and returns path to 'Courses' 
def createCourseDir(destFolder):
    os.chdir(destFolder)
    os.mkdir('Courses')
    os.chdir('Courses')

    return os.getcwd()

# Navigates the website and downloads the files
def webNavigate(id_num, password, download_dir):
    def downloadRes():
        pass

    options = webdriver.ChromeOptions()
    download_folder = "/home/dominic/Downloads"

    profile = {"plugins.always_open_pdf_externally": True, "download.default_directory": download_folder}

    options.add_experimental_option('prefs', profile)

    driver = webdriver.Chrome(options = options)
    driver.get("https://ourvle.mona.uwi.edu")

    driver.find_element_by_name("username").send_keys("620118591")
    driver.find_element_by_name("password").send_keys("QJuWIwQ4")
    driver.find_element_by_xpath("//button[@class='btn']").click()

    try: 
        driver.find_element_by_xpath("//input[@value='Cancel']").click()
    finally: 
        href_even = driver.find_elements_by_xpath("//div[@data-type='1']/div[@class='info']/h3[@class='coursename']/a")

        """
        for href in href_even:
            driver.execute_script(f"window.open('{href.get_attribute('href')}');")
        """
        driver.execute_script(f"window.open('{href_even[1].get_attribute('href')}');")
        driver.switch_to.window(driver.window_handles[1])


        driver.find_element_by_xpath("//a[@href='https://ourvle.mona.uwi.edu/mod/resource/view.php?id=218809']").click()
    

# python downloadFile.py <id_number> <password> <DownloadDestination (file_path)>
if __name__ == "__main__":
    download_dir = createCourseDir(sys.argv[3])
    webNavigate(sys.argv[1], sys.argv[2], download_dir)
