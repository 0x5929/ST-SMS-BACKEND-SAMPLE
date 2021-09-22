#!/bin/bash

msg="You are about to delete apps [ $* ] and remake their associated migration files, are you sure?"

read -p "$msg" -r
echo

if [[ $REPLY =~ ^[Yy](es)?$ ]]
then
	# first remove all app's migration folder
	for app in "$@"
	do
		if [ -d "$app/migrations" ]
		then
			rm -Ir "$app/migrations"
		else
			echo "$app/migrations does not exist"
		fi
	done

	# then remake migrations for each app
	for app in "$@"
	do
		python manage.py makemigrations $app
	done	
fi

exit
