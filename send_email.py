from email.message import EmailMessage
from smtplib import SMTP


#from_addr = 'shaydruano2020@itp.edu.co'
#to= 'shaydruano2020@itp.edu.co'
#message = 'Este es un mensaje de prueba'

#=======================================================================

msg= EmailMessage()
msg.set_content('Eres una perra')

msg['Subject']='Mi perra'
msg['From']='fabiohernandez2020@itp.edu.co'
msg['To']='cristianrobles2020@itp.edu.co'

#=======================================================================

username = 'fabiohernandez2020@itp.edu.co'
password = '1006814041'

server = SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)

#=======================================================================
#server.sendmail(from_addr, to, message)
#=======================================================================
server.send_message(msg)
#=======================================================================
server.quit()
