# genai-sql-assistant
# Title
Building a Generative AI-Powered SQL Assistant using Streamlit, LangChain, and MySQL

# Overview
This project demonstrates how to build a Generative AI SQL Assistant that converts natural language questions into SQL queries, executes them against a MySQL database, and displays the results in Streamlit interface.

# Technologies Used

- Streamlit – For building the web-based UI
- LangChain – To interact with OpenAI’s LLM in a modular and structured way
- OpenAI API – To generate SQL queries from natural language prompts
- MySQL – For data storage and querying
- Python (pymysql, pandas, dotenv) – For backend logic and database connection

# Key Features
- Integrated OpenAI API to convert user questions into SQL queries
- Dynamic schema detection – fetches table structures from MySQL automatically (no hardcoding)
- Role-based access control:
    - Viewer: Can only run SELECT queries
    - Admin: Can run full SQL (e.g., INSERT, UPDATE, DELETE)
- Query history tracking – previously run queries and sample results are stored and viewable
- Simple and clean Streamlit UI for interactive SQL generation and execution
- Allows Admin users to download query results as a .csv file.

# Prerequisites

- OpenAI API key
- MySQL database with sample data
- Python 3.9+
- Packages: streamlit, langchain, langchain_openai, pymysql, python-dotenv, pandas

# How to Run

# 1. Clone the repo and navigate
- git clone https://github.com/veerababu558/genai-sql-assistant.git
- cd sql-genai-assistant

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set environment variables in .env file
OPENAI_API_KEY=your-key
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your-password
DB_NAME=your-database

# 4. Run the app
streamlit run MySQLQueryGenerator.py

Below is the Project structure
The .env file is not included in the reposiorty due to GitHub security restrictions.

![](https://github.com/veerababu558/genai-sql-assistant/blob/main/Screenshot%202025-06-16%20202219.png)
     
# Example Queries to Try

- "Show total sales per customer"
- "List all products with price above $100"
- "Which customers made more than 5 orders?"

  Below is a screenshot showing the result for the query "Show total sales per customer" executed by a user with the Viewer role.

  ![](https://github.com/veerababu558/genai-sql-assistant/blob/main/Screenshot%202025-06-16%20171243.png)

  Below is a screenshot showing an error when the delete query is executed by  "Viewer" role.
  
  ![](https://github.com/veerababu558/genai-sql-assistant/blob/main/Screenshot%202025-06-16%20171425.png)
  
  Below is a screenshot showing the query history tracking.
  
  ![](https://github.com/veerababu558/genai-sql-assistant/blob/main/Screenshot%202025-06-16%20171547.png)

  Below is a screenshot showing the CSV download option for "Admin" role
  
  ![](https://github.com/veerababu558/genai-sql-assistant/blob/main/Screenshot%202025-06-16%20171721.png)

  Below is a screenshot showing an error encountered by by "Admin" role when executing a delete query.  Application attempted to delete data from a table,but it failed due to constraints imposed on the table.
  
  ![](https://github.com/veerababu558/genai-sql-assistant/blob/main/Screenshot%202025-06-16%20171810.png)

# Further enhancments 
  - Deploy the application using AWS cloud native services such as EC2,RDS, and App runner.
  - Implement user authentication  using AWS Cognito.
  - Configure and mange user roles in the database,and dyanmically apply roles based on the loggined-in user.

# Acknowledgements

As part of my learning in Generative AI , I  built this project using Langchain,MySQL and Streamlit. Certain parts of the code and structure were guided with the help of ChatGPT.

I have enhanched certain functionlaties such as query history,dynamic schema detection,role based access control,SQL query saftey validation, and CSV export.
