import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

class AmazonReviewScraper:
    def __init__(self):
        self.driver = None
        self.product_name = None

    def open_browser(self):
        
        opt = Options()
        opt.add_argument("--disable-infobars")
        opt.add_argument("--disable-extensions")
        opt.add_argument('--log-level=OFF')
        opt.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        
        opt.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

        
        service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=opt)
        self.driver.get("https://www.amazon.in/")
        time.sleep(3)

    def get_product_url(self, product_name):
        self.product_name = product_name
        formatted_product_name = self.product_name.replace(" ", "+")
        product_url = f"https://www.amazon.in/s?k={formatted_product_name}&ref=nb_sb_noss"
        print(">> Product URL: ", product_url)
        self.driver.get(product_url)
        time.sleep(3)  
        return product_url

    def extract_webpage_information(self):
        
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        page_results = soup.find_all('div', {'data-component-type': 's-search-result'})
        return page_results

    def extract_product_information(self, page_results):
        temp_record = []
        for item in page_results[:25]:  
            description = item.find('span', {'class': 'a-size-medium'})
            description = description.text.strip() if description else "N/A"

            product_price = item.find('span', {'class': 'a-price-whole'})
            product_price = product_price.text.strip() if product_price else "N/A"

            product_review = item.find('span', {'class': 'a-icon-alt'})
            product_review = product_review.text.strip() if product_review else "N/A"

            review_number = item.find('span', {'class': 'a-size-base'})
            review_number = review_number.text.strip() if review_number else "N/A"

            category_url = item.find('a', {'class': 'a-link-normal s-no-outline'})
            category_url = 'https://www.amazon.in' + category_url['href'] if category_url else "N/A"

            reviews = set()  
            if category_url != "N/A":
                try:
                    self.driver.get(category_url)
                    time.sleep(5)  
                    
                    
                    see_all_reviews = self.driver.find_elements(By.PARTIAL_LINK_TEXT, "See all reviews")
                    if see_all_reviews:
                        see_all_reviews[0].click()
                        time.sleep(5)  

                    
                    review_elements = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-hook='review']"))
                    )
                    for review_element in review_elements:
                        try:
                            review_text = review_element.find_element(By.CSS_SELECTOR, "span[data-hook='review-body']").text.strip()
                            reviews.add(review_text)  
                            if len(reviews) >= 5:  
                                break
                        except Exception as e:
                            print(f"Error extracting review: {e}")

                except Exception as e:
                    print(f"Error accessing category URL {category_url}: {e}")

            
            reviews_list = list(reviews)
            reviews_list.extend(["N/A"] * (5 - len(reviews_list)))

            temp_record.append({
                'description': description,
                'price': product_price,
                'review': product_review,
                'review_count': review_number,
                'review1': reviews_list[0],
                'review2': reviews_list[1],
                'review3': reviews_list[2],
                'review4': reviews_list[3],
                'review5': reviews_list[4]
            })

        return temp_record

    def save_to_csv(self, records, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['description', 'price', 'review', 'review_count', 'review1', 'review2', 'review3', 'review4', 'review5']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for record in records:
                writer.writerow(record)

    def run(self, product_name):
        self.open_browser()
        self.get_product_url(product_name)
        page_results = self.extract_webpage_information()
        records = self.extract_product_information(page_results)
        self.save_to_csv(records, f'{product_name}_reviews.csv')
        self.driver.quit()

if __name__ == "__main__":
    scraper = AmazonReviewScraper()
    product_name = input("Enter the product name: ")
    scraper.run(product_name)
