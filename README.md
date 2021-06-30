Pre-requisite 
Docker desktop and docker-compose should be up running.

Steps to run the application:-
1) unzip lemon.zip file and cd lemon


2) docker-compose -f ./docker-compose.yaml up --build


3) From postman generate POST request to url
   "http://127.0.0.1:8000/account/56a7e0d8-d288-11eb-9be0-d7593912b03c/order/"
    
    payload as follows 
   
   {
   
    "isin": "b9dbbdc6",
    "valid_until": "2021-07-26 10:19:20",
    "limit_price": 10.25,
    "side": "B"
  
   }
    
4) To run test within docker:
   
    EXPORT ENV=TEST
   
    docker-compose -f ./docker-compose.yaml up --build

    unset $ENV and execute normal docker
