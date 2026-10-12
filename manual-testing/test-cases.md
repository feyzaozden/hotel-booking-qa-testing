
## TC-001 - Verify Successful Room Booking

**Jira Task:** Manual Booking Testing
**Module:** Room Booking
**Test Type:** Functional / Positive
**Priority:** High
**Status:** PASS
**Execution Date:** 2026-10-08

### Preconditions
- The application is accessible.
- A room is available for the selected dates.

### Test Data
- Room: Suite Room
- Check-in: 2026-10-08
- Check-out: 2026-10-10
- Guest information: Valid test data

### Test Steps
1. Open the hotel booking website.
2. Select the check-in and check-out dates.
3. Select the available Suite Room.
4. Enter valid guest information.
5. Click "Reserve Now".

### Expected Result
The system should confirm the reservation
and display the selected booking dates.

### Actual Result
The system displayed "Booking Confirmed"
and showed the dates:
2026-10-08 - 2026-10-10.

### Test Result
PASS

### Evidence
screenshots/TC-001-booking-confirmed.png







---

## TC-002 - Verify Required Field Validation

**Module:** Room Booking
**Test Type:** Functional / Negative
**Priority:** High
**Status:** PASS
**Execution Date:** 2026-10-08

### Preconditions
- The application is accessible.
- A room is available for selected dates.

### Test Data
- Room: Double Room
- Check-in: 2026-10-08
- Check-out: 2026-10-09
- Firstname: Empty
- Lastname: Empty
- Email: Empty
- Phone: Empty

### Test Steps
1. Open the hotel booking website.
2. Select valid booking dates.
3. Choose the Double Room.
4. Leave all guest information fields empty.
5. Click "Reserve Now".

### Expected Result
The system should display validation errors
and prevent the reservation from being created.

### Actual Result
The system displayed a red validation error
box containing messages about missing values
and field length requirements.

No booking confirmation was displayed.

### Test Result
PASS

### Evidence
screenshots/TC-002-required-fields.png











---

## TC-003 - Verify Invalid Email Validation

**Module:** Room Booking
**Test Type:** Functional / Negative
**Technique:** Equivalence Partitioning
**Priority:** High
**Status:** PASS
**Execution Date:** 2026-10-12

### Preconditions
- The booking website is accessible.
- An available room and valid dates are selected.

### Test Data
- Firstname: Test
- Lastname: User
- Email: testexample.com
- Phone: 07123456789

### Test Steps
1. Open the hotel booking website.
2. Select valid check-in and check-out dates.
3. Choose an available room.
4. Enter valid first name, last name, and phone.
5. Enter "testexample.com" in the email field.
6. Click "Reserve Now".

### Expected Result
The application should display an email
validation error and prevent booking
confirmation.


### Actual Result
The application rejected the invalid email
address and displayed the validation message:
"must be a well-formed email address".

The booking confirmation was not displayed.

### Test Result
PASS

### Evidence
screenshots/TC-003-invalid-email.png






---

## TC-004 - Verify Firstname Length Validation

**Module:** Room Booking
**Test Type:** Functional / Boundary Testing
**Technique:** Boundary Value Analysis
**Priority:** Medium
**Status:** PASS
**Execution Date:** 2026-10-12

### Preconditions
- The application is accessible.
- An available room and valid booking dates are selected.
- Other required fields contain valid data.

### Test Objective
Verify the minimum and maximum character
length requirements of the Firstname field.

### Validation Rule
Firstname must contain between 3 and
18 characters (inclusive).

### Test Data and Execution Results

| Length | Expected | Actual | Result |
|---|---|---|---|
| 2 | Rejected | Rejected | PASS |
| 3 | Accepted | Accepted | PASS |
| 4 | Accepted | Accepted | PASS |
| 18 | Accepted | Accepted | PASS |
| 19 | Rejected | Rejected | PASS |

### Test Steps
1. Open the hotel booking application.
2. Select an available room and valid dates.
3. Fill the other required fields with valid data.
4. Enter each Firstname test value separately.
5. Submit the booking form.
6. Verify whether the Firstname validation
   accepts or rejects the value.
7. Record the observed result.

### Expected Result
Values containing 3 to 18 characters should
pass the Firstname length validation.

Values shorter than 3 or longer than 18
characters should be rejected.

### Actual Result
The application accepted Firstname values
containing 3, 4, and 18 characters.

The application rejected 2-character and
19-character values with the message:
"size must be between 3 and 18".

### Test Result
PASS - All 5 boundary test cases passed.

### Evidence
screenshots/TC-004-firstname-boundary.png





## TC-005 - Verify Invalid Booking Date Range

**Module:** Booking Date Selection
**Test Type:** Functional / Negative
**Priority:** High
**Status:** FAIL
**Execution Date:** 2026-10-12

### Test Data
- Check-in: 2026-10-20
- Check-out: 2026-10-19
- Room: Double Room

### Expected Result
The application should reject a booking
date range where the check-out date is
earlier than the check-in date.

Invalid date ranges should not produce
negative booking durations or prices.

### Actual Result
The application allowed an invalid date
range and displayed:

- Duration: -1 nights
- Room charge: GBP -150
- Cleaning fee: GBP 25
- Service fee: GBP 15
- Total: GBP -110

The "Reserve Now" button remained enabled.

When proceeding, the user reported that
the page could not be loaded.

### Test Result
FAIL

### Evidence
screenshots/TC-005-invalid-date-range.png
