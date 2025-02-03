# Test Execution Report

## **Scenario 1: Submit valid rating and feedback**
As a user, I should be able to submit a valid rating and feedback for a product.

| Step# | Action                                         | Expected outcome                                                   | OK/NOK | URL  | Link to issue |
|-------|-----------------------------------------------|------------------------------------------------------------------|--------|------|---------------|
| 1     | Navigate to a product page                   | Product page is displayed                                         | OK     | [Oranges](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f) |               |
| 2     | Select 5 stars for the rating               | 5-star rating is highlighted                                     | OK     |  |               |
| 3     | Add a feedback message                      | Message is entered successfully                                 | OK     |  |               |
| 4     | Click submit                                | Confirmation message appears, rating is saved                   | NOK    |  | [Issue-001](https://github.com/Taekeiro/Portfolio/issues/1) |

## **Scenario 2: Submit invalid star rating (e.g., 6 stars)**
As a user, I should receive an error message when submitting an invalid rating.

| Step# | Action                                         | Expected outcome                                                   | OK/NOK | URL  | Link to issue |
|-------|-----------------------------------------------|------------------------------------------------------------------|--------|------|---------------|
| 1     | Navigate to a product page                   | Product page is displayed                                         | OK     | [Oranges](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f) |               |
| 2     | Enter an invalid rating (e.g., 6 stars)     | Input is not accepted                                           | OK     |          |               |
| 3     | Click submit                                | Error message is displayed                                      | NOK    |          | [Issue-001](https://github.com/Taekeiro/Portfolio/issues/1) |

## **Scenario 3: Verify access for a user entering a valid age (18+)**
As a user, I should be able to access the alcohol section if I am 18 or older.

| Step# | Action                                  | Expected outcome                     | OK/NOK | URL           | Link to issue |
|-------|----------------------------------------|--------------------------------------|--------|--------------|---------------|
| 1     | Navigate to the alcohol section       | Age verification modal appears      | OK     | [alcohol-page](https://grocerymate.masterschool.com/store#) |               |
| 2     | Enter age 18                          | Age is entered successfully         | OK     |                |               |
| 3     | Click confirm                         | Modal disappears, access is granted | OK     |                |               |

## **Scenario 4: Deny access for users below 18**
As a user, I should not be able to access the alcohol section if I am below 18.

| Step# | Action                                  | Expected outcome                     | OK/NOK | URL           | Link to issue |
|-------|----------------------------------------|--------------------------------------|--------|--------------|---------------|
| 1     | Navigate to the alcohol section       | Age verification modal appears      | OK     | [alcohol-page](https://grocerymate.masterschool.com/store#) |               |
| 2     | Enter age 17                          | Age is entered successfully         | OK     |                 |               |
| 3     | Click confirm                         | Error message appears               | OK     |                 |               |

## **Scenario 5: Reappearance of the modal on new sessions**
As a user, the age verification modal should reappear when I start a new session.

| Step# | Action                                  | Expected outcome                     | OK/NOK | URL           | Link to issue |
|-------|----------------------------------------|--------------------------------------|--------|--------------|---------------|
| 1     | Access the alcohol section            | Age verification modal appears      | OK     | [alcohol-page](https://grocerymate.masterschool.com/store#) |               |
| 2     | Confirm age                           | Modal disappears                    | OK     |                 |               |
| 3     | Log out and log back in               | Age verification modal appears again | NOK    | [alcohol-page](https://grocerymate.masterschool.com/store#) | [Issue-002](https://github.com/Taekeiro/Portfolio/issues/2) |

## **Scenario 6: Verify free shipping for orders meeting the threshold**
As a user, I should receive free shipping when my order meets the threshold.

| Step# | Action                                  | Expected outcome                     | OK/NOK | URL            | Link to issue |
|-------|----------------------------------------|--------------------------------------|--------|---------------|---------------|
| 1     | Add items to cart worth $20           | Cart total updates correctly        | OK     | [checkout](https://grocerymate.masterschool.com/checkout)      |               |
| 2     | Proceed to checkout                   | Checkout page loads                 | OK     |                 |               |
| 3     | Verify shipping cost                  | Shipping cost is $0                 | OK     |                 |               |

## **Scenario 7: Validate shipping cost for orders below the threshold**
As a user, I should be charged shipping if my order is below the threshold.

| Step# | Action                                  | Expected outcome                     | OK/NOK | URL            | Link to issue |
|-------|----------------------------------------|--------------------------------------|--------|---------------|---------------|
| 1     | Add items to cart worth $15           | Cart total updates correctly        | OK     | [checkout](https://grocerymate.masterschool.com/checkout)      |               |
| 2     | Proceed to checkout                   | Checkout page loads                 | OK     |                 |               |
| 3     | Verify shipping cost                  | Shipping cost displays correctly     | OK     |                |               |

## **Scenario 8: Dynamically update shipping costs as items are added/removed**
As a user, my shipping costs should update dynamically based on my cart total.

| Step# | Action                                  | Expected outcome                     | OK/NOK | URL            | Link to issue |
|-------|----------------------------------------|--------------------------------------|--------|---------------|---------------|
| 1     | Add items worth $20                   | Free shipping is applied            | OK     | [checkout](https://grocerymate.masterschool.com/checkout)      |               |
| 2     | Remove some items (total below $20)   | Shipping cost updates dynamically   | NOK    |                 | [Issue-003](https://github.com/Taekeiro/Portfolio/issues/3) |

