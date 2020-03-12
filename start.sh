[ -f *.db ] && rm *.db
docker-compose build
docker-compose up
