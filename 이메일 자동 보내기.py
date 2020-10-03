import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


# 보내는 사람 정보
me = "보내는사람@gmail.com"
my_password = "비밀번호"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보
you = "받는사람@아무_도메인"

# 메일 기본 정보 설정
msg = MIMEMultipart('alternative')
msg['Subject'] = "제목"
msg['From'] = me
msg['To'] = you

# 메일 내용 쓰기
content = "메일 내용"
part2 = MIMEText(content, 'plain')
msg.attach(part2)

# 메일 보내고 서버 끄기
s.sendmail(me, you, msg.as_string())
s.quit()



#2단계 인증을 제거해야함
https://myaccount.google.com/signinoptions/two-step-verification

#보안 수준 낮은 앱 제거해야함
https://myaccount.google.com/lesssecureapps

#이 두단계를 거쳐야 정상적으로 메일 전송 가능.
