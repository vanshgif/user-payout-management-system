# 🚀 User Payout Management System

A backend system built using **FastAPI** and **PostgreSQL** to manage affiliate user payouts, wallet balances, and withdrawals.

This project simulates the payout workflow of affiliate platforms like **CashKaro**, **EarnKaro**, or cashback/reward systems where users earn commissions from successful sales.

---

# 📌 Features

- User Management
- Sale Management
- Wallet Management
- Advance Payout Processing
- Final Payout Processing
- Sale Rejection Adjustment
- Withdrawal Management
- 24-Hour Withdrawal Restriction
- Failed Withdrawal Refund
- Exception Handling
- Request Logging Middleware
- Interactive Swagger API Documentation

---

# 🛠 Tech Stack

- FastAPI
- Python 3.11+
- PostgreSQL
- SQLAlchemy ORM
- Pydantic
- Uvicorn

---

# 📁 Project Structure

```
app/
│
├── core/
│   └── enums.py
│
├── database.py
├── config.py
├── main.py
│
├── models/
│   ├── user.py
│   ├── sales.py
│   ├── payout.py
│   └── withdrawal.py
│
├── schemas/
│   ├── user.py
│   ├── sale.py
│   ├── payout.py
│   └── withdrawal.py
│
├── services/
│   ├── user_service.py
│   ├── sale_service.py
│   ├── payout_service.py
│   ├── withdrawal_service.py
│   └── wallet_service.py
│
├── routes/
│   ├── user_routes.py
│   ├── sale_routes.py
│   ├── payout_routes.py
│   └── withdrawal_routes.py
│
├── exceptions/
│   ├── custom_exceptions.py
│   └── handlers.py
│
└── middleware/
    └── logging_middleware.py
```

---

# 🗄 Database Schema

## Users

| Field | Type |
|---------|------|
| id | UUID |
| username | String |
| email | String |
| wallet_balance | Decimal |

---

## Sales

| Field | Type |
|---------|------|
| id | UUID |
| user_id | UUID |
| brand | String |
| earning | Decimal |
| status | Pending / Approved / Rejected |
| advance_paid | Boolean |

---

## Payouts

| Field | Type |
|---------|------|
| id | UUID |
| user_id | UUID |
| sale_id | UUID |
| amount | Decimal |
| payout_type | Advance / Final / Adjustment |
| status | Success |

---

## Withdrawals

| Field | Type |
|---------|------|
| id | UUID |
| user_id | UUID |
| amount | Decimal |
| status | Pending / Success / Failed / Cancelled |
| created_at | Timestamp |
| updated_at | Timestamp |

---

# 💼 Business Rules

### 1. Sale Creation

Every new sale is created with **Pending** status.

---

### 2. Advance Payout

When advance payouts are processed:

- User receives **10%** of the sale earning.
- Wallet balance increases.
- Sale is marked as advance paid.

---

### 3. Sale Approval

When a sale is approved:

- Remaining **90%** is credited.
- Final payout record is created.

---

### 4. Sale Rejection

If advance payout was already processed:

- 10% advance is recovered.
- Wallet is debited.
- Adjustment payout is created.

---

### 5. Withdrawals

Users can withdraw only if:

- Wallet has sufficient balance.
- No withdrawal has been made within the last **24 hours**.

---

### 6. Failed Withdrawals

If a withdrawal fails or is cancelled:

- Amount is automatically refunded to the user's wallet.

---

# 🔗 API Endpoints

## Users

| Method | Endpoint |
|---------|----------|
| POST | /users |
| GET | /users/{id} |

---

## Sales

| Method | Endpoint |
|---------|----------|
| POST | /sales |
| PATCH | /sales/{sale_id}/status |

---

## Payouts

| Method | Endpoint |
|---------|----------|
| POST | /payouts/process-advance |

---

## Withdrawals

| Method | Endpoint |
|---------|----------|
| POST | /withdrawals |
| GET | /withdrawals/{id} |
| GET | /withdrawals/user/{user_id} |
| PATCH | /withdrawals/{id}/status |

---

# ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/vanshgif/user-payout-management-system.git
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure your `.env` file:

```
DATABASE_URL=postgresql://username:password@localhost:5432/payout_db
```

Run the application:

```bash
uvicorn app.main:app --reload
```

---

# 📖 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 🧪 Testing

The following business flows were tested successfully:

- Create User
- Create Sale
- Process Advance Payout
- Approve Sale
- Reject Sale
- Wallet Credit
- Wallet Debit
- Create Withdrawal
- Withdrawal Cooldown Validation
- Failed Withdrawal Refund
- Exception Handling

---

# 🚀 Future Improvements

- JWT Authentication
- Role-Based Access Control
- Docker Support
- Alembic Database Migrations
- Unit & Integration Tests
- Background Job Processing
- Redis Caching
- CI/CD Pipeline

---

# 👨‍💻 Author

**Vansh Vohra**

B.Tech – Artificial Intelligence & Data Science

Backend Developer | Python | FastAPI | PostgreSQL