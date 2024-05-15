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

def extract_list(url, path):
    
    if not url.startswith("https://musicboard.app/"):
        print("Invalid URL. Please enter a valid URL.")
        return 0
    
    # Set up Chrome options

    options = Options()
    options.add_argument("--headless")  # Ensure GUI is off
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)

    try:
        
        # Go to the URL
        driver.get(str(url))

        # Wait for the page to load
        time.sleep(5)

        print("Page loaded successfully.")

        # Use a while loop to keep clicking the button as long as it exists
        while True:
            try:
                # Find the "View More" div by xPath
                element = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div[7]/div")
                
                # Click the "View More" button using JavaScript
                driver.execute_script("arguments[0].click();", element)
                time.sleep(2)

            except Exception as e:
                # If the "View More" button can't be found, break the loop
                break

        # Get the HTML of the webpage
        html_content = driver.page_source
        driver.quit()

        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all the divs containing the data
        divs = soup.find_all('div', {'class': 'content-options-wrapper'})

        # Open the CSV file
        # Create the 'out' folder if it doesn't exist
        if not os.path.exists('out'):
            os.makedirs('out')

        # Open the CSV file
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Artist", "Image URL"])
            
        # Loop through the divs and extract the data
            for div in divs:
                title = div.find('h6', {'class': 'bigbackenditem_title__bSh2l'}).text
                artist = div.find('a', {'class': 'bigbackenditem_artistLink__2-oCg'}).text
                img_url = div.find('img', {'class': 'albumcover_cover__1egXq'})['src']

                # Write the data to the CSV file
                writer.writerow([title, artist, img_url])

        print("CSV file created successfully.")
        
        return 1

    except WebDriverException:
        print("WebDriverException occurred.")
    finally:
        if driver is not None:
            driver.quit()           
            
def extract_list_later(url, path):
    
    if not url.startswith("https://musicboard.app/"):
        print("Invalid URL. Please enter a valid URL.")
        return 0
    
    # Set up Chrome options
    options = Options()
    options.add_argument("--headless")  # Ensure GUI is off
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

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

        # Use a while loop to keep clicking the button as long as it exists
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
        driver.quit()

        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all the divs containing the data
        divs = soup.find_all('div', {'class': 'content-options-wrapper'})

        # Open the CSV file
        # Create the 'out' folder if it doesn't exist
        if not os.path.exists('out'):
            os.makedirs('out')
        
        # Open the CSV file
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Artist", "Image URL"])
            
        # Loop through the divs and extract the data
            for div in divs:
                title = div.find('h6', {'class': 'bigbackenditem_title__bSh2l'}).text
                artist = div.find('a', {'class': 'bigbackenditem_artistLink__2-oCg'}).text
                img_url = div.find('img', {'class': 'albumcover_cover__1egXq'})['src']

                # Write the data to the CSV file
                writer.writerow([title, artist, img_url])

       
        print("CSV file created successfully.")
        
        driver.quit()
        
        return 1

    except WebDriverException:
        print("WebDriverException occurred.")
    finally:
        if driver is not None:
            driver.quit()
            
def extract_list_album(url, path):
    
    if not url.startswith("https://musicboard.app/"):
        print("Invalid URL. Please enter a valid URL.")
        return 0
    
    options = Options()
    options.add_argument("--headless")  # Ensure GUI is off
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

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
        driver.quit()
        
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find all the divs containing the data
        divs = soup.find_all('div', {'class': 'content-options-wrapper'})
        
        # Open the CSV file
        # Create the 'out' folder if it doesn't exist
        if not os.path.exists('out'):
            os.makedirs('out')
        
        # Open the CSV file
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Rate", "Image URL"])
        
            # Loop through the divs and extract the data
            for div in divs:
                
                title = div.find('h6', {'class': 'bigbackenditem_title__bSh2l'}).text
                img_url = div.find('img', {'class': 'albumcover_cover__1egXq'})['src']
                
                halfstar_divs = div.find_all('div', {'style': 'width: 7px; overflow: hidden; opacity: 1; height: 14px; z-index: 1;'})
                rate = 0
                for halfstar_div in halfstar_divs:
                    rate += 0.5
                
                writer.writerow([title, rate, img_url])

        
        
        print("CSV file created successfully.")

        
        return 1

    except WebDriverException:
        print("WebDriverException occurred.")
    finally:
        if driver is not None:
            driver.quit()
            
def extract_list_reviews(url, path):
    
    if not url.startswith("https://musicboard.app/"):
        print("Invalid URL. Please enter a valid URL.")
        return 0
    
    options = Options()
    options.add_argument("--headless")  # Ensure GUI is off
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

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
            time.sleep(4)

            # Calculate new scroll height and compare with the last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            
         # Get the HTML of the webpage
        html_content = driver.page_source
        driver.quit()
        
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find all the divs containing the data
        divs = soup.find_all('div', {'class': 'link-inner'})
      
        # Open the CSV file
        # Create the 'out' folder if it doesn't exist
        if not os.path.exists('out'):
            os.makedirs('out')
        
        # Open the CSV file
        with open(path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Target", "Artist", "Type", "Title" ,"Review"])
        
            # Loop through the divs and extract the data
            for div in divs:
                title = None
                review = None
                
                title = div.find('h5', {'class': 'textColor', 'style': 'margin-top: 14px;'}).get_text() if div.find('h5', {'class': 'textColor', 'style': 'margin-top: 14px;'}) else None
                target = div.find('h5', {'class': 'reviewitem_a__iuJDD'}).get_text() if div.find('h5', {'class': 'reviewitem_a__iuJDD'}) else None
                artist = div.find('a', {'class': 'reviewitem_artistLink__28F-G'}).get_text() if div.find('a', {'class': 'reviewitem_artistLink__28F-G'}) else None
                type = div.find('p', {'class': 'highDarkGrey'}).get_text() if div.find('p', {'class': 'highDarkGrey'}) else None
                
                review_container = div.find('div', {'class': 'truncate_container__3Xl3S'})
                if review_container is not None:  # Check if 'truncate_container' div is found
                    review = review_container.find('p').get_text()
                
                        
                halfstar_divs = div.find_all('div', {'style': 'width: 10px; overflow: hidden; opacity: 1; height: 20px; z-index: 1;'})
                rate = 0
                for halfstar_div in halfstar_divs:
                    rate += 0.5
                
                writer.writerow([target, artist, type, title, review, rate])

        print("CSV file created successfully.")
        
        return 1

    except WebDriverException:
        print("WebDriverException occurred.")
    finally:
        if driver is not None:
            driver.quit()
