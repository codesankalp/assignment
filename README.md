How to run:

```bash

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```

Endpoints:

```
http://localhost:8000/box/ - GET - List all the boxes
http://localhost:8000/box/my-boxes/ - GET -List all boxes of authenticated user
http://localhost:8000/box/ - POST - Create Box
http://localhost:8000/box/{id} - PUT - Update Box
http://localhost:8000/box/{id} - PATCH - Update Box partially
http://localhost:8000/box/{id} - DELETE - Delete Box
http://localhost:8000/box/{id} - GET - Get Box detail
http://localhost:8000/token/ - POST - Get token (session and basic auth is also supported)
```

SWAGGER - `http://localhost:8000/`

REDOC - `http://localhost:8000/redoc/`

API Schema:

```json
{
  "swagger": "2.0",
  "info": {
    "title": "CRUD APIs",
    "description": "Store APIs",
    "contact": {
      "email": "sankalp123427@gmail.com"
    },
    "license": {
      "name": "BSD License"
    },
    "version": "v1"
  },
  "host": "localhost:8000",
  "schemes": [
    "http"
  ],
  "basePath": "/api",
  "consumes": [
    "application/json"
  ],
  "produces": [
    "application/json"
  ],
  "securityDefinitions": {
    "Basic": {
      "type": "basic"
    }
  },
  "security": [
    {
      "Basic": [
        
      ]
    }
  ],
  "paths": {
    "/box": {
      "get": {
        "operationId": "box_list",
        "description": "",
        "parameters": [
          {
            "name": "length__lt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "number"
          },
          {
            "name": "length__gt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "number"
          },
          {
            "name": "width__lt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "number"
          },
          {
            "name": "width__gt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "number"
          },
          {
            "name": "height__lt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "number"
          },
          {
            "name": "height__gt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "number"
          },
          {
            "name": "area__lt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "number"
          },
          {
            "name": "area__gt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "number"
          },
          {
            "name": "volume__lt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "number"
          },
          {
            "name": "volume__gt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "number"
          },
          {
            "name": "created_by__username",
            "in": "query",
            "description": "",
            "required": false,
            "type": "string"
          },
          {
            "name": "created_on__lt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "string"
          },
          {
            "name": "created_on__gt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Box"
              }
            }
          }
        },
        "tags": [
          "box"
        ]
      },
      "post": {
        "operationId": "box_create",
        "description": "",
        "parameters": [
          {
            "name": "data",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/Box"
            }
          }
        ],
        "responses": {
          "201": {
            "description": "",
            "schema": {
              "$ref": "#/definitions/Box"
            }
          }
        },
        "tags": [
          "box"
        ]
      },
      "parameters": [
        
      ]
    },
    "/box/my-boxes": {
      "get": {
        "operationId": "box_list_my_boxes",
        "description": "",
        "parameters": [
          {
            "name": "length__lt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "number"
          },
          {
            "name": "length__gt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "number"
          },
          {
            "name": "width__lt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "number"
          },
          {
            "name": "width__gt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "number"
          },
          {
            "name": "height__lt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "number"
          },
          {
            "name": "height__gt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "number"
          },
          {
            "name": "area__lt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "number"
          },
          {
            "name": "area__gt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "number"
          },
          {
            "name": "volume__lt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "number"
          },
          {
            "name": "volume__gt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "number"
          },
          {
            "name": "created_by__username",
            "in": "query",
            "description": "",
            "required": false,
            "type": "string"
          },
          {
            "name": "created_on__lt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "string"
          },
          {
            "name": "created_on__gt",
            "in": "query",
            "description": "",
            "required": false,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Box"
              }
            }
          }
        },
        "tags": [
          "box"
        ]
      },
      "parameters": [
        
      ]
    },
    "/box/{id}": {
      "get": {
        "operationId": "box_read",
        "description": "",
        "parameters": [
          
        ],
        "responses": {
          "200": {
            "description": "",
            "schema": {
              "$ref": "#/definitions/Box"
            }
          }
        },
        "tags": [
          "box"
        ]
      },
      "put": {
        "operationId": "box_update",
        "description": "",
        "parameters": [
          {
            "name": "data",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/Box"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "schema": {
              "$ref": "#/definitions/Box"
            }
          }
        },
        "tags": [
          "box"
        ]
      },
      "patch": {
        "operationId": "box_partial_update",
        "description": "",
        "parameters": [
          {
            "name": "data",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/Box"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "schema": {
              "$ref": "#/definitions/Box"
            }
          }
        },
        "tags": [
          "box"
        ]
      },
      "delete": {
        "operationId": "box_delete",
        "description": "",
        "parameters": [
          
        ],
        "responses": {
          "204": {
            "description": ""
          }
        },
        "tags": [
          "box"
        ]
      },
      "parameters": [
        {
          "name": "id",
          "in": "path",
          "description": "A unique integer value identifying this box.",
          "required": true,
          "type": "integer"
        }
      ]
    },
    "/token/": {
      "post": {
        "operationId": "token_create",
        "description": "",
        "parameters": [
          {
            "name": "data",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/AuthToken"
            }
          }
        ],
        "responses": {
          "201": {
            "description": "",
            "schema": {
              "$ref": "#/definitions/AuthToken"
            }
          }
        },
        "tags": [
          "token"
        ]
      },
      "parameters": [
        
      ]
    }
  },
  "definitions": {
    "Box": {
      "required": [
        "length",
        "width",
        "height"
      ],
      "type": "object",
      "properties": {
        "id": {
          "title": "ID",
          "type": "integer",
          "readOnly": true
        },
        "length": {
          "title": "Length",
          "description": "Length of the box",
          "type": "number"
        },
        "width": {
          "title": "Width",
          "description": "Breadth of the box",
          "type": "number"
        },
        "height": {
          "title": "Height",
          "description": "Height of the box",
          "type": "number"
        },
        "area": {
          "title": "Area",
          "description": "Area of the box",
          "type": "number",
          "readOnly": true
        },
        "volume": {
          "title": "Volume",
          "description": "Volume of the box",
          "type": "number",
          "readOnly": true
        }
      }
    },
    "AuthToken": {
      "required": [
        "username",
        "password"
      ],
      "type": "object",
      "properties": {
        "username": {
          "title": "Username",
          "type": "string",
          "minLength": 1
        },
        "password": {
          "title": "Password",
          "type": "string",
          "minLength": 1
        },
        "token": {
          "title": "Token",
          "type": "string",
          "readOnly": true,
          "minLength": 1
        }
      }
    }
  }
}
```