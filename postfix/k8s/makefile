help:
	@echo "make install"
	@echo "make uninstall"
	@echo "make connect"
	@echo ""
	@echo "Run: echo \"Hello User, This is the email sent via relay smtp server.\" | sendmail -s "Testmail" user1@org.example.test"

install:
	kubectl apply -f ./

uninstall:
	kubectl delete -f ./

connect:
	kubectl port-forward services/relay-smtp-svc 8025:25
