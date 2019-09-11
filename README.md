## How to Run:
- Make the file **config.json** with following parameters. (Sample given)
    ```
    {
        "MONGO_HOST": "mongo-atlas.mongodb.net",
        "USERNAME": "<username>",
        "PASSWORD": "<password>",
        "DATABASE": "<db_name>",
        "COLLECTION": "<collection_in_db>",
        "ADMIN_USER": "<Admin User>",
        "ADMIN_PASSWORD": "<Admin Password>"
    }
    ```
    Admin User and Password is used to authorize the requests.
- Run
    ```
    python webservice.py
    ```
   to start the web server.

## API Docs:
- Headers required:
  - Authorization: `<JWT Token>`

- GET /
  - **DESCRIPTION**: Healthy Point to verify

- GET /authorize/`<username>`/`<password>`
  - **DESCRIPTION**: Get auth token for creating requests.
  - Returns JWT Token.

- GET /getContacts/`<offset>`/`<limit>`/?`<query_params>`
  - **DESCRIPTION**: Fetch the list of contacts based on parameters specified.
  - offset (optional) : Starting point from where the list should be displayed. (Default: 0)
  - limit (optional. If given, offset is required as well.): Total number of items to display. (Default: 10)
  - query_params: Search params to give. For example, **/?email=test1@gmail.com&phone=1111111111** etc. For example,
    ```
    GET getContacts/?email=test1@gmail.com
    GET /getContacts/0/?email=test1@gmail.com
    GET /getContacts/0/2/?email=test1@gmail.com
    ```
  - Returns JSON list of objects.

- POST /createContact
  - **DESCRIPTION**: Create new contact. Throws error if the any contact with same Email ID is already present.
  - **Request Body**: Data to send.
    ```
    {
        "email": "test1@gmail.com",
        "name": "qwerty",
        "phone": "1111111111"
    }
    ```
  - Returns Object ID or error.

- PUT /updateContact/`<id>`
  - **DESCRIPTION**: Update existing contact.
  - **Request Body**: Data to send.
    ```
    {
        "email": "test2@gmail.com",
        "name": "qwerty",
        "phone": "1111111111"
    }
    ```
    Other fields if given are automatically rejected. Basic validations for Email, Name and Phone number is also present. If invalid data, it throws error.
  - id: Object ID to update.

- DELETE /deleteContact/`<id>`
  - **DESCRIPTION**: Delete existing contact.
  - id: Object ID to delete.
