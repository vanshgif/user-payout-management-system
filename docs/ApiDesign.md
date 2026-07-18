The User Payout Management System exposes RESTful APIs to manage affiliate sales, advance payouts, reconciliation, withdrawals, and payout recovery.

These APIs allow administrators and users to interact with the system while enforcing the defined business rules.

## Create Sales

Endpoint:
>POST /sales
Description
Creates a new affiliate sale with Pending status.

## Get all sales

Endpoint:
>GET /sales
Description
Returns all sales.

## Get Sale By ID

Endpoint:
>GET /sales/{sale_id}
Description
Returns details of a specific sale.

## Run Advance Payout

Endpoint:
>POST /payouts/advance
Description
Runs the advance payout process.
Eligible pending sales receive 10% advance payout.
Already processed sales are skipped.

## Reconcile Sales

Endpoint:
>POST /sales/{sale_id}/reconcile
Description
Updates the sale status.

## Get Wallet Balance
Endpoint:
>GET /users/{user_id}/wallet
Description
Returns the user's current withdrawable balance.

## Withdrawal Money
Endpoint:
>POST /withdrawals
Description
Creates a withdrawal request.
The API checks

>sufficient balance
>one withdrawal in 24 hours

before processing.

## Recover Failed Payout
Endpoint:
>POST /withdrawals/{withdrawal_id}/recover
Description
Credits the failed payout amount back to the user's wallet.


