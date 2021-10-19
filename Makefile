target:  make-database make-runserver lint

make-database:
	sudo systemctl start clickhouse-server
	clickhouse-client --query "CREATE DATABASE $(database_name);"
	clickhouse-client -d $(database_name) --query "CREATE TABLE $(database_name) ( message String, timestamp DateTime('UTC'), IP UInt32) ENGINE = MergeTree() ORDER BY timestamp;"

make-runserver:
	hypercorn main:app --worker-class trio --reload

lint:
	flake8 ./main.py