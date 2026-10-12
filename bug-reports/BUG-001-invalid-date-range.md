
# BUG-001 - Invalid Date Range Produces Negative Booking Price

**Jira Issue:** HBQA-8
**Related Test Case:** TC-005
**Severity:** Major
**Priority:** High
**Status:** Open
**Environment:** Windows / Google Chrome

## Description
The booking application allows a check-out
date earlier than the check-in date,
resulting in a negative booking duration
and an incorrect negative total price.

## Steps to Reproduce
1. Open https://automationintesting.online/
2. Select October 20, 2026 as check-in.
3. Select October 19, 2026 as check-out.
4. Open the Double Room booking page.
5. Observe the price summary.

## Expected Result
The application should reject invalid
booking date ranges and prevent negative
booking durations and prices.

## Actual Result
The application displayed:
- Duration: -1 nights
- Room charge: GBP -150
- Cleaning fee: GBP 25
- Service fee: GBP 15
- Total: GBP -110

The Reserve Now button remained enabled.

## Evidence
See: ../screenshots/TC-005-invalid-date-range.png

## Jira Reference
HBQA-8
