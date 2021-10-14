A simple example project to test out functionalites of FastAPI's WebSocket's. Main source used for this was an official documentation at https://fastapi.tiangolo.com/advanced/websockets/.

To Create a database, do following:

1. Install a clickhouse client and server with https://clickhouse.com/docs/en/getting-started/install/
2. Create a default user with a password: Ya999888777
3. Activate a clickhouse server with: sudo systemctl start clickhouse-server
4. Activate a clickhouse client with: clickhouse-client --password (with passwowrd being Ya999888777)
5. In your client, create a database: CREATE DATABASE eventlog;
6. Make sure you are working with your database with: USE eventlog;
7. Create a table: CREATE TABLE eventlog (
                                 id UInt64,
                                 message String,
                                 timestamp DateTime)
                            ENGINE = MergeTree() 
                            PRIMARY KEY id 
                            ORDER BY id;

8. Then run an app with: hypercorn main:app --worker-class trio --reload



