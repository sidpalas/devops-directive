# set environment variables
export PROJECT_ID=<TODO: YOUR GCP PROJECT ID>
export DOMAIN=<TODO: YOUR DOMAIN>

# create the bucket
gsutil mb -p $PROJECT_ID -b on gs://$DOMAIN

# set website config
gsutil web set -m index.html -e 404.html gs://$DOMAIN

# add user permissions
gsutil iam ch allUsers:legacyObjectReader gs://$DOMAIN

# copy the website files!
gsutil -m rsync -d -r my-website/build gs://$DOMAIN

# 🎉🎉🎉