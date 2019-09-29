from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import os
import sys
from shutil import move
from time import sleep

# Creates a new folder to house course folders in 'destFolder' 
# Moves into coures directory and returns path to 'Courses' 
def createCourseDir(destFolder):
    os.chdir(destFolder)
    os.mkdir('Courses')
    os.chdir('Courses')

    return os.getcwd()

# Navigates the website and downloads the files
def webNavigate(id_num, password, download_dir):
    
    # Retrieves all resource links using regex 
    """
    def downloadRes(course_name, all_links):
        os.mkdir(course_name)

        # Uses regex to all resource links 
    """

    # Setting chrome options
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs',{"plugins.always_open_pdf_externally": True, "download.default_directory": download_dir})

    # Instantiation of webdriver
    driver = webdriver.Chrome(options = options)
    #driver.get("https://ourvle.mona.uwi.edu")
    driver.get("https://engvle.com/")

    # Login to OURVLE
    driver.find_element_by_name("username").send_keys(id_num)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_xpath("//input [@value='Log in']").click()

    # Navigation to course pages after login
    try: 
        driver.find_element_by_xpath("//input[@value='Cancel']").click()
    finally: 
        anchor_links = driver.find_elements_by_xpath("//div[@data-type='1']/div[@class='info']/h3[@class='coursename']/a")

        # Stores all the course folder names
        course_folder_names = []

        for href in anchor_links:
            # Switches to intial course page list 
            driver.switch_to.window(driver.window_handles[0])

            driver.execute_script(f"window.open('{href.get_attribute('href')}');")
            driver.switch_to.window(driver.window_handles[1])

            course_page_title = driver.title

            # Skips leve one course pages
            if re.search(r'Course: (COMP11((26)|(27)))', course_page_title):
                driver.close()
                continue


            # TODO Create a file for specific course page detailing the files downloaded already 

            # Downloads each resource on page j
            # downloadRes(driver.title,driver.find_element_by_name('a'))

            all_links = [(link.get_attribute('href'), link.text) for link in driver.find_elements_by_tag_name('a')]
            
            for link in all_links:
                if re.search(r'.?/mod/resource/view.?',str(link[0])) and (not re.search(r'^(Class Recording)', str(link[1]))):
                    driver.find_element_by_xpath(f'//a[@href="{link[0]}"]').click()

                    if driver.title != course_page_title:
                        driver.back()
            

            # Sleeps to ensure all files have been downloaded before moving them
            sleep(5)

            # Creating course folder
            os.mkdir(download_dir + f"{course_page_title}")
            courseFolder = download_dir + f"{course_page_title}/"

            course_folder_names.append(course_page_title)

            # Moves all resource files into course folder
            list_of_files = os.listdir(download_dir)

            for _file in list_of_files:
                if not _file in course_folder_names:
                    move(download_dir+_file, courseFolder+_file)

            driver.close()

# python downloadFile.py <id_number> <password> <DownloadDestination (file_path)>
if __name__ == "__main__":
    download_dir = createCourseDir(sys.argv[3])
    webNavigate(sys.argv[1], sys.argv[2], download_dir+"/")
