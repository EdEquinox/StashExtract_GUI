import csv
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import psutil
            
def extract_list(url, path):
    
    
    if not url.startswith("https://stash.games/users/"):
        print("Invalid URL. Please enter a valid URL. (URL must start with 'https://stash.games/users/')")
        return 0
    
    options = Options()
    options.add_argument("--headless")  # Ensure GUI is off
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    if 'collections' in url:
        print("Collections")        
        # Create a new instance of the Chrome driver
        driver = webdriver.Chrome(options=options)
        
        try:

            # Go to the URL
            driver.get(str(url))

            # Wait for the page to load
            time.sleep(5)

            print("Page loaded successfully.5")
            
            # Get the initial page height
            last_height = driver.execute_script("return document.body.scrollHeight")

            while True:
                # Scroll down to the bottom of the page
                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

                # Wait for new content to load
                time.sleep(2)

                # Calculate new scroll height and compare with the last scroll height
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
                
             # Get the HTML of the webpage
            html_content = driver.page_source
            
            # Parse the HTML content of the page with BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Find all the divs containing the data
            divs = soup.find_all('div', class_='games-list__item')
            
            # Open the CSV file
            # Create the 'out' folder if it doesn't exist
            if not os.path.exists('out'):
                os.makedirs('out')
            
            # Open the CSV file
            with open(path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Title", "Image URL", "Category"])
                
                for div in divs:
                    # Find the image and get its source
                    img = div.find('img', class_='games-list__item-image')
                    img_src = img['data-src'] if img else None

                    # Find the span with the title and get its text
                    title_span = div.find('span', class_='games-list__item-name')
                    title = title_span.text if title_span else None
                    writer.writerow([title, img_src, "Collection"])
            print("CSV file created successfully.5")
        except WebDriverException as e:
            print("WebDriverException occurred5.")
            print(e)
        finally:
            if driver is not None:
                driver.quit()
    else:

        # Create a new instance of the Chrome driver
        driver = webdriver.Chrome(options=options)
        
        try:
            # Go to the URL
            driver.get(str(url))

            # Wait for the page to load
            time.sleep(5)

            print("Page loaded successfully.")
            
            # Get the initial page height
            last_height = driver.execute_script("return document.body.scrollHeight")

            while True:
                # Scroll down to the bottom of the page
                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

                # Wait for new content to load
                time.sleep(2)

                # Calculate new scroll height and compare with the last scroll height
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
                
            # Get the HTML of the webpage
            html_content = driver.page_source
            
            # Parse the HTML content of the page with BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Find all the divs containing the data
            divs_all = soup.find('div', {'class': 'tab-panel'})
            divs = divs_all.find_all('div', class_='games-list__item')
            
            # Open the CSV file
            # Create the 'out' folder if it doesn't exist
            if not os.path.exists('out'):
                os.makedirs('out')
            
            # Open the CSV file
            with open(path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Title", "Image URL", "Category"])
                
                for div in divs:
                    # Find the image and get its source
                    img = div.find('img', class_='games-list__item-image')
                    img_src = img['data-src'] if img else None

                    # Find the span with the title and get its text
                    title_span = div.find('span', class_='games-list__item-name')
                    title = title_span.text if title_span else None
                    writer.writerow([title, img_src, "Want"])        
            
            print("CSV file created successfully.")
        except WebDriverException:
            print("WebDriverException occurred.")
        finally:
            if driver is not None:
                driver.quit()
                
        # Create a new instance of the Chrome driver
        driver = webdriver.Chrome(options=options)
        
        try:
            # Go to the URL
            driver.get(str(url))

            # Wait for the page to load
            time.sleep(5)

            print("Page loaded successfully.2")

            # Find the buttons to click
            playing_btn = driver.find_element(By.XPATH, "//*[@id=\"playing-tab\"]")
            
            playing_btn.click()
            
            # Click the button using JavaScript
            #driver.execute_script("playing_btn[0].click();", playing_btn)
            time.sleep(2)
            
            # Get the initial page height
            last_height = driver.execute_script("return document.body.scrollHeight")

            while True:
                # Scroll down to the bottom of the page
                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

                # Wait for new content to load
                time.sleep(2)

                # Calculate new scroll height and compare with the last scroll height
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
                
            # Get the HTML of the webpage
            html_content = driver.page_source
            
            # Parse the HTML content of the page with BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')
            
            
            # Find all the divs containing the data
            divs_all = soup.find_all('div', {'class': 'tab-panel'})
            div = divs_all[1]
            
            divs = div.find_all('div', class_='games-list__item')
            
            
            # Open the CSV file
            # Create the 'out' folder if it doesn't exist
            if not os.path.exists('out'):
                os.makedirs('out')
            
            # Open the CSV file
            with open(path, 'a', newline='') as file:
                writer = csv.writer(file)
                #writer.writerow(["Title", "Image URL", "Category"])
                
                for div in divs:
                    # Find the image and get its source
                    img = div.find('img', class_='games-list__item-image')
                    img_src = img['data-src'] if img else None

                    # Find the span with the title and get its text
                    title_span = div.find('span', class_='games-list__item-name')
                    title = title_span.text if title_span else None
                    writer.writerow([title, img_src, "Playing"])
                    
            print("CSV file created successfully.2")
        except WebDriverException as e:
            print("WebDriverException occurred2.")
            print(e)
        finally:
            if driver is not None:
                driver.quit()
                
        # Create a new instance of the Chrome driver
        driver = webdriver.Chrome(options=options)
        
        try:
            # Go to the URL
            driver.get(str(url))

            # Wait for the page to load
            time.sleep(5)

            print("Page loaded successfully.3")

            # Find the buttons to click
            beaten_btn = driver.find_element(By.XPATH, "//*[@id=\"profileTab\"]/li[3]")
            beaten_btn.click()
            # Click the button using JavaScript
            #driver.execute_script("beaten_btn[0].click();", beaten_btn)
            time.sleep(2)
            
            # Get the initial page height
            last_height = driver.execute_script("return document.body.scrollHeight")

            while True:
                # Scroll down to the bottom of the page
                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

                # Wait for new content to load
                time.sleep(2)

                # Calculate new scroll height and compare with the last scroll height
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
                
            # Get the HTML of the webpage
            html_content = driver.page_source
            
            # Parse the HTML content of the page with BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Find all the divs containing the data
            divs_all = soup.find_all('div', {'class': 'tab-panel'})
            div = divs_all[3]
            divs = div.find_all('div', class_='games-list__item')
            
            # Open the CSV file
            # Create the 'out' folder if it doesn't exist
            if not os.path.exists('out'):
                os.makedirs('out')
            
            # Open the CSV file
            with open(path, 'a', newline='') as file:
                writer = csv.writer(file)
                #writer.writerow(["Title", "Image URL", "Category"])
                
                for div in divs:
                    # Find the image and get its source
                    img = div.find('img', class_='games-list__item-image')
                    img_src = img['data-src'] if img else None

                    # Find the span with the title and get its text
                    title_span = div.find('span', class_='games-list__item-name')
                    title = title_span.text if title_span else None
                    writer.writerow([title, img_src, "Beaten"])
                    
            print("CSV file created successfully.3")
        except WebDriverException as e:
            print("WebDriverException occurred3.")
            print(e)
        finally:
            if driver is not None:
                driver.quit()
                
        # Create a new instance of the Chrome driver
        driver = webdriver.Chrome(options=options)
        
        try:
            # Go to the URL
            driver.get(str(url))

            # Wait for the page to load
            time.sleep(5)

            print("Page loaded successfully.4")

            # Find the buttons to click
            archived_btn = driver.find_element(By.XPATH, "//*[@id=\"profileTab\"]/li[4]")
            archived_btn.click()
            # Click the button using JavaScript
            #driver.execute_script("playing_btn[0].click();", archived_btn)
            time.sleep(2)
            
            # Get the initial page height
            last_height = driver.execute_script("return document.body.scrollHeight")

            while True:
                # Scroll down to the bottom of the page
                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

                # Wait for new content to load
                time.sleep(2)

                # Calculate new scroll height and compare with the last scroll height
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
                
            # Get the HTML of the webpage
            html_content = driver.page_source
            
            # Parse the HTML content of the page with BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Find all the divs containing the data
            divs_all = soup.find_all('div', {'class': 'tab-panel'})
            div = divs_all[4]
            divs = div.find_all('div', class_='games-list__item')
            
            # Open the CSV file
            # Create the 'out' folder if it doesn't exist
            if not os.path.exists('out'):
                os.makedirs('out')
            
            # Open the CSV file
            with open(path, 'a', newline='') as file:
                writer = csv.writer(file)
                #writer.writerow(["Title", "Image URL", "Category"])
                
                for div in divs:
                    # Find the image and get its source
                    img = div.find('img', class_='games-list__item-image')
                    img_src = img['data-src'] if img else None

                    # Find the span with the title and get its text
                    title_span = div.find('span', class_='games-list__item-name')
                    title = title_span.text if title_span else None
                    writer.writerow([title, img_src, "Archived"])
                    
            print("CSV file created successfully.4")
        except WebDriverException as e:
            print("WebDriverException occurred4.")
            print(e)
        finally:
            if driver is not None:
                driver.quit()
            
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if proc.name() == "chrome.exe":
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        
    
    return 1