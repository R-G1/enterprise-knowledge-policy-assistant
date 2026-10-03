Your application will be an Enterprise Knowledge & Policy Assistant.

Imagine a company has documents such as:

company_policy.pdf
leave_policy.pdf
security_policy.pdf
employee_handbook.pdf
remote_work_sop.pdf

An employee should be able to ask something like:

"How many days of annual leave can an employee take?"

And instead of the LLM answering from its general knowledge, our system should:

Employee Question
       ↓
Find relevant information in company documents
       ↓
Give that information to the LLM
       ↓
Generate an answer based on those documents
       ↓
Show the source of the answer