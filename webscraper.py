from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import matplotlib.pyplot as plt


driver = webdriver.Firefox()  # make sure geckodriver is in PATH
driver.maximize_window()
driver.get("https://quotes.toscrape.com/")

time.sleep(2)

data = []

while True:
    quotes = driver.find_elements(By.CSS_SELECTOR, ".quote")
    for q in quotes:
        text = q.find_element(By.CSS_SELECTOR, ".text").text
        author = q.find_element(By.CSS_SELECTOR, ".author").text
        tags = [t.text for t in q.find_elements(By.CSS_SELECTOR, ".tag")]
        
        driver.execute_script(
            "arguments[0].style.border='2px solid red'; arguments[0].style.boxShadow='0 0 10px red';", 
            q
        )
        time.sleep(0.2)
        
        data.append({
            "Quote": text,
            "Author": author,
            "Tags": ", ".join(tags)
        })
    

    try:
        next_btn = driver.find_element(By.CSS_SELECTOR, ".next a")
        next_btn.click()
        time.sleep(1)
    except:
        break  # no more pages

print(f"Scraped {len(data)} quotes")


df = pd.DataFrame(data)
df.to_csv("quotes.csv", index=False)

driver.save_screenshot("quotes_page.png")


top_authors = df["Author"].value_counts().head(10)

plt.figure(figsize=(8,6))
top_authors.plot(kind="bar")
plt.title("Most Frequent Authors (Scraped via Selenium)")
plt.xlabel("Author")
plt.ylabel("Number of Quotes")
plt.tight_layout()
plt.show()


driver.quit()
