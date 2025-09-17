# Personal Finances Module for Odoo 16

This module provides a comprehensive solution for managing personal finances directly within Odoo. It allows users to track their income and expenses, categorize them with tags, and analyze their financial activity through intuitive reports.

## Key Features

- **Unified Transactions**: Both income and expenses are managed as single `Transaction` objects, simplifying the data model.
- **Smart Amount Handling**: Expense amounts are automatically stored as negative values, ensuring that totals and balances are always calculated correctly in list views.
- **Categorization with Tags**: Create and assign custom tags to each transaction. Tags can be specific to income or expenses, ensuring you only see relevant tags when creating a transaction.
- **Multi-User Privacy**: The module is built for multiple users. Each user can only see and manage their own financial transactions, thanks to built-in record rules.
- **Notes**: Add detailed notes to any transaction for future reference.
- **Reporting & Analysis**:
  - **Transaction List**: A clear list view of all your transactions, which can be filtered and is grouped by month by default.
  - **Income Analysis**: A bar chart report showing total income grouped by tag.
  - **Expense Analysis**: A bar chart report showing total expenses grouped by tag. A calculated field is used to display the absolute values, ensuring the chart is rendered correctly.

## Installation

1.  Copy the `personal_finances` folder into your Odoo `addons` directory.
2.  Navigate to the **Apps** menu in your Odoo instance.
3.  Click on **Update Apps List** (developer mode must be enabled).
4.  Search for "Personal Finances" in the app list.
5.  Click the **Install** button.

## Configuration

1.  **User Access**: To grant a user access to the module, you must add them to the appropriate security group.
    - Go to `Settings > Users & Companies > Users`.
    - Select the user you want to give access to.
    - Under the "Access Rights" tab, find the **Personal Finances** section and select **User**.
    - The user will need to reload the page to see the new "Personal Finances" menu.

2.  **Create Tags**: Before you start creating transactions, it is recommended to set up your tags.
    - Go to `Personal Finances > Configuration > Tags`.
    - Create new tags, giving each a name and assigning its type (`Income` or `Expense`).

## Usage

- **Create a Transaction**:
  - Navigate to `Personal Finances > Transactions`.
  - Click **Create**.
  - Fill in the description, select the type (`Income` or `Expense`), and enter the amount (always as a positive number; the system will adjust it if it's an expense).
  - Assign one or more tags. The list of available tags will be automatically filtered based on the transaction type you selected.
  - Save the transaction.

- **Analyze Your Finances**:
  - Go to `Personal Finances > Income Analysis` to see a graph of your income sources.
  - Go to `Personal Finances > Expense Analysis` to see a graph of where your money is going.
  - Use the filters in the search bar on any view to narrow down data by date, tag, or other criteria.

---

Developed by: `Your Name`
