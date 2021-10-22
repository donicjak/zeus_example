# Zeus_example Project


**Version 1.0.0.**

A simple example project to test out functionalites of FastAPI's WebSocket's. Main source used for this was an official [documentation](https://fastapi.tiangolo.com/advanced/websockets/) 
The project also stores data into a database created with [clickhouse](https://clickhouse.com/)

## Usage

1. Install a clickhouse client and server with the help of [documentation] (https://clickhouse.com/docs/en/getting-started/install/)
2. Create a default user without a password.
3. Set your enviromental variables for database connection. export database_name=VALUE; export user_name=VALUE; export host_name=VALUE
4. Run command make database to activate server and create a database with a table
5. Run command make runserver to run an application

## Contributors

- Jakub Donič <https://github.com/donicjak>
