1. main_h1 = driver.find_element(By.XPATH, "//h1[@id='mainTitle']")

2. about_link = driver.find_element(By.XPATH, "//a[text()='About Us']")

3. graphic_design_link = driver.find_element(By.XPATH, "//ul[@class='dropdown']//a[text()='Graphic Design']")

4. jane_smith = driver.find_element(By.XPATH, "//h4[text()='Jane Smith']")

5. seo_description = driver.find_element(By.XPATH, "//div[@class='service-item'][h3[text()='SEO Services']]/p")

6. service_items = driver.find_elements(By.XPATH, "//section[@id='services']//div[@class='service-item']")

7. email_input = driver.find_element(By.XPATH, "//form[@id='contactForm']//input[@type='email']")

8. contact_form = driver.find_element(By.XPATH, "//form[@id='contactForm']")

9. footer_paragraph = driver.find_element(By.XPATH, "//footer//p")

10. first_team_member = driver.find_element(By.XPATH, "//div[@class='team']//li[1]/h4")

11. second_service_description = driver.find_element(By.XPATH, "//div[@class='service-item'][2]/p")

12. contact_header = driver.find_element(By.XPATH, "//section[@id='contact']//h2")

13. dropdown_links = driver.find_elements(By.XPATH, "//li[a[text()='Services']]//ul[@class='dropdown']//a")

14. first_team_li = driver.find_element(By.XPATH, "//div[@class='team']//ul/li[1]")

15. send_message_button = driver.find_element(By.XPATH, "//form[@id='contactForm']//input[@type='submit' and @value='Send Message']")
