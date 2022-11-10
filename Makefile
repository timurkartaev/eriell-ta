.PHONY: no_targets

no_targets:
	echo "command expected"

build-web:
	docker-compose -f ./docker-compose.yml build web

up:
	docker-compose -f ./docker-compose.yml up -d

down:
	docker-compose -f ./docker-compose.yml down

downv:
	docker-compose -f ./docker-compose.yml down -v

ps:
	docker-compose -f ./docker-compose.yml ps