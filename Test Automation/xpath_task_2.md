## 1. Highlighted icon
//div[@class='headerIcon'][1]

## 2.Email input field
//input[@type='email' and @placeholder='Email address'] 
### Password input field
//input[@type='password' and @placeholder='Password'] 
### Sign in button
//button[@type='submit' and contains(@class, 'submit-btn')]
### Create a new account link
//a[contains(@class, 'switch-link') and text()='Create a new account'] 
### Go to Home link
//a[contains(@class, 'home-link') and text()='Go to Home'] 
## 3. Full name field
//input[@type='text' and @placeholder='Full Name']
### Email field
//input[@type='email' and @placeholder='Email address']
### Password field
//input[@type='password' and @placeholder='Password']
### Sign Up button
//button[@type='submit' and contains(@class, 'submit-btn') and text()='Sign Up']
## 4. Confirm button
//div[@class='modal-overlay']//button[text()='Confirm']
## 5. Oranges
### Quantity input of Oranges
//p[text()='Oranges']/ancestor::div[@class='card']//input[@type='number']
### Add to cart button for Oranges
//p[text()='Oranges']/ancestor::div[@class='card']//button[contains(text(),'Add to Cart')]
### Add to wish list for Oranges
//p[text()='Oranges']/ancestor::div[@class='card']//button[contains(@class,'btn-outline-dark')]


