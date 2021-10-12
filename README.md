A simple example project to test out functionalites of FastAPI's WebSocket's. Main source used for this was an official documentation at https://fastapi.tiangolo.com/advanced/websockets/.

To Create a database, do following:

1. Activate your server with clickhouse-server start
2. Activate your client with clickhouse-client
3. In your client, create a database: CREATE DATABASE eventlog;
4. Make sure you are working with your database with: USE eventlog;
5. Create a table: CREATE TABLE eventlog ( id UInt64, message String ) ENGINE = MergeTree() PRIMARY KEY id ORDER BY id;
6. To add a timestamp attribute into a Table do: ALTER TABLE eventlog ADD COLUMN timestamp DateTime;