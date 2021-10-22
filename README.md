# Zeus_example Project


**Version 1.0.0.**

A simple example project to test out functionalites of FastAPI's WebSocket's. Main source used for this was an official [documentation](https://fastapi.tiangolo.com/advanced/websockets/) 
The project also stores data into a database created with [clickhouse](https://clickhouse.com/)

## Usage

Install a clickhouse client and server with the help of [documentation](https://clickhouse.com/docs/en/getting-started/install/)

Create a user account with a name and password of your choice.

Set your enviromental variables for database connection. 
```export database_name=VALUE``` for the name of your database
```export user_name=VALUE``` for the user name you have chosen
```export host_name=VALUE``` for the host name you've set.
Run command ```make database``` to activate server and create a database with a table
Run command ```make runserver``` to run an application

## Contributors

- Jakub Donič <https://github.com/donicjak>
