**Test Plan for GroceryMate - New Features**

---

### **1. Overview**

#### **Objective**

This test plan outlines the approach for validating new features introduced in the GroceryMate webshop. The goal is to ensure these features function as expected, integrate smoothly with existing functionalities, and provide a seamless user experience.

#### **New Features Under Test**

- **Product Rating System**: Allows customers to rate and review products.
- **Age Verification for Alcoholic Products**: Restricts purchases based on age validation.
- **Dynamic Shipping Cost Calculation**: Automatically updates shipping costs based on user input.

#### **Key Risks to Mitigate**

- Users being unable to leave or view ratings properly.
- Age verification being bypassed or failing incorrectly.
- Incorrect shipping costs leading to checkout issues or abandoned carts.

---

### **2. Scope of Testing**

#### **In Scope**

- **Core functionalities of new features** (Rating, Age Verification, Shipping Cost Calculation).
- **User interactions with these features**, including login dependencies.
- **Integration with existing checkout and purchase flows.**
- **Frontend and backend validation of age verification.**
- **Usability testing to ensure ease of use and clarity.**
- **Performance testing for dynamic calculations under various conditions.**

#### **Out of Scope**

- Security validation of third-party payment gateways.
- Backend database performance optimization.
- Load testing beyond expected usage scenarios.

---

### **3. Testing Approach**

#### **Testing Strategy**

1. **Exploratory Testing** (Initial Phase)

   - Conduct unscripted testing to identify usability issues and edge cases.
   - Explore potential user paths, including error handling.

2. **Structured Test Execution**

   - Develop test cases based on feature specifications.
   - Execute functional, usability, performance, and security tests.

3. **Regression Testing**

   - Ensure new features do not introduce issues into existing workflows.

#### **Types of Testing**

- **Functional Testing:** Validate expected behavior of each new feature.
- **Usability Testing:** Assess ease of use from a customer’s perspective.
- **Performance Testing:** Ensure real-time calculations work efficiently.
- **Security Testing:** Confirm proper handling of sensitive user data.
- **Regression Testing:** Identify unintended side effects on existing functionality.

---

### **4. Test Objectives**

| Feature                   | Key Test Objectives                                                                                                                            |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Product Rating System     | Ensure users can submit, edit, and delete ratings correctly. Validate display of average ratings and reviews.                                  |
| Age Verification          | Confirm valid users can purchase restricted products while underage users are blocked. Check handling of network failures or incorrect inputs. |
| Shipping Cost Calculation | Validate price updates based on shipping address, product weight, and promotions. Test various location-based inputs.                          |

---

### **5. Test Environment & Resources**

#### **Test Environments**

- **DEV (Development):** Initial feature testing.
- **TEST (Testing):** Dedicated environment for structured test execution.
- **ACC (Acceptance):** Final validation before deployment.

#### **Required Devices & Software**

- **Devices:** Desktop (Windows/macOS), Mobile (iOS/Android)
- **Browsers:** Chrome, Firefox, Safari, Edge
- **Tools:** Test automation framework, performance monitoring tools

#### **Team Members & Responsibilities**

- **Test Manager:** Oversees test planning & execution.
- **QA Engineers:** Execute functional, usability, and performance tests.


---

### **6. Test Execution Plan**

| **Phase**             | **Start Date** | **End Date** | **Responsible** |
| --------------------- | -------------- | ------------ | --------------- |
| Exploratory Testing   | 01/08/2024     | 05/08/2024   | QA Team         |
| Test Case Development | 06/08/2024     | 10/08/2024   | QA Team         |
| Functional Testing    | 11/08/2024     | 20/08/2024   | QA Team         |
| Usability Testing     | 21/08/2024     | 25/08/2024   | QA Team         |
| Performance Testing   | 26/08/2024     | 28/08/2024   | QA Team         |
| Regression Testing    | 29/08/2024     | 02/09/2024   | QA Team         |
| UAT                   | 03/09/2024     | 10/09/2024   | End Users       |

---

### **7. Test Deliverables**

- **Test Plan Document** (this document)
- **Test Cases**
- **Test Execution Reports**
- **Defect Reports & Bug Logs**
- **Final Test Summary**

---

### **8. Exit Criteria**

- All critical and high-priority defects are resolved.
- No major usability or performance issues remain.
- Test execution is complete, and sign-off is received.

---



