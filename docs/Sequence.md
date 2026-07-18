1.Create Sales

User/Admin
    │
    │ Create Sale Request
    ▼
FastAPI
    │
    ▼
Sale Service
    │
    ▼
Database
    │
Save Sale (Status = Pending)
    │
    ▼
Success Response

>When a customer purchases a product through an affiliate link, a new sale is created with the status set to Pending. The Sale Service validates the request and stores the sale in the database.


2. Advance Payout

Scheduler
    │
    ▼
Payout Service
    │
    ▼
Database
    │
Find Pending Sales
    │
    ▼
Calculate 10% Advance
    │
    ▼
Create Payout Record
    │
    ▼
Update Wallet Balance
    │
    ▼
Mark Sale as Advance Paid

>The scheduler periodically checks all eligible pending sales. If the sale has not already received an advance payout, the system calculates 10% of the earning, creates a payout record, updates the user's wallet balance, and marks the sale as advance paid.

3. Sale Reconciliation

Admin
    │
    ▼
FastAPI
    │
    ▼
Payout Service
    │
    ▼
Database

      Approved?
      /      \
    Yes      No
    │         │
Pay Remaining  Create Adjustment
    │         │
Update Wallet Balance
    │
    ▼
Success

>The administrator updates the sale status. If the sale is approved, the remaining payout is credited after deducting the advance. If rejected, the previously paid advance is recovered by creating a negative adjustment.

4. Withdrawal

User
    │
    ▼
FastAPI
    │
    ▼
Withdrawal Service
    │
Check Balance
    │
Check 24-Hour Rule
    │
Create Withdrawal
    │
Send to Payment Gateway
          │
   ┌──────┴───────┐
   ▼              ▼
Success        Failed
   │              │
Update Status  Refund Wallet

>The system validates the user's wallet balance and checks whether a withdrawal has already been made within the last 24 hours. If valid, the withdrawal request is processed through the payment gateway. If the transfer fails, the amount is credited back to the user's wallet.

