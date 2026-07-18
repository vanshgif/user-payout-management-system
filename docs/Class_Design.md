CLASS DESIGN

## User Class

| Attribute      | Type    |
| -------------- | ------- |
| id             | UUID    |
| username       | String  |
| email          | String  |
| wallet_balance | Decimal |


>Maintain user information.
>Store the current wallet balance.
>Associate sales, payouts, and withdrawals with the user.

## Sale Class

| Attribute    | Type    |
| ------------ | ------- |
| id           | UUID    |
| user_id      | UUID    |
| brand        | String  |
| earning      | Decimal |
| status       | Enum    |
| advance_paid | Boolean |

>Store affiliate sale details.
>Track sale status.
>Prevent duplicate advance payouts.

## Payout Class

| Attribute   | Type    |
| ----------- | ------- |
| id          | UUID    |
| user_id     | UUID    |
| sale_id     | UUID    |
| payout_type | Enum    |
| amount      | Decimal |
| status      | Enum    |

>Record all payout transactions.
>Store advance payouts.
>Store final payouts.
>Store recovery adjustments.

## Withdrawal Class

| Attribute | Type    |
| --------- | ------- |
| id        | UUID    |
| user_id   | UUID    |
| amount    | Decimal |
| status    | Enum    |

>Store withdrawal requests.
>Track withdrawal status.
>Maintain withdrawal history.