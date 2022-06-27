#$$$$ Created by Irreverent - 6/22' $$$$#
############### Ver. 1.0 ###############

# Importing libraries.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from parsel import Selector

	# Set "IMPLICT_WAIT" to 5.
IMPLICT_WAIT = 5 
	# Create webdriver object 
options = webdriver.ChromeOptions()
	# Pass to webdriver the location of User Data.
options.add_argument(r"--user-data-dir=C:\\Users\\Zuss\\AppData\\Local\\Google\\Chrome\\User Data")
	# Pass to webdriver the location of profile directory.
options.add_argument(r'--profile-directory=C:\\Users\\Zuss\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
	# Pass to webdriver some options.
options.add_argument("--disable-infobars --disable-extensions --window-size=1366,768")
	# Set variable "driver" the "chromodriver.exe" path.
driver = webdriver.Chrome(executable_path=r'C:\\Users\\Zuss\\Desktop\\chromedriver.exe')
	# Pause 5s after any action.
driver.implicitly_wait(IMPLICT_WAIT)
	# Print a message.
print("\n Give me a GMap URL to scrap: \n")
  # Parse driver a link.
driver.get('https://www.google.gr/maps/search/Louer+un+bateau/@43.0682923,6.2460164,10z/data=!3m1!4b1!4m2!2m1!6e1?authuser=0&hl=en')
 
  # Set variable "m" the result of finding the element by the given xPath.
#m = driver.find_element(by=By.XPATH, value='//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/a')
	# Set variable "page_content" the source page of the oppened given link.
page_content = driver.page_source
	# Set variable "response" to the page content through Selector.
response = Selector(page_content)
	# Create an empty list "results".
results = []
  # For every variable in the given xPath:
for el in response.xpath('//div[contains(@aria-label, "Results for")]/div/div[./a]'):
	# Add every result with extracted Title and Link to the list.
    results.append({
    	# Extract every time the tittle from the given xPath.
    	"Title": el.xpath('./a/@aria-label').extract_first(''),
    	# Extract every time the link from the given xPath.
       	"Link": el.xpath('./a/@href').extract_first('')
    # Closur of the stracture of the list "results".
    })
  # Print messages with the results.
print('\n'.join(map(str, results)))
