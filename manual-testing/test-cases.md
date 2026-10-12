
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

