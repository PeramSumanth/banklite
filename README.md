"# banklite" 
BankLite – Console Banking System 

Objective: 

Simulate a basic bank account management system where users can open accounts, 
deposit/withdraw money, check balances, and store transaction history using OOP and logic 
fundamentals. 


Key Features: 
●  Create account 
●  Deposit / Withdraw funds 
●  View balance 
●  View transaction history 
●  Save/load data to/from  bank.json 

Modules & Class Design: 

1.  Account  class 
Attributes: 
●  id 
●  name 
●  balance 
●  transactions (List of strings) 
Methods: 
●  deposit() 
●  withdraw() 
●  get_balance() 
●  get_history() 
●  to_dict(), from_dict() 

2.  Bank  class 
Attributes: 
●  accounts (List of Account objects) 
Methods: 
●  create_account() 
●  find_account_by_id() 
●  deposit_to_account() 
●  withdraw_from_account() 
●  show_account_details() 
●  save_to_file(), load_from_file() 


Tasks to Implement: 
1.  Create Account 
Input name, assign ID, start balance 

2.  Deposit / Withdraw 
Validate input, update balance 
Log transaction string 

3.  View Balance & History 
Show current balance 
Display past actions 

4.  Save & Load 
Store in  bank.json 


Evaluation Points: 

●  Inheritance not needed but encouraged for extension 

●  Clear method structure for money handling 

●  Input and balance validation 

●  File storage and readable transaction logs 
