run:
	docker-compose up
run-detach:
	docker-compose up -d 
migrations:
	docker-compose run --rm appserver python manage.py makemigrations
superuser:
	docker-compose run --rm appserver python manage.py createsuperuser