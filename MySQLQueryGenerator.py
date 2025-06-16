import os
import pymysql
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import httpx
import pandas as pd


# Load your API key here 

# LLM setup
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# Connect to DB and build schema string
def get_full_schema():
    try:
        conn = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        with conn.cursor() as cursor:
            cursor.execute("SHOW TABLES")
            tables = [row[0] for row in cursor.fetchall()]
            schema_lines = []
            for table in tables:
                cursor.execute(f"DESCRIBE {table}")
                columns = [col[0] for col in cursor.fetchall()]
                schema_lines.append(f"{table}({', '.join(columns)})")
            return "\n".join(schema_lines)
    except Exception as e:
        return f"⚠️ Error loading schema: {e}"

#  SQL generator
def generate_sql(user_question, schema):
    try:
        prompt = f"""
You are an AI that writes SQL queries based on user questions.
Here is the database schema:

{schema}

When writing SQL, always prefix column names with the table name to avoid ambiguity.
User question: {user_question}
Write only the SQL query.
"""
        response = llm([HumanMessage(content=prompt)])
        return response.content.strip()
    except Exception as e:
        return f"⚠️ Error: {e}"

#  SQL safety checker
def is_safe_sql(sql):
    unsafe_keywords = ["delete", "update", "insert", "drop", "alter", "truncate", "replace", "create"]
    return not any(sql.strip().lower().startswith(keyword) for keyword in unsafe_keywords)

# SQL executor
def run_sql_query(sql):
    try:
        conn = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        df = pd.read_sql(sql, conn)
        return df
    except Exception as e:
        return f"⚠️ Failed to execute SQL: {e}"

#  Streamlit UI
st.set_page_config(page_title="GenAI SQL Assistant", layout="wide")
st.title("🧠 GenAI SQL Assistant")

#  Role-based access
role = st.sidebar.selectbox("Select your role", ["viewer", "admin"])
read_only = st.sidebar.checkbox("  Read-Only Mode", value=True if role == "viewer" else False)

#  Query history & latest result
if "query_history" not in st.session_state:
    st.session_state.query_history = []
if "latest_df" not in st.session_state:
    st.session_state.latest_df = None

st.write("Ask a question about your MySQL database. Schema will be fetched dynamically.")
user_input = st.text_input("💬 Enter your question:")

if user_input:
    if role == "viewer" and not read_only:
        st.warning("⚠️ Viewers are restricted to read-only mode.")
    else:
        with st.spinner("🔄 Fetching schema and generating SQL..."):
            schema = get_full_schema()
            if schema.startswith("⚠️"):
                st.error(schema)
            else:
                sql = generate_sql(user_input, schema)
                st.code(sql, language="sql")

                st.subheader(" Executing SQL...")

                if read_only and not is_safe_sql(sql):
                    st.error(" Unsafe SQL detected! Execution blocked (e.g. DELETE, UPDATE, etc.)")
                else:
                    result = run_sql_query(sql)

                    if isinstance(result, pd.DataFrame):
                        st.dataframe(result)
                        st.session_state.latest_df = result  # store for CSV export

                        #  Store to query history
                        st.session_state.query_history.append({
                            "question": user_input,
                            "sql": sql,
                            "rows": result.head(5).to_dict(orient="records")
                        })
                    else:
                        st.error(result)

#  CSV Export
if role == "admin" and st.session_state.latest_df is not None:
    csv = st.session_state.latest_df.to_csv(index=False).encode('utf-8')
    st.download_button("  Download Results as CSV", data=csv, file_name="query_result.csv", mime='text/csv')

#  Show Query History
st.sidebar.header("🕘 Query History")
if st.session_state.query_history:
    for i, entry in enumerate(reversed(st.session_state.query_history), 1):
        with st.sidebar.expander(f"Query #{len(st.session_state.query_history)-i+1}"):
            st.markdown(f"**Q:** {entry['question']}")
            st.code(entry["sql"], language="sql")
            st.write("Sample Rows:")
            st.json(entry["rows"])
else:
    st.sidebar.info("No query history yet.")
