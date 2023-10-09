docker compose up -d
docker exec config-0 mongosh --file /data/db/crudconfig.js
docker exec crud1-0 mongosh --file /data/db/crud1.js
docker exec crud2-0 mongosh --file /data/db/crud2.js
sleep 10
docker exec crud-router mongosh --file /data/db/shard.js
