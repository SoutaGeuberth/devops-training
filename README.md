# devops-training
my first steps for devops engineering

This is just a quick tutorial of how to stablish all the enviroment to run it with no complications

install Docker Desktop

1. run docker compose up in the root of the project 
2. run docker ps and it would deploy the id of the dockers
3. run docker exec -it <id_docker> bash for the id_locker you will start with a run docker exec -it <id_docker_of_crudb1-0> bash
4. run mongosh
5. run use config;
6. paste the content of crud1.js on the terminal #for the instruction of "line 14" you will need crud2.js, crudconfig.js and shard.js for the docker crud-router
7. replicate the process from "line 10" to "line 13" changing the (id_docker_of_cruddb1-0) for id_docker_of_cruddb2-0 and id_docker_of_cruddb-config-0 so on
8. go to root project directory in terminal and run docker compose start
