A simple example project to test out functionalites of FastAPI's WebSocket's. Main source used for this was an official documentation at https://fastapi.tiangolo.com/advanced/websockets/.

To Create a database, do following:

1. Install a clickhouse client and server with https://clickhouse.com/docs/en/getting-started/install/
2. Create a default user without a password.
3. Set your enviromental variables for database connection. export database_name=VALUE; export user_name=VALUE; export host_name=VALUE
4. Run command make make-database to activate server and create a database with a table
5. Run command make make-runserver to run an application



