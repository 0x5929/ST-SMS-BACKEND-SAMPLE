#!/bin/bash

APPS_DIR='apps'

msg="You are about to delete apps [ $* ] and remake their associated migration files, are you sure?"

read -p "$msg" -r
echo

if [[ $REPLY =~ ^[Yy](es)?$ ]]
then
	# first remove all app's migration folder
	for app in "$@"
	do
		if [ -d "$APPS_DIR/$app/migrations" ]
		then
            echo "Deleting $APPS_DIR/$app/migrations folder"
			rm -Ir "$APPS_DIR/$app/migrations"
		else
			echo "$APPS_DIR/$app/migrations does not exist"
		fi
	done

	# then remake migrations for each app
	for app in "$@"
	do
        echo "Remaking migrations folder for: $app"
		python manage.py makemigrations $app
	done	
fi

exit
