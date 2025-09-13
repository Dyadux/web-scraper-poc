# Web Scraper POC

A Python-based web scraper that extracts quotes from [quotes.toscrape.com](https://quotes.toscrape.com/) using Selenium WebDriver. The scraper collects quote text, authors, and tags, then generates visualizations and exports the data to CSV.

## Features

- **Automated Web Scraping**: Uses Selenium WebDriver to navigate through multiple pages
- **Visual Feedback**: Highlights scraped quotes with red borders for real-time monitoring
- **Data Export**: Saves scraped data to CSV format
- **Data Visualization**: Creates bar charts showing the most frequent authors
- **Screenshot Capture**: Takes a screenshot of the final page

## Prerequisites

- Python 3.7 or higher
- Firefox browser installed
- Geckodriver (Firefox WebDriver) in your system PATH

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd web-scraper-poc
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

3. Download and install Geckodriver:
   - Visit [Geckodriver releases](https://github.com/mozilla/geckodriver/releases)
   - Download the appropriate version for your operating system
   - Add the geckodriver executable to your system PATH

## Usage

Run the scraper:

```bash
python webscraper.py
```

The script will:

1. Open Firefox browser
2. Navigate to quotes.toscrape.com
3. Scrape quotes from all available pages
4. Highlight each quote with a red border during scraping
5. Save data to `quotes.csv`
6. Take a screenshot (`quotes_page.png`)
7. Generate and display a bar chart of top authors
8. Close the browser

## Output Files

- **`quotes.csv`**: Contains all scraped quotes with columns:
  - Quote: The quote text
  - Author: Author name
  - Tags: Comma-separated list of tags
- **`quotes_page.png`**: Screenshot of the final page
- **Bar Chart**: Displays the 10 most frequent authors

## Project Structure

```
web-scraper-poc/
├── webscraper.py      # Main scraper script
├── requirements.txt   # Python dependencies
├── README.md         # This file
├── quotes.csv        # Generated output (after running)
└── quotes_page.png   # Generated screenshot (after running)
```

## Dependencies

- **selenium** (>=4.21.0): Web browser automation
- **pandas** (>=2.2.2): Data manipulation and CSV export
- **matplotlib** (>=3.9.0): Data visualization

## How It Works

1. **Browser Setup**: Initializes Firefox WebDriver and maximizes the window
2. **Page Navigation**: Visits the target website and waits for content to load
3. **Data Extraction**:
   - Finds all quote elements using CSS selectors
   - Extracts text, author, and tags from each quote
   - Highlights each quote with visual feedback
4. **Pagination**: Automatically clicks "Next" button to scrape all pages
5. **Data Processing**: Converts collected data to pandas DataFrame
6. **Export & Visualization**: Saves to CSV and creates author frequency chart

## Customization

You can modify the scraper for different websites by:

- Changing the target URL in `driver.get()`
- Updating CSS selectors for different page structures
- Modifying data extraction logic
- Adjusting sleep times for different page load speeds

## Troubleshooting

- **Geckodriver not found**: Ensure geckodriver is installed and in your PATH
- **Browser crashes**: Try reducing sleep times or adding more robust error handling
- **Element not found**: Check if the website structure has changed and update selectors

## License

This project is for educational and proof-of-concept purposes.
