# Test Execution Report

## **Scenario 1: Submit valid rating and feedback**
As a user, I should be able to submit a valid rating and feedback for a product.

| Step# | Action                                         | Expected outcome                                                   | OK/NOK | URL  | Link to issue |
|-------|-----------------------------------------------|------------------------------------------------------------------|--------|------|---------------|
| 1     | Navigate to a product page, Complete the purchase of the product         | Product purchased                     | OK     | [Product Page](https://grocerymate.masterschool.com/product)     |               |
| 2     | Select 5 stars for the rating               | 5-star rating is highlighted                                     | OK     |      |               |
| 3     | Add a comment message                      | Message is entered successfully                                   | OK     |      |               |
| 4     | Click "Send"                                | Rating is saved, comment added      | NOK     |      | [Issue 01](https://github.com/Taekeiro/Portfolio/issues/5#issue-2874836952)              |

**Result:** Rating is saved but comment is not displayed.

![image](https://github.com/user-attachments/assets/c175f1b3-729b-4721-b8c9-df7ebcc826b5)
![image](https://github.com/user-attachments/assets/a87895f5-8efd-4ebf-a2b2-4c1b3e090b71)





## **Scenario 2: Submit invalid star rating (e.g., 0 stars)**
As a user, I should receive an error message when submitting an invalid rating.

| Step# | Action                                         | Expected outcome                                                   | OK/NOK | URL  | Link to issue |
|-------|-----------------------------------------------|------------------------------------------------------------------|--------|------|---------------|
| 1     | Navigate to a product page                   | Product page is displayed                                         | OK     | [Product Page](https://grocerymate.masterschool.com/product) |               |
| 2     | Enter an invalid rating (e.g., 0 stars)      | Input is not accepted                                             | OK     |      |               |
| 3     | Click "Send"                                | Error message is displayed                                        | OK     |      |               |

**Result:** The system behaved as expected.

![image](https://github.com/user-attachments/assets/a861873c-96f1-4400-b240-b28db2afca60)


## **Scenario 3: Edit and delete an existing rating**
As a user, I should be able to edit and delete an existing rating.

| Step# | Action                                         | Expected outcome                                                   | OK/NOK | URL  | Link to issue |
|-------|-----------------------------------------------|------------------------------------------------------------------|--------|------|---------------|
| 1     | Navigate to a product with a saved rating     | Product page with saved rating is displayed                       | OK     | [Product Page](https://grocerymate.masterschool.com/product) |               |
| 2     | Edit the rating to 3 stars                   | Rating is updated successfully                                    | OK     |      |               |
| 3     | Delete the rating                            | Rating is removed with a confirmation message                     | OK     |      |               |

**Result:** The system behaved as expected.

## **Scenario 4: Verify access for a user entering a valid age (18+)**
As a user, I should be able to access the alcohol section if I am 18 or older.

| Step# | Action                                  | Expected outcome                     | OK/NOK | URL           | Link to issue |
|-------|----------------------------------------|--------------------------------------|--------|--------------|---------------|
| 1     | Navigate to the alcohol section        | Age verification modal appears      | OK     | [Alcohol Section](https://grocerymate.masterschool.com/store#) |               |
| 2     | Enter age 18                           | Age is entered successfully         | OK     |              |               |
| 3     | Click confirm                          | Modal disappears, access is granted | OK     |              |               |

**Result:** The system behaved as expected

## **Scenario 5: Deny access for users below 18**
As a user, I should not be able to access the alcohol section if I am below 18.

| Step# | Action                                  | Expected outcome                     | OK/NOK | URL           | Link to issue |
|-------|----------------------------------------|--------------------------------------|--------|--------------|---------------|
| 1     | Navigate to the alcohol section        | Age verification modal appears      | OK     | [Alcohol Section](https://grocerymate.masterschool.com/store#) |               |
| 2     | Enter age 17                           | Age is entered successfully         | OK     |              |               |
| 3     | Click confirm                          | Error message appears               | OK     |              |               |

**Result:** The system behaved as expected.

![image](https://github.com/user-attachments/assets/e6417c7a-4771-4904-b3b1-96d47e7e5980)

## **Scenario 6: Reappearance of the modal on new sessions**
As a user, the age verification modal should reappear when I start a new session.

| Step# | Action                                  | Expected outcome                     | OK/NOK | URL           | Link to issue |
|-------|----------------------------------------|--------------------------------------|--------|--------------|---------------|
| 1     | Access the alcohol section             | Age verification modal appears      | OK     | [Alcohol Section](https://grocerymate.masterschool.com/store#) |               |
| 2     | Confirm age                            | Modal disappears                    | OK     |              |               |
| 3     | Log out and log back in                | Age verification modal appears again | NOK     |              | [Issue 02] (https://github.com/Taekeiro/Portfolio/issues/2#issue-2827103871)              |

**Result:** Age verification modal do not appear again after Relog.

![image](https://github.com/user-attachments/assets/13490a93-c673-4966-8d51-6fd216aa1c30)


## **Scenario 7: Verify free shipping for orders meeting the threshold**
As a user, I should receive free shipping when my order meets the threshold.

| Step# | Action                                  | Expected outcome                     | OK/NOK | URL            | Link to issue |
|-------|----------------------------------------|--------------------------------------|--------|---------------|---------------|
| 1     | Add items to cart worth $20            | Cart total updates correctly        | OK     | [Checkout](https://grocerymate.masterschool.com/checkout)      |               |
| 2     | Proceed to checkout                    | Checkout page loads                 | OK     |               |               |
| 3     | Verify shipping cost                   | Shipping cost is $0                 | OK     |               |               |

**Result:** The system behaved as expected.

![image](https://github.com/user-attachments/assets/43942890-3f50-476a-aeaf-cfe0df27ff78)


## **Scenario 8: Validate shipping cost for orders below the threshold**
As a user, I should be charged shipping if my order is below the threshold.

| Step# | Action                                  | Expected outcome                     | OK/NOK | URL            | Link to issue |
|-------|----------------------------------------|--------------------------------------|--------|---------------|---------------|
| 1     | Add items to cart worth $15            | Cart total updates correctly        | OK     | [Checkout](https://grocerymate.masterschool.com/checkout)      |               |
| 2     | Proceed to checkout                    | Checkout page loads                 | OK     |               |               |
| 3     | Verify shipping cost                   | Shipping cost displays correctly    | OK     |               |               |

**Result:** The system behaved as expected.

![image](https://github.com/user-attachments/assets/04c35626-81fd-4aaf-a45c-7835235fac52)


## **Scenario 9: Dynamically update shipping costs as items are added/removed**
As a user, my shipping costs should update dynamically based on my cart total.

| Step# | Action                                  | Expected outcome                     | OK/NOK | URL            | Link to issue |
|-------|----------------------------------------|--------------------------------------|--------|---------------|---------------|
| 1     | Add items worth $20                   | Free shipping is applied            | OK     | [Checkout](https://grocerymate.masterschool.com/checkout)      |               |
| 2     | Remove some items (total below $20)   | Shipping cost updates dynamically   | NOK     |               | [Issue 03](https://github.com/Taekeiro/Portfolio/issues/3#issue-2827114093)              |

**Result:** After adding product worth $20,  Free shipping is applied, but after removing some items from the list and getting total cost of lower than 20$, Shipping cost didn`t change (from 0$ to 5$)

![image](https://github.com/user-attachments/assets/130799b0-b36d-46be-ac1b-99c30ffad587)



