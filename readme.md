Smarsh wants to Split the Mails coming via SMTP between 2 Servers (Apps) in PCF and Kubernetes. 
The Above diagram shows TO-BE State, where the emails should be filtered and routed based on ome SMTP headers like mail domain or hostname.
One solution from Caizin/Hemanth is writing a custom Router with Go-lang


docker run -d --name postfix -P \
       -e SMTP_SERVER=smtp.bar.com \
       -e SERVER_HOSTNAME=helpdesk.mycompany.com \           
       juanluisbaptiste/postfix

docker run -d --name postfix-local -p "1025:25"  \
       -e SMTP_SERVER=smtp.freesmtpservers.com \
       -e SMTP_PORT=25 \
       -e SERVER_HOSTNAME=mac.gmail.com \
       juanluisbaptiste/postfix

#echo "Test sending email from Postfix" | mail -s "Test Postfix" kn.sandeep@gmail.com

# Check Email

https://www.wpoven.com/tools/free-smtp-server-for-testing#
