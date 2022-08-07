NAME ?= aneeshroy

all: build run push

images:
	docker images | grep ${NAME}

ps:
	docker ps -a | grep ${NAME}

build:
	docker build -t ${NAME}/o-iss-where-art-thou:1.0 .

run:
	docker run --rm -d -p 5025:5000 --name aneesh-iss ${NAME}/o-iss-where-art-thou:1.0

push:
	docker push ${NAME}/o-iss-where-art-thou:1.0

pull:
	docker pull ${NAME}/o-iss-where-art-thou:1.0

kill:
	docker rm -f aneesh-iss