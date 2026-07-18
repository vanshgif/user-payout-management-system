User Payout Management System
1. PROBLEM STATEMENT

The User Payout Management System is designed to manage affiliate sales and payouts efficiently.

Every affiliate sale enters the system with a Pending status. While the sale is pending, the user becomes eligible for an Advance Payout equal to 10% of the commission.

Once the sale is reconciled by the administrator, its status changes to either:

# Approved
# Rejected

If approved, the system pays the remaining commission after deducting any advance already paid.

If rejected, the previously paid advance is recovered by deducting it from the user's future payouts.

The system also allows users to withdraw their available balance while enforcing a 24-hour withdrawal restriction and automatically recovers failed payouts.

2. FUNCTIONAL REQUIREMENTS

# Store affiliate sales.

# Calculate advance payouts.

# Prevent duplicate advance payouts.

# Reconcile sales.

# Calculate final payouts.

# Maintain withdrawable balance.

# Restrict withdrawals to one every 24 hours.

# Recover failed payouts.

3. NON-FUNCTIONAL REQUIREMENTS

(HOW THE SYSTEM SHOULD BEHAVE)

//reliability
//consistency
// manatainability
//scalitibity

4. ASSUMPTIONS

#   each sale belongs to one user only
#   advance payout is fixed at 10% only
#   wallet balance cannot become negative


## LLD
LLD

1. Class Diagram
2. Service Layer
3. Sequence Diagrams
4. API Design
5. Business Rules
6. Error Handling
