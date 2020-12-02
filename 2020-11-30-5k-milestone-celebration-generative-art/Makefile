PROJECT_ID:=devops-directive-project
DOMAIN:=style-transfer.devopsdirective.com

generate-images:
	poetry run python yt_get_subscriber_data.py
	poetry run python generate_images.py
	poetry run python reshape_subscriber_data.py
	cp ./subscriber_data_array.json ./subscriber-gallery/src/subscriber_data_array.json
	cp -r ./photos/* ./subscriber-gallery/public/photos/

set-up-bucket:
	gsutil mb -p $(PROJECT_ID) -b on gs://$(DOMAIN)
	gsutil web set -m index.html -e 404.html gs://$(DOMAIN)
	gsutil iam ch allUsers:legacyObjectReader gs://$(DOMAIN)

build-site:
	cd subscriber-gallery && yarn build

deploy-website:
	gsutil -m rsync -r -c -d subscriber-gallery/build gs://$(DOMAIN)
