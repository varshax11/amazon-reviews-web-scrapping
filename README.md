# Amazon Review Scraper

Amazon Review Scraper is a Python-based tool that enables users to collect data about products, including descriptions, prices, ratings, and customer reviews, from Amazon. As a beginner, I developed this project by combining insights, resources, and code snippets from a variety of online sources. 



## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Requirements](#requirements)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Automated Product Search**: Searches Amazon for a given product name.
- **Data Extraction**: Collects information about:
  - Product descriptions
  - Prices
  - Ratings
  - Review counts
  - Up to 5 unique customer reviews per product
- **CSV Output**: Saves the extracted data to a CSV file named after the product.

---

## Installation

1. **Clone this repository** to your local machine:
   ```bash
   git clone https://github.com/your-username/amazon-review-scraper.git
   cd amazon-review-scraper

   
2. **Install required packages using pip:**


    
    pip install -r requirements.txt

## Setup

**Step 1: Set Up ChromeDriver**
This project requires ChromeDriver to enable Selenium to control the Chrome browser. We use webdriver-manager to handle ChromeDriver installation automatically.

**Step 2: Virtual Environment (Optional but Recommended)**
Set up a virtual environment to isolate project dependencies:

```bash
python3 -m venv env
source env/bin/activate  # For Linux and macOS
env\Scripts\activate     # For Windows
```

**Step 3: Run the Script**
The project is ready to run. See Usage for instructions.

## Usage
Run the Script: Run the scraper script by entering:

```bash
python amazon_review_scraper.py
Input the Product Name: When prompted, enter the name of the product you want to scrape, for example:

mathematica
```
```bash
Enter the product name: wireless earbuds

```

## Script Actions:

-Opens Amazon's website and searches for the specified product.
-Extracts up to 25 product listings with details such as:
   Description
   Price
   Average rating
   Number of reviews
   Top 5 unique customer reviews for each product (if available).
-Saves the extracted data into a CSV file named <product_name>_reviews.csv in the project directory.
-Output: The final data is stored in a CSV file with columns:

description: Product description.
price: Price of the product.
review: Average rating.
review_count: Number of reviews.
review1 to review5: Individual reviews (up to 5).

## File Structure

The project directory contains the following files:

```bash
├── amazon_review_scraper.py     # Main scraping script
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation



```

## Requirements

Below is the list of required Python packages:

selenium==4.0.0
beautifulsoup4==4.10.0
webdriver-manager==3.5.0


## Troubleshooting

If you encounter issues with ChromeDriver, ensure that your Chrome browser is updated to the latest version compatible with the ChromeDriver version.
If the script fails to load product pages, verify your internet connection and check if Amazon is blocking automated requests.


## Contributing

Contributions are welcome! If you have suggestions for improvements or find bugs, feel free to create an issue or submit a pull request.

**Fork the repository**

Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
