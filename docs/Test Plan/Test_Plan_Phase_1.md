# Testing Plan

## 1. Introduction
This testing plan aims to verify that the shipping label generation process functions correctly, ensuring proper data capture, validation, and PDF file generation.

## 2. Scope
The tests will be conducted on the "Generate Shipping Label" functionality within the desktop application.

## 3. Types of Tests
* Functional Testing: Validate that the data entry flow and PDF generation work correctly.
* Field Validation Testing: Ensure that the entered data meets the established restrictions.
* File Generation Testing: Verify that the PDF is correctly created with the entered data.
* UX/UI Testing: Assess that graphical elements are displayed correctly and are accessible.

## 4. Test Cases

### Test Case 1: Application Launch</br>
**ID:** CP-01</br>
**Description:** Verify that the application opens without errors and correctly displays the data entry form.</br>
**Preconditions:** The application must be correctly installed.</br>
**Steps:** 
1. Turn on the device (if necessary).
2. Locate the application icon.
3. Click on the application icon to open it.
4. Wait for the application to fully load.
5. Verify that the application’s home screen displays without visual errors (e.g., missing, distorted, or overlapping elements).
6. Ensure that the data entry form (fields, labels, buttons, etc.) is complete and displayed correctly.
7. Check that all form elements are interactive (e.g., fields can be selected, buttons can be clicked).</br>

**Expected Result:**
* The application opens without errors and correctly displays the home screen.
* The data entry form is fully visible, with no visual errors, and all its elements are interactive.
* The application does not close unexpectedly or show error messages during the loading process.

### Test Case 2: Correct Validation of Numeric Characters</br>
**ID:** CP-02</br>
**Description:** Verify that the "ID", "Phone", "Number", "Postal Code", and "Floor" fields allow the entry of numeric characters without spaces.</br>
**Preconditions:** The application must be open.</br>
**Steps:**
1. Open the application.
2. Enter "123" in the "ID" field.
3. Verify that the number "123" appears in the field.
4. Repeat steps 2 and 3 for the "Phone", "Number", "Postal Code", and "Floor" fields.
5. Ensure numbers can be entered without spaces.
6. Enter an invalid format (e.g., letters, symbols) in each numeric field.
7. Verify that non-numeric characters cannot be entered.

**Expected Result:**
* The system allows numeric characters (0-9) without spaces in the "ID", "Phone", "Number", "Postal Code", and "Floor" fields.
* No other characters can be entered.

### Test Case 3: Incorrect Validation of Numeric Characters
**ID:** CP-03</br>
**Description:** Verify that the "ID", "Phone", "Number", "Postal Code", and "Floor" fields do not allow alphabetic characters or spaces.</br>
**Preconditions:** The application must be open.</br>
**Steps:**</br>
1. Open the application.
2. Enter the letter "a" in the "ID" field.
3. Verify that the letter "a" does not appear in the field.
4. Repeat steps 2 and 3 for all lowercase letters (a-z).
5. Repeat steps 2 and 3 for all uppercase letters (A-Z).
6. Enter a space in the "ID" field.
7. Verify that the space does not appear.
8. Repeat steps 2-7 for the "Phone", "Number", "Postal Code", and "Floor" fields.

**Expected Result:**
* The system does not allow alphabetic characters (a-z, A-Z) or spaces in the "ID", "Phone", "Number", "Postal Code", and "Floor" fields.
* Pressing alphabetic or space keys does not affect the fields.

### Test Case 4: Correct Validation of Alphabetic Characters
**ID:** CP-04</br>
**Description:** Verify that the "Last Name", "First Name", "Street", "City", and "State" fields allow only letters and spaces.</br>
**Preconditions:** The application must be open.</br>
**Steps:**</br>
1. Open the application.
2. Enter the letter "a" in the "Last Name" field.
3. Verify that the letter "a" appears.
4. Repeat steps 2 and 3 for all lowercase letters (a-z).
5. Repeat steps 2 and 3 for all uppercase letters (A-Z).
6. Enter a space in the "Last Name" field.
7. Verify that the space appears.
8. Repeat steps 2-7 for the "First Name", "Street", "City", and "State" fields.

**Expected Result:**
* The system allows alphabetic characters (a-z, A-Z) and spaces in the "Last Name", "First Name", "Street", "City", and "State" fields.
* No other characters (numbers, symbols, etc.) are allowed.

### Test Case 5: Incorrect Validation of Alphabetic Characters
**ID:** CP-05</br>
**Description:** Verify that the "Last Name", "First Name", "Street", "City", and "State" fields do not allow numeric characters.</br>
**Preconditions:** The application must be open.</br>
**Steps:**
1. Open the application.
2. Enter the number "1" in the "Last Name" field.
3. Verify that the number "1" does not appear.
4. Repeat steps 2 and 3 for numbers 2-9 and 0.
5. Repeat steps 2-4 for the "First Name", "Street", "City", and "State" fields.</br>

**Expected Result:**
* The system does not allow numeric characters (0-9) in the "Last Name", "First Name", "Street", "City", and "State" fields.
* Pressing numeric keys does not affect the fields.

### Test Case 6: Valid Data Entry and PDF Generation
**ID:** CP-06</br>
**Description:** Verify that the shipping label is correctly generated when valid data is entered in the mandatory fields ("Last Name", "First Name", "ID", "Phone", "Street", "Number", "City", "State", "Postal Code").</br>
**Preconditions:** The application must be running.</br>
**Steps:**
1. Open the application.
2. Enter valid data in all mandatory fields:</br>
* "Last Name": "Example"
* "First Name": "Example"
* "ID": "12345678"
* "Phone": "123-456-7890"
* "Street": "Example Street 123"
* "Number": "123"
* "City": "Example City"
* "State": "Example State"
* "Postal Code": "12345"</br>
3. Press the "Generate Shipping Label" button.
4. Verify that the system displays a success message: "Success, Shipping Label generated successfully."
5. Press the "OK" button on the success message.
6. Verify that the PDF file opens immediately in the default PDF viewer on the user's computer.
7. Verify that the PDF contains all the data entered in the mandatory fields, with the correct format and in a readable manner.</br>

**Expected Result:**
* The PDF is correctly generated when all mandatory fields are complete.
* The PDF is saved in the designated folder (specify the folder in the documentation).
* The PDF file name follows the specified format (e.g., "LastName_FirstName_DateTime").
* The PDF contains all the data entered in the mandatory fields, formatted correctly and legibly.
* Optional fields (if any) may or may not be completed, and this should not affect PDF generation.

### Test Case 7: Attempt to Generate PDF Without Completing Mandatory Fields
**ID:** CP-07</br>
**Description:** Verify that the system does not allow generating a shipping label if one or more of the mandatory fields ("Last Name", "First Name", "ID", "Phone", "Street", "Number", "City", "State", "Postal Code") are empty.</br>
**Preconditions:** The application must be open.</br>
**Steps:**

***Scenario 1: All fields empty***</br>
1. Open the application.
2. Press the "Generate Shipping Label" button.
3. Verify that the system displays the error message: ***"Error, Fields marked with (*) *are required."***
4. Verify that the PDF is not generated.</br>

***Scenario 2: One mandatory field empty***</br>
1. Open the application.
2. Fill in all mandatory fields except the "Last Name" field.
4. Press the "Generate Shipping Label" button.
5. Verify that the system displays the error message: ***"Error, Fields marked with (*) *are required."***
6. Verify that the PDF is not generated.
7. Repeat ***Scenario 2*** for each of the mandatory fields: "First Name", "ID", "Phone", "Street", "Number", "City", "State", and "Postal Code".</br>

**Expected Result:**
* The system displays a clear and specific error message: ***"Error, Fields marked with (*) *are required."*** if an attempt is made to generate the label with one or more mandatory fields left empty.
* The PDF is not generated if any mandatory fields are empty.
* The error message must clearly indicate which fields are mandatory and left empty.

### Test Case 8: Reset of Form Fields After PDF Generation
**ID:** CP-08</br>
**Description:** Verify that after the PDF is successfully generated and opened, all fields in the form are reset, meaning all previously entered data is cleared.</br>
**Preconditions:** The application must be open.</br>
**Steps:**
1. Execute CP-06 
2. Check that all fields in the form are reset, meaning all previously entered data is cleared.</br>

**Expected Result:**
Every time a PDF is generated, all fields must be reset.

## 5. Acceptance Criteria
* The application must allow valid data entry and correctly generate a PDF.
* If fields are empty, the system must display an error and prevent PDF generation.
* The PDF must contain the exact entered data.
* The PDF must be saved in the specified folder.
* The interface must be user-friendly and accessible.

