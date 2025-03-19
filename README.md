## REST API for User Management

This project contains a REST API for user management, built using Flask.

### To get started:

1. Build and start the containers using Docker:
   ```bash
    docker-compose up --build
   ```

2. If you want to run tests
    ```bash
    docker-compose exec backend sh
    ```

    ```bash
    pytest
    ```

3. Path to Swagger
   ```bash
   http://127.0.0.1:5000/swagger/
   ```



### GET Request
![GET](./images/GET.png)

### GET by ID Request
![GET_BY_ID](./images/GET_BY_ID.png)

### POST Request
![POST](./images/POST.png)

### PUT Request
![PUT](./images/PUT.png)

### DELETE Request
![DELETE](./images/DELETE.png)
