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