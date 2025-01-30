# Requirements

## **The software**

A webshop, which can be found here: [Market Mate](https://grocerymate.masterschool.com/)

The webshop has the following basic functionalities:

- Register and login functionality
- Searching for products, sorting on price, categories of products
- Add products to favorites
- Add products to basket
- Check-out process: billing and sending information in a form, choose payment method. Calculation of costs (calculate total price)

## **New features**

### **1. Product Rating System**

**Requirement:** Users should be able to rate products with a 5-star system and have the option to add written feedback.**

**Questions**:

**Functionality**:
1. Can a user submit a rating and written feedback successfully?
2. Does the system allow only valid inputs (e.g., star ratings between 1-5)?
3. Are users able to edit or delete their submitted ratings and feedback?
4. Can users rate only products they have purchased?
   
**Usability**:
1. Is the rating system user-friendly and intuitive?
2. Does the interface handle errors gracefully (e.g., trying to submit without selecting a star or entering invalid text)?
3. Is there visual confirmation when a rating or feedback is submitted?
   
**Data Integrity**:
1. Are the ratings and feedback stored correctly and displayed accurately for the product?
2. Is the average star rating calculated and updated correctly?
3. Does the system prevent duplicate ratings from the same user for the same product?

**Detailed Requirement:**
Users can rate products using a 5-star system and submit written feedback (max 500 characters).
Ratings must be between 1-5 stars; feedback is optional but cannot exceed character limits.
Users can edit or delete their ratings/feedback, and duplicate submissions for the same product are not allowed.


### **2. Age Verification for Alcoholic Products**

**Vague Requirement**:

- Alcoholic products require age verification. A modal should appear when navigating to the alcoholic products category asking if the user is 18+. Users must input their age before accessing the alcoholic products.

**Questions**:

**Functionality:**
1. When the notification should pop-up? (when entering the alcohol page or just at the beginning of the session)
2. Is the modal dismissed only after valid input (e.g., entering an age above 18)?
3. Does the system block access if invalid or no input is provided?

**Security:**
1. Is user age stored securely and compliant with privacy regulations?
2. Can the age verification mechanism be bypassed (e.g., refreshing the page, direct URL access)?
3. Does the modal reappear if the user logs out or clears cookies?

**Edge cases:**
1. What happens if a user enters an invalid or edge-case age (e.g., 0, negative values, text input)?
2. Is the age verification modal accessible and functional on all device types (desktop, mobile, tablet)?

**Detailed Requirement**:

Users must confirm they are 18+ via a modal when accessing the alcoholic products category.
The popup appears **only** when navigating to alcoholic product pages, not on other pages.
Input must accept only numeric values; users under 18 or with invalid input are denied access.
The modal must reappear for new sessions or after clearing cookies.

### **3. Shipping Cost Changes**

**Vague Requirement**:

Free shipping for orders above a certain amount. Orders below this amount will incur a shipping fee.

**Questions**:

1. Is free shipping applied correctly when the order exceeds the threshold amount?
2. Are the shipping costs calculated accurately for orders below the threshold?
3. Are the shipping costs updated correctly if items are added/removed from the basket?
4. Is the shipping cost clearly displayed during checkout?
5. Is the user informed when they qualify for free shipping (e.g., via message)?
6. What happens if the basket total is exactly equal to the free shipping threshold?

**Detailed Requirement**:

Orders above a configurable threshold ($20) qualify for free shipping; otherwise, a shipping fee is applied.
Shipping costs update dynamically when items are added or removed and must reflect in the total cost breakdown.
Users should see a message when they qualify for free shipping.
