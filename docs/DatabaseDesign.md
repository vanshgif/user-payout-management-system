# Database Design
The system uses a relational database (PostgreSQL) to store users, affiliate sales, payouts, and withdrawal records.

The database is designed to maintain transactional consistency, prevent duplicate payouts, and accurately track every financial transaction.

## Entities

The system consists of four primary entities:

- User
- Sale
- Payout
- Withdrawal

## users
//contains columns like id, username, email, wallet_balance, created_at

Every sale belongs to a user.

Every payout belongs to a user.

Every withdrawal belongs to a user.

Users are the parent entity.

## Sales
//contains columns like id, user_id, brand, earning, status, advance_paid, created_at, updated_at

contains advance_paid so that even if he scheduler runs twice, it should not pay 10% again and again.

## payouts
// contains id, user_id, sale_id, payout_type, amount, status, created_at

## withdrawals
// contains coluns like id, user_id, amount, status, requested_at, completed_at


        Entity relationships:
User (1)
   │
   ├──────────────< Sale (Many)
   │
   ├──────────────< Payout (Many)
   │
   └──────────────< Withdrawal (Many)

Sale (1)
   │
   └──────────────< Payout (Many)

