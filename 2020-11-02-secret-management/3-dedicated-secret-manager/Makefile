PROJECT_ID:=<MY_GCP_PROJECT>
SECRET_NAME:=DB_PASS

define get-secret
$(shell gcloud secrets versions access latest --secret=$(1) --project=$(PROJECT_ID))
endef

run-app:
	@DB_PASS=$(call get-secret,$(DB_PASS))" npm start