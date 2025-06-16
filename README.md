# genai-sql-assistant
# Title
Building a Generative AI-Powered SQL Assistant using Streamlit, LangChain, and MySQL

# Overview
This project demonstrates how to build a Generative AI SQL Assistant that converts natural language questions into SQL queries, executes them against a MySQL database, and displays the results in a user-friendly Streamlit interface.

# Technologies Used

Streamlit – For building the web-based UI
LangChain – To interact with OpenAI’s LLM in a modular and structured way
OpenAI API – To generate SQL queries from natural language prompts
MySQL – For data storage and querying
Python (pymysql, pandas, dotenv) – For backend logic and database interaction

# Key Features
✅ Integrated OpenAI API to convert user questions into SQL queries
✅ Dynamic schema detection – fetches table structures from MySQL automatically (no hardcoding)
✅ Role-based access control:

    Viewer: Can only run safe SELECT queries
    Admin: Can run full SQL (e.g., INSERT, UPDATE, DELETE)
✅ Query history tracking – previously run queries and sample results are stored and viewable
✅ Simple and clean Streamlit UI for interactive SQL generation and execution

# Prerequisites

OpenAI API key
MySQL database with sample data
Python 3.9+
Packages: streamlit, langchain, langchain_openai, pymysql, python-dotenv, pandas

# How to Run

# 1. Clone the repo and navigate
git clone https://github.com/your-username/sql-genai-assistant.git
cd sql-genai-assistant

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

📦sql-genai-assistant/
 ┣ 📄 MySQLQueryGenerator.py
 ┣ 📄 requirements.txt
 ┣ 📄 .env
 ┗ 📁 sample_data/
     ┣ 📄 create_tables.sql
     ┗ 📄 insert_data.sql
     
# Example Queries to Try

Show total sales per customer
List all products with price above $100
Which customers made more than 5 orders?
