**Test Execution Document**

**1. Product Rating System**

**Test Design Techniques:** Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Use Case Testing

**Test Execution Summary:**
- **Test Environment:** Web Application
- **Test Data:** Various product ratings and feedback inputs
- **Execution Date:** [3-2-2025]
- **Tester:** [Sakharnyi Vladyslav]

**Test Case Execution:**
1. **Submit valid rating and feedback**  
   - **Steps:** Navigate to a product, select 5 stars, add a feedback message, click submit.  
   - **Expected Result:** Rating and feedback are saved successfully with a confirmation message.  
   - **Status:** [Fail] (Unable to test, need to buy a product first)
   
2. **Submit invalid star rating (e.g., 6 stars)**  
   - **Steps:** Enter an invalid rating (e.g., 6 stars), click submit.  
   - **Expected Result:** Error message displayed, rating not saved.  
   - **Status:** [Fail] (Unable to test, need to buy a product first)
   
3. **Edit and delete an existing rating**  
   - **Steps:** Navigate to a product with a saved rating, edit the rating to 3 stars, delete the rating.  
   - **Expected Result:** Rating is updated successfully, then removed with a confirmation message.  
   - **Status:** [Fail] (Unable to test, need to buy a product first)

**Automation Execution:** First two test cases automated.

---

**2. Age Verification for Alcoholic Products**

**Test Design Techniques:** Boundary Value Analysis (BVA), Equivalence Partitioning (EP), State Transition Testing

**Test Execution Summary:**
- **Test Environment:** Web Application
- **Test Data:** Age values 17, 18, 19
- **Execution Date:** [3-2-2025]
- **Tester:** [Sakharnyi Vladyslav]

**Test Case Execution:**
1. **Verify access for a user entering a valid age (18+)**  
   - **Steps:** Navigate to the alcohol section, enter age 18, click confirm.  
   - **Expected Result:** Access granted, modal disappears.  
   - **Status:** [Pass]
   
2. **Deny access for users below 18**  
   - **Steps:** Navigate to the alcohol section, enter age 17, click confirm.  
   - **Expected Result:** Access denied with an error message.  
   - **Status:** [Pass]
   
3. **Reappearance of the modal on new sessions**  
   - **Steps:** Access the alcohol section, confirm age, log out, log back in.  
   - **Expected Result:** Modal reappears to verify age again.  
   - **Status:** [Fail] (No Modal appears to verify age again)

**Automation Execution:** First two test cases automated.

---

**3. Dynamic Shipping Costs**

**Test Design Techniques:** Boundary Value Analysis (BVA), Decision Table Testing, Use Case Testing

**Test Execution Summary:**
- **Test Environment:** Web Application
- **Test Data:** Cart totals at various price points
- **Execution Date:** [3-2-2025]
- **Tester:** [Sakharnyi Vladyslav]

**Test Case Execution:**
1. **Verify free shipping for orders meeting the threshold**  
   - **Steps:** Add items to cart, ensure total equals $20, proceed to checkout.  
   - **Expected Result:** Shipping cost is $0, free shipping applied.  
   - **Status:** [Pass]
   
2. **Validate shipping cost for orders below the threshold**  
   - **Steps:** Add items worth $15 to the cart, proceed to checkout.  
   - **Expected Result:** Shipping cost displays accurately based on the configuration.  
   - **Status:** [Pass]
   
3. **Dynamically update shipping costs as items are added/removed**  
   - **Steps:** Add items worth 20$, proceed to checkout,  then remove some items to get total cost lower than 20$.
   - **Expected Result:** Shipping cost changes dynamically to reflect shipping cost.  
   - **Status:** [Fail] (Shipment costs are not updated)

**Automation Execution:** First and third test cases automated.

---

**Conclusion:**
The test execution revealed multiple issues across different functionalities:
- **Product Rating System:** All test cases failed due to a prerequisite requiring a product purchase before rating, which prevents further validation. This needs to be addressed before re-execution.
- **Age Verification:** Two test cases passed successfully, but the third failed as the modal did not reappear in a new session. Further investigation is required to verify the expected state transition behavior.
- **Dynamic Shipping Costs:** While the shipping cost calculations for the threshold and below-threshold cases worked correctly, the dynamic update mechanism failed. This issue needs fixing to ensure a seamless user experience.

Next Steps:
- Resolve the purchase prerequisite for testing the rating system.
- Investigate and fix the missing age verification modal in new sessions.
- Debug and fix the dynamic shipping cost update issue.
- Re-execute failed test cases after fixes and verify correctness.



