#### 1. XPath to locate the main h1 element.
main_h1 = driver.find_element(By.XPATH, "//h1[@id='mainTitle']")
#### 2. XPath to select the About Us navigational link.
about_link = driver.find_element(By.XPATH, "//a[text()='About Us']")
#### 3. XPath to select the Graphic Design dropdown link.
graphic_design_link = driver.find_element(By.XPATH, "//ul[@class='dropdown']//a[text()='Graphic Design']")
#### 4. XPath to select the team member’s name Jane Smith.
jane_smith = driver.find_element(By.XPATH, "//h4[text()='Jane Smith']")
####  5. XPath to select the description (which is inside the paragraph) of SEO Services. 
seo_description = driver.find_element(By.XPATH, "//div[@class='service-item'][h3[text()='SEO Services']]/p")
#### 6. XPath expression to select all service items in the "Our Services" section.
service_items = driver.find_elements(By.XPATH, "//section[@id='services']//div[@class='service-item']")
#### 7. XPath to select the email input field in the contact form
email_input = driver.find_element(By.XPATH, "//form[@id='contactForm']//input[@type='email']")
#### 8. XPath to select the entire contact form
contact_form = driver.find_element(By.XPATH, "//form[@id='contactForm']")
#### 9. XPath to select the footer paragraph element.
footer_paragraph = driver.find_element(By.XPATH, "//footer//p")
#### 10. XPath to select the first team member's 'h4' name
first_team_member = driver.find_element(By.XPATH, "//div[@class='team']//li[1]/h4")
#### 11. Select the description of the second service item using XPath
second_service_description = driver.find_element(By.XPATH, "//div[@class='service-item'][2]/p")
#### 12. XPath to select the "Contact Us" section header ('h2' element)
contact_header = driver.find_element(By.XPATH, "//section[@id='contact']//h2")
#### 13. XPath expression to select all links within the dropdown under the "Services" navigation item
dropdown_links = driver.find_elements(By.XPATH, "//li[a[text()='Services']]//ul[@class='dropdown']//a")
#### 14. XPath to select the first 'li' under the "Our Team" section
first_team_li = driver.find_element(By.XPATH, "//div[@class='team']//ul/li[1]")
#### 15. XPath to locate the "Send Message" button in the contact form
send_message_button = driver.find_element(By.XPATH, "//form[@id='contactForm']//input[@type='submit' and @value='Send Message']")
