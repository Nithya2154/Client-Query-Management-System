# Client-Query-Management-System
# OVERVIEW
This project is a role-based web application built using Streamlit and PostgreSQL.
It provides a simple login system with two roles:

Client

Support Team

Clients can submit support queries, and the Support Team can view, filter, and close those queries through a dashboard.

# FEATURES

Authentication

Login page with username, password, and role selection

Passwords validated using SHA-256 hashing

Session-based navigation using Streamlit session state

# Client Module

Submit support queries with:

Email ID

Mobile number

Query heading

Query description

Queries are stored in PostgreSQL

Query status initialized as Open

# Support Team Module

View all client queries in a dashboard

Filter queries by status (All / Opened / Closed)

View summary statistics:

Total queries

Open queries

Closed queries

Close queries by Query ID

Automatic timestamping for query closure

# Database Integration

PostgreSQL used as backend database

psycopg2 used for database connectivity

# PROJECT STRUCTURE

app.py

Main entry point

Handles login, role-based routing, and session state

client.py

Client interface

Query submission form

Writes data to database

support_team.py

Support dashboard

Displays, filters, and updates queries

database.py

PostgreSQL connection handler

requirements.txt

List of required Python dependencies

# DATABASE REQUIREMENTS

PostgreSQL database configuration (example from code):

Host: localhost

Database name: support

User: postgres

Port: 5432

Required tables (must exist before running the app):

users

username (TEXT, PRIMARY KEY)

hashed_password (TEXT)

role (TEXT)

client_queries

query_id (SERIAL, PRIMARY KEY)

email_id (TEXT)

mobile_number (TEXT)

query_heading (TEXT)

query_description (TEXT)

status (TEXT)

query_created_time (TIMESTAMP)

query_closed_time (TIMESTAMP, nullable)

# INSTALLATION

Clone the repository
git clone <repository-url>
cd <project-folder>

Create and activate a virtual environment (recommended)

Install dependencies
pip install -r requirements.txt

Configure PostgreSQL

Create the database and required tables

Update database credentials in database.py if needed

# RUNNING THE APPLICATION

Run the Streamlit app using:

streamlit run app.py

The application will open in your browser.

# SECURITY NOTES

Passwords are hashed using SHA-256 before validation

Database credentials are hardcoded (for demo purposes only)

For production use:

Use environment variables

Enable stronger authentication and access control

TECHNOLOGIES USED

Python

Streamlit

PostgreSQL

psycopg2

Pandas

# USE CASES

Internal helpdesk systems

Learning project for Streamlit + database integration

Role-based CRUD applications
