### 1. Introduction
#### System Description
 The developed system is a desktop application in Python with Tkinter, designed for generating shipping labels for parcel deliveries. The application allows users to enter sender and recipient details, validate the entered information, and generate a PDF file with the shipping label.

#### Testing Objectives
 The main objective of this testing phase is to verify that the system functions correctly, ensuring data validation, form integrity, and proper PDF file generation. The aim is to identify errors and potential improvements before proceeding with future versions.

### 2. Test Plan
The tests performed include:

* Functional testing: Verifying that each system function fulfills its intended purpose.
*  Data validation testing: Ensuring that input fields accept only the correct values (letters in names, numbers in ID fields, etc.).
* Integrity testing: Checking that the information entered in the forms is correctly reflected in the generated PDF.
* Usability testing: Reviewing the ease of use of the interface.
* Error handling testing: Entering incorrect or missing data to verify that the system responds appropriately.

### 3. Casos de Prueba
#### TEST CASES - Functional - Project: SendUrPack - Version: 1

|ID|Test type|Description|Pre-Condition|Steps|Expected Result|Current Result|
|---|---|---|---|---|---|---|
|TC-001|Happy Path|Opening the application and confirming forms are visible correctly|Application must be installed.|1. Open the application.</br>2. Check the main window.</br>3. Confirm forms and button visibility.</br>4. Check main window.|Application opens without errors and accessible form.|Pass|
|TC-002|Happy Path|Validation of numeric fields allowing only numbers.|Application must be open.|1. Enter "123" in numeric fields (ID, Phone, Number, Postal Code, Floor).</br> 2. Verify the input is accepted.</br> 3. Attempt entering non-numeric characters.</br> 4. Verify they are rejected.|Only numbers (0-9) can be entered, other characters are rejected|Pass|
|TC-003|Negative Path|Validation of numeric fields rejecting letters/space|Application must be open.|1. Enter letters or spaces in numeric fields (ID, Phone, Number, Postal Code, Floor).</br> 2. Verify that input is not accepted.|The system does not accept non-numeric input in these fields.|Pass|
|TC-004|Happy Path|Validation of alphabetic fields allowing only letters and spaces.|Application must be open.|1. Enter letters and spaces in fields (Last Name, First Name, Street, City, State).</br> 2. Verify input is accepted.</br> 3. Attempt entering numbers or symbols.</br> 4. Verify they are rejected.|Only alphabetic characters and spaces are accepted. Other characters are rejected.|Pass|
|TC-005|Negative Path|Validation of alphabetic fields rejecting numbers.|Application must be open.|1. Enter numbers in fields (Last Name, First Name, Street, City, State).</br>2. Verify input is rejected.|The system does not accept numeric input in these fields.|Pass|
|TC-006|Happy Path|Generation of shipping label with valid inputs.|Application must be open.|1. Fill all required fields with valid data.</br>2. Click "Generate Shipping Label".</br>3. Verify the success message.</br>4. Open the generated PDF.</br>5. Verify that it contains all required information.|The system generates a correctly formatted PDF when all fields are completed|Pass|
|TC-007|Happy Path|Attempting to generate PDF with missing required fields.|Application must be open.|1. Leave one or more required fields empty.</br>2. Click "Generate Shipping Label".</br>3. Verify that the error message appears.</br>4. Ensure no PDF is generated.|The system prevents PDF generation if required fields are missing and displays an error message.|Pass|
|TC-008|Happy Path|After the PDF is generated correctly, all entries in the fields are deleted.|Application must be open.|1. Execute CP-06.</br>2. Verify that all form fields are reset, meaning that all previously entered data is cleared.|Every time a PDF is generated, all fields must be reset.|Pass| 

### 4. Errors Found and Corrections
In this case, no errors were found during test execution. The system behaved as expected in all scenarios.

#### Suggestions for Improvement:
Although no issues were identified, the following improvements can be considered to optimize functionality:
Adjust character limit: This could enhance the user experience by defining the maximum number of characters allowed in each field, preventing the entry of extra characters.

### 5. Conclusions
The system has demonstrated compliance with functional requirements. No errors were detected in field validations, and the PDF document is successfully generated and saved in the desired folder.

