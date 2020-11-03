ENCRYPTION_KEY=Where-am-I-supposed-to-store-this?!

encrypt-secrets-file:
	openssl aes-256-cbc -a -salt -in secrets.env -out secrets.env.enc -pass pass:$(ENCRYPTION_KEY)

decrypt-secrets-file:
	openssl aes-256-cbc -d -a -salt -in secrets.env.enc -out secrets.env -pass pass:$(ENCRYPTION_KEY)
