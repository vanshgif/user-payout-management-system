The primary objectives of the system are:

- Manage affiliate sales.
- Provide advance payouts for eligible pending sales.
- Prevent duplicate advance payouts.
- Calculate final payouts after reconciliation.
- Maintain accurate user wallet balances.
- Process user withdrawals.
- Recover failed payouts.


           COMPONENTS:
    1. CLIENT
The client interacts with the system through REST APIs.
Clients can be:

- Administrator
- User
- External applications
    
    2. BACKEND (PYTHON)
The FastAPI backend exposes REST APIs and acts as the central controller of the system.

It validates requests, executes business logic through services, and communicates with the database.

    3. SALE SERVICE

- Creating sales
- Managing sale status
- Retrieving sale information

    4. PAYOUT SERVICE

- Calculating advance payouts
- Preventing duplicate payouts
- Calculating final payouts
- Recovering rejected advances

    5. WITHDRAWAL SERVICE

- Processing withdrawals
- Enforcing the 24-hour withdrawal rule
- Handling payout failures
- Updating user balances

    6. DATABASE

Stores all system data including:

- Users
- Sales
- Payouts
- Withdrawals

    7. PAYMENT GATEWAY

Represents the external banking/payment service responsible for transferring money to users.

The gateway may return:

- Success
- Failed
- Cancelled
- Rejected

These responses are handled by the Withdrawal Service.

          HIGH LEVEL WORKFLOW:
        
        Customer purchases a product
            │
            ▼
        Sale created
        (Status = Pending)
            │
            ▼
        Advance Payout Job
            │
            ▼
        User Wallet Updated
            │
            ▼
        Admin Reconciliation
            │
        Approved / Rejected
            │
            ▼
        Final Balance Updated
            │
            ▼
        User Withdrawal Request
            │
            ▼
        Payment Gateway
            │
        Success / Failed