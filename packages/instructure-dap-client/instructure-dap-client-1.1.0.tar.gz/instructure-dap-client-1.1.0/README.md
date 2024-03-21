# Data Access Platform CLI & Client Library

Data Access Platform (DAP) acts as a single source of data for analytics at Instructure. It provides efficient access to data collected across various educational products in bulk with high fidelity and low latency, adhering to a canonical data model.

The DAP CLI and Client Library is a Python wrapper around the DAP Query API, allowing you to fetch an initial snapshot and incremental changes, or initialize a supported database and keep it synchronized with data in DAP.

## Operating System and Database Support

The DAP CLI and Client Library currently are tested and supported on the following:

Supported on the following OS:

-   Ubuntu 22 provider supported versions with x86_64 and AArch64 CPU architectures
-   Windows 11
-   MacOS 14

Support the following database integrations:

-   PostgreSQL 12.17 or above, 16.1 or above
-   MySQL 5.7, 8.2 or later

## Installation

The client library is available as a Python package in the [Python Package Index (PyPI)](https://pypi.org/project/instructure-dap-client/). You can install it using the `pip` package manager:

```sh
pip install instructure-dap-client
```

In case you are using the library to synchronize data with a PostgreSQL database, you need to install the package using the following command, specifying `postgresql` as an extra feature:

```sh
pip install "instructure-dap-client[postgresql]"
```

Or in case you are using the library to synchronize data with a MySQL database, you need to install the package using the following command, specifying `mysql` as an extra feature:

```sh
pip install "instructure-dap-client[mysql]"
```

Note: if you miss installing an extra feature, the library will not be able to synchronize data with a database, and you may get an error message similar to the following (in case of PostgreSQL):

```
ERROR - missing dependency: `asyncpg`; you may need to run `pip install pysqlsync[postgresql]`
```

## Getting started

Accessing DAP API requires a URL to an endpoint, and a client ID and secret pair. Further details on how to obtain these can be found in the [Instructure API Gateway documentation](https://api-gateway.instructure.com/doc/). Once obtained, they can be set as environment variables (recommended), or passed as command-line arguments:

### Use environment variables for authentication

First, configure the environment with what you have in your setup instructions. Use the `export` command on UNIX-like operating systems such as Linux or macOS:

```sh
export DAP_API_URL=https://api-gateway.instructure.com
export DAP_CLIENT_ID=us-east-1#0c59cade-...-2ac120002
export DAP_CLIENT_SECRET=xdEC0lI...4X4QBOhM
```

Alternatively, use the `set` command in the Windows command line:

```bat
set DAP_API_URL=https://api-gateway.instructure.com
set DAP_CLIENT_ID=us-east-1#0c59cade-...-2ac120002
set DAP_CLIENT_SECRET=xdEC0lI...4X4QBOhM
```

With environment variables set, you can issue `dap` commands directly:

```sh
dap incremental --namespace canvas --table accounts --since 2022-07-13T09:30:00+02:00
```

### Use command-line for authentication

Unless you set environment variables, you need to pass endpoint URL and API key to the `dap` command explicitly:

```sh
dap --base-url https://api-gateway.instructure.com --client-id=us-east-1#0c59cade-...-2ac120002 --client-secret=xdEC0lI...4X4QBOhM incremental --namespace canvas --table accounts --since 2022-07-13T09:30:00+02:00
```

## Command-line usage

Invoking the command-line utility with `--help` shows usage, required and optional arguments:

```sh
dap --help
dap incremental --help
dap snapshot --help
dap list --help
dap schema --help
dap initdb --help
dap syncdb --help
dap dropdb --help
```

## Common use cases

If you are a first-time user of DAP client library, it's best to start with two high-level commands of the CLI (command-line interface): `initdb` and `syncdb`. `initdb` fetches the data stored in DAP and replicates them in a database table that you control. It takes care of authenticating with DAP, fetching data schema, creating a database table, starting a snapshot query, monitoring job progress, downloading data, and inserting records into the table. Subsequently, `syncdb` helps keep the database table up-to-date with the data in DAP. As in the case of `initdb`, `syncdb` manages all the details of verifying the data schema, altering database table structure (if necessary), getting the right data and inserting, updating or deleting the corresponding database table records.

### Obtain a full snapshot of a table in a database or data warehouse

The command-line utility is capable of automatically copying a full table snapshot to a database table with the `initdb` command. Along with the parameters `--table` and `--namespace`, you have to specify your target database with a connection string using the `--connection-string` parameter.

Typically, the connection string looks as follows:

```sh
dialect://username:password@host:port/database
```

Dialect is the database protocol dialect such as `postgresql`. The parameter `port` is optional, if omitted, the default port for the given dialect is assumed (e.g. `5432` in the case of `postgresql`).

The dialects the library supports are `postgresql` and `mysql`.

Examples:

```sh
postgresql://scott:password@server.example.com:5432/testdb
postgresql://scott:password@server.example.com/testdb
```

```sh
mysql://scott:password@server.example.com:3306/testdb
mysql://scott:password@server.example.com/testdb
```

The examples above use the database host `server.example.com`. If your database server is running on the same machine where DAP client library is executing, you would typically pass `localhost` as the database host.

> **_NOTE:_** The connection string is parsed as a URL compliant with RFC 3986. This means that the password part of the connection string is treated as a URL component and must be URL-encoded (a.k.a. percent-encoded) if it contains characters that are treated specially in URLs.
>
> For example if the password is `<?Your:Strong@Pass/w0rd>`, the connection string would look like this:
>
> ```none
> postgresql://scott:%3C%3FYour%3AStrong%40Pass%2Fw0rd%3E@server.example.com:5432/testdb
> ```
>
> On Windows each `%` character in the password must be doubled to be properly escaped, so the connection string would look like this:
>
> ```none
> postgresql://scott:%%3C%%3FYour%%3AStrong%%40Pass%%2Fw0rd%%3E@server.example.com:5432/testdb
> ```

Example for a complete `initdb` command:

```sh
dap initdb --connection-string postgresql://scott:password@server.example.com/testdb --namespace canvas --table accounts
```

The tool automatically fetches the schema and the data from the DAP API, connects to your database, creates the necessary table based on the published schema and inserts the downloaded data into the created table.

If the target database already has a table with same name as the table whose snapshot is about to be obtained, an error is triggered.

Please note that the tool does not support type juggling. Data types specified in the schema obtained from the DAP API must be strictly adhered to during table creation and data insertion. Any attempt to manipulate or convert data types in a way that deviates from the schema will result in errors being thrown.

### Synchronize data with a table in a database or data warehouse

After obtaining a full table snapshot with `initdb`, you can keep it up to date using the `syncdb` command. This replicates the inserts, updates and deletes that took place in the data source. The `syncdb` command has the same parameters as `initdb`. The tool automatically gets an incremental update from the DAP API, connects to your database and applies the incremental update to the target table. All this happens in one atomic transaction so in case of an error you retain consistent data in your database. Only database tables previously created by `initdb` can be synchronized with `syncdb`.

Example:

```sh
dap syncdb --connection-string postgresql://scott:password@server.example.com/testdb --namespace canvas --table accounts
```

The timestamp used for performing the incremental query on the DAP API is maintained in the `dap_meta` meta-information table together with other data about the synchronized tables. This `dap_meta` table is owned by the DAP client library and should not be dropped or changed.

### Drop a synchronized table in a database or data warehouse

With the `dropdb` command, you can completely drop a table from your database that was previously created with `initdb`. An error is triggered if the given table does not exist in the target database.

Example:

```sh
dap dropdb --connection-string postgresql://scott:password@server.example.com/testdb --namespace canvas --table accounts
```

This command not only drops the specified table from the target database but also removes meta-information used for synchronization.

### Use environment variables for database connection

You can (and in most cases, should) configure the database connection string as an environment variable:

```sh
export DAP_CONNECTION_STRING=postgresql://scott:password@server.example.com/testdb
```

As previously, instead of the the `export` command on UNIX-like operating systems such as Linux or macOS, Windows users should invoke the `set` command.

With environment variables set, you can issue `initdb`, `syncdb` and `dropdb` commands directly without explicitly passing your database credentials to the terminal:

```sh
dap initdb --namespace canvas --table accounts
dap syncdb --namespace canvas --table accounts
dap dropdb --namespace canvas --table accounts
```

### Chain a snapshot query with an incremental query

Usually, you should prefer initializing and synchronizing a database or data warehouse with the high-level commands `initdb` and `syncdb`. However, if your database engine is not supported, or you want to transform the (CSV, JSON or TSV) output as part of an ETL process, you may want to use low-level commands `snapshot` and `incremental`.

When you start using DAP, you will definitely want to download a snapshot for the table(s) you need. In the snapshot query response body, you will find a field called `at`, which captures the data lake state at a point in time that the snapshot corresponds to. Copy the timestamp into the `since` field of an incremental query request. This will guarantee that you have chained the two queries and will not miss any data.

Note that if a table has not received updates for a while (e.g. user profiles have not changed over the weekend), the value of `at` might be well behind current time.

### Chain an incremental query with another

To fetch the most recent changes since a previous incremental query, chain the next request to the previous response using `since` and `until`. The `until` of a previous response becomes the `since` of the next request. The `until` of the next request should typically be omitted, it is automatically populated by DAP API. This allows you to fetch the most recent changes for a table. If a table has not received updates for a while, timestamps you see in the response may lag behind current time.

For example, suppose you submit an incremental query job `#82`, and receive a response whose `until` is `2021-07-28T19:00`. You can then pass `2021-07-28T19:00` as the value for `since` in your next incremental query job `#83`. Job `#83` would then return `2021-07-28T19:00` as the value of `since` (the exact value you submitted), and might return `2021-07-28T21:00` as `until` (the latest point in time for which data is available).

If you choose to fill in `until` in a request (which is not necessary in most cases), its value must be in the time range DAP has data for. Otherwise, your request is rejected.

### Get the list of tables available for querying

The `list` command will return all table names from a certain namespace.

### Download the latest schema for a table

The schema endpoint returns the latest schema of a table as a [JSON Schema](https://json-schema.org/) document. The `schema` command enables you to download the schema of a specified table as a JSON file.

### Configure logging

The default log level is `info` and messages are printed to the console. You can change the log level by adding the `--loglevel` parameter to the `dap` command. The `--logfile` parameter allows you to save the log messages to a file.

```sh
dap --loglevel debug --logfile dap.log initdb --namespace canvas --table accounts
```

## Code examples

While basic functionality of the DAP client library is exposed over its command-line interface (CLI), more advanced functionality requires interacting with classes and functions defined in the module `dap.api`. This enables seamless integration into workflow management platforms like Apache Airflow.

DAP client library is following the [asynchronous programming paradigm](https://docs.python.org/3/library/asyncio.html), and makes use of the new Python keywords `async` and `await`. The examples below have to be executed in an asynchronous context. You can [enter an asynchronous context](https://docs.python.org/3/library/asyncio-runner.html#running-an-asyncio-program) by invoking `asyncio.run`. By default, a Python script runs in a synchronous context; you must wrap the examples below into an `async` function, or you will get a syntax error.

First, we need to instantiate the `DAPClient` class:

```python
import os
from dap.api import DAPClient
from dap.dap_types import Credentials

base_url: str = os.environ["DAP_API_URL"]
client_id: str = os.environ["DAP_CLIENT_ID"]
client_secret: str = os.environ["DAP_CLIENT_SECRET"]

credentials = Credentials.create(client_id=client_id, client_secret=client_secret)
async with DAPClient(base_url, credentials) as session:
    ...
```

However, `DAPClient` can automatically extract the value of these parameters from the above environment variables, allowing us to write:

```python
async with DAPClient() as session:
    ...
```

Note that `DAPClient` uses an asynchronous context manager. Keywords such as `async with` are permitted only in an asynchronous context. We can enter such a context by invoking `asyncio.run(my_function(arg1, arg2, ...))`.

Let's explore a few common use cases with `DAPClient`.

### Obtaining the latest schema

Before we obtain data, we need to get the latest schema of a table. The following example retrieves the JSON schema of the table `accounts` in the namespace `canvas` as a JSON schema object. A JSON object is a recursive Python data structure whose outermost layer is a Python `dict` whose keys are strings (type `str`) and values are JSON objects. We can use the Python package [jsonschema](https://python-jsonschema.readthedocs.io/en/stable/) to validate data against this JSON schema.

```python
from dap.api import DAPClient

async with DAPClient() as session:
    schema = await session.get_table_schema("canvas", "accounts")
```

We can also save the schema to a file.

```python
import os
from dap.api import DAPClient

output_directory: str = os.getcwd()
async with DAPClient() as session:
    tables = await session.get_tables("canvas")
    for table in tables:
        await session.download_table_schema("canvas", table, output_directory)
```

### Fetching table data with a snapshot query

In order to get an initial copy of the full table contents, we need to perform a snapshot query. The parameter `format` determines the output data format, including CSV, TSV, JSONL and Parquet. We recommend JSONL or Parquet. For JSONL, each line in the output can be parsed into a JSON object, conforming to the JSON schema returned above.

```python
import os
from dap.api import DAPClient
from dap.dap_types import Format, SnapshotQuery

output_directory = os.getcwd()
async with DAPClient() as session:
    query = SnapshotQuery(format=Format.JSONL, mode=None)
    await session.download_table_data(
        "canvas", "accounts", query, output_directory, decompress=True
    )
```

### Getting latest changes with an incremental query

Once an initial snapshot has been obtained, we need to keep the data synchronized with DAP. This is possible with incremental queries. The following, more complex example gets all changes since a specified `since` timestamp, and saves each data file on the server to an output file in the local filesystem. The `last_seen` timestamp is typically the `until` returned by a previous incremental query.

```python
import os
from datetime import datetime, timezone
from urllib.parse import ParseResult, urlparse

import aiofiles

from dap.api import DAPClient
from dap.dap_types import Format, IncrementalQuery

# timestamp returned by last snapshot or incremental query
last_seen = datetime(2023, 2, 1, 0, 0, 0, tzinfo=timezone.utc)

async with DAPClient() as session:
    query = IncrementalQuery(
        format=Format.JSONL,
        mode=None,
        since=last_seen,
        until=None,
    )
    result = await session.get_table_data("canvas", "accounts", query)
    resources = await session.get_resources(result.objects)
    for resource in resources.values():
        components: ParseResult = urlparse(str(resource.url))
        file_path = os.path.join(
            os.getcwd(), "data", os.path.basename(components.path)
        )
        async for stream in session.stream_resource(resource):
            async with aiofiles.open(file_path, "wb") as file:
                # save gzip data to file without decompressing
                async for chunk in stream.iter_chunked(64 * 1024):
                    await file.write(chunk)
```

### Replicating data to a database

Earlier sections have shown how to obtain the latest schema, fetch data with a snapshot query, or get the latest changes with an incremental query. These are low-level operations that give you full control over what you do with the data.

However, in most cases we want high-level operations that ensure our database (either running locally or in the cloud) is synchronized with the data in DAP, without paying attention to specifics of data transfer. This is possible with two operations that

1. initialize a database, and
2. synchronize a database with the data in DAP.

In order to replicate data in DAP locally, we must first initialize a database:

```python
from dap.api import DAPClient
from dap.integration.database import DatabaseConnection
from dap.replicator.sql import SQLReplicator

connection_string: str = "postgresql://scott:password@server.example.com/testdb"
db_connection = DatabaseConnection(connection_string)
async with DAPClient() as session:
    await SQLReplicator(session, db_connection).initialize(namespace, table_name)
```

Initialization creates a database schema for the DAP namespace, and a corresponding database table for each DAP table. In addition, it creates a _meta-table_, which is a special database table that holds synchronization information, e.g. the last time the data was synchronized with DAP, and the schema version that the locally stored data conforms to. Finally, it issues a snapshot query to DAP API, and populates the database table with output returned by the snapshot query.

### Synchronizing data with a database

Once the table has been initialized, it can be kept up to date using the synchronize operation:

```python
db_connection = DatabaseConnection(connection_string)
async with DAPClient() as session:
    await SQLReplicator(session, db_connection).synchronize(namespace, table_name)
```

This inspects the information in the meta-table, and issues an incremental query to DAP API with a `since` timestamp corresponding to the last synchronization time. Based on the results of the incremental query, it inserts new records, updates existing records, and deletes records that have been added to, updated in, or removed from the DAP service.

If the local schema version in the meta-table is identical to the remote schema version in DAP, inserting, updating and deleting records proceeds normally. However, if there is a mismatch, the table structure of the local database has to evolve to match the current structure of the data in DAP. This includes the following schema changes in the back-end:

-   A new required (a.k.a. non-nullable) field (column) is added. The new field has a default value assigned to it in the schema.
-   A new optional (a.k.a. nullable) field (column) is added to a table.
-   A new enumeration value is added to an existing enumeration type.
-   A new enumeration type is introduced.
-   A field (column) is removed from a table.

Behind the scenes, the client library uses SQL commands such as `ALTER TABLE ... ADD COLUMN ...` or `ALTER TYPE ... ADD VALUE ...` to replicate schema changes in DAP in our local database. If the JSON schema change couldn't be mapped to a series of these SQL statements, the client library wouldn't be able to synchronize with DAP using incremental queries, and would have to issue an expensive snapshot query.

Once the local database table structure has been reconciled with the new schema in DAP, and the meta-table has been updated, data synchronization proceeds normally with insert, update and delete SQL statements.

### Dropping data from a database

If the table is no longer needed, it can be dropped from the database using the following code:

```python
db_connection = DatabaseConnection(connection_string)
await SQLDrop(db_connection).drop(namespace, table_name)
```

### Configure log level for debugging

The client library uses the Python logging module to log messages. The default log level is `INFO`. You can change the log level by adding the following code to the beginning of your script. It'll also add the timestamp to each log message.

```python
import logging

# ... other imports

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("dap")
logger.setLevel(logging.DEBUG)
logger.propagate = False
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(handler)
```
