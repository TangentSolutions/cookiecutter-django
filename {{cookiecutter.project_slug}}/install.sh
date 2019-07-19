#! /bin/bash

pip install --upgrade pip pipenv
pipenv lock

if [ "$BUILD" == "DEV" ];
    then
    	echo "Installing development dependencies";
    	pipenv install --dev --system --deploy --ignore-pipfile;
    else
    	echo "Installing production dependencies";
    	pipenv install --system --deploy --ignore-pipfile;
fi
