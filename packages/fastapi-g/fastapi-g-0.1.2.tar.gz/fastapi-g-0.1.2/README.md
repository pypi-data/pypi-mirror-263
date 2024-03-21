CLI generator tool for FastAPI Framework

Only need a json model to generate fastapi.

Generated structures : 
* model
* dto
* service
* route
* repository (need enhancement)
* main

Here is json example:

`{
"employees": {
    "employee_id": "str",
    "firstName": "str",
    "lastName": "str",
    "photo": "blob"
},
"transaction": {
    "transaction_id": "str",
    "transaction_name": "str",
    "transaction_created": "datetime"
}
}`

How to use:

`fastapi-g --input=.\model.json --project_name=test_project`