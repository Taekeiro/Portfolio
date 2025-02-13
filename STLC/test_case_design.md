# Test Cases

### **1. Product Rating System**

**Test Design Techniques**: Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Use Case Testing

#### Test Cases:

1. **Boundary Value Analysis**:
     - **Test Case**: Submit valid rating and feedback.
     - **Steps**: Navigate to a product, select 5 stars, add a feedback message, click submit.
     - **Expected Result**: Rating and feedback are saved successfully with a confirmation message.

2. **Equivalence Partitioning**:
     - **Test Case**: Submit invalid star rating (e.g., 6 stars).
     - **Steps**: Enter an invalid rating (e.g., 6 stars), click submit.
     - **Expected Result**: Error message displayed, rating not saved.

3. **Use Case Testing**:
     - **Test Case**: Edit and delete an existing rating.
     - **Steps**: Navigate to a product with a saved rating, edit the rating to 3 stars, delete the rating.
     - **Expected Result**: Rating is updated successfully, then removed with a confirmation message.

**Automate?**: Automate the first two test cases due to frequent and critical validation needs.

---

### **2. Age Verification for Alcoholic Products**

**Test Design Techniques**: Boundary Value Analysis (BVA), Equivalence Partitioning (EP), State Transition Testing

#### Test Cases:

1. **Boundary Value Analysis**:
     - **Test Case**: Verify access for a user entering a valid age (18+).
     - **Steps**: Navigate to the alcohol section, enter age 18, click confirm.
     - **Expected Result**: Access granted, modal disappears.

2. **Equivalence Partitioning**:
     - **Test Case**: Deny access for users below 18.
     - **Steps**: Navigate to the alcohol section, enter age 17, click confirm.
     - **Expected Result**: Access denied with an error message.

3. **State Transition Testing**:
     - **Test Case**: Reappearance of the modal on new sessions.
     - **Steps**: Access the alcohol section, confirm age, log out, log back in.
     - **Expected Result**: Modal reappears to verify age again.

**Automate?**: Automate the first two test cases as age validation is critical and repetitive.

---

### **3. Dynamic Shipping Costs**

**Test Design Techniques**: Boundary Value Analysis (BVA), Decision Table Testing, Use Case Testing

#### Test Cases:

1. **Boundary Value Analysis**:
     - **Test Case**: Verify free shipping for orders meeting the threshold.
     - **Steps**: Add items to cart, ensure total equals $20, proceed to checkout.
     - **Expected Result**: Shipping cost is $0, free shipping applied.

2. **Decision Table Testing**:
     - **Test Case**: Validate shipping cost for orders below the threshold.
     - **Steps**: Add items worth $15 to the cart, proceed to checkout.
     - **Expected Result**: Shipping cost displays accurately based on the configuration.

3. **Use Case Testing**:
     - **Test Case**: Dynamically update shipping costs as items are added/removed.
     - **Steps**: Add items worth $18, proceed to checkout, then add more items to exceed $20.
     - **Expected Result**: Shipping cost changes dynamically to reflect free shipping.

**Automate?**: Automate the first and third test cases as they are critical to user satisfaction and frequently executed.

---

### **4. Add to Cart Feature**

**Test Design Techniques**: Equivalence Partitioning (EP), Boundary Value Analysis (BVA)

#### Test Cases:

1. **Equivalence Partitioning**:
     - **Test Case**: Add a single item to the cart.
     - **Steps**: Navigate to a product page, click "Add to Cart."
     - **Expected Result**: Item appears in the cart, and a pop-up message confirms "Item Successfully added to the cart."

2. **Boundary Value Analysis**:
     - **Test Case**: Add multiple quantities of the same item.
     - **Steps**: Increase quantity to 5, click "Add to Cart."
     - **Expected Result**: The cart correctly reflects 5 items, and the pop-up confirmation appears.

**Automate?**: Automate the first and second test cases as they are critical and repetitive user interactions.
