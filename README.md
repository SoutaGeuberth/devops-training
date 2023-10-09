# devops-training
my first steps for devops engineering

This is just a quick tutorial of how to stablish all the enviroment to run it with no complications

install Docker Desktop

run docker compose up in the root of the project 
run docker ps and it would deploy the id of the dockers
run docker exec -it <id_docker> bash for the id_locker you will start with a run docker exec -it <id_docker_of_crudb1-0> bash
run mongosh
run use config;
paste the content of crud1.js on the terminal #for the instruction of "line 14" you will need crud2.js, crudconfig.js and shard.js for the docker crud-router
replicate the process from "line 10" to "line 13" changing the (id_docker_of_cruddb1-0) for id_docker_of_cruddb2-0 and id_docker_of_cruddb-config-0 so on
go to root project directory in terminal and run docker compose start
