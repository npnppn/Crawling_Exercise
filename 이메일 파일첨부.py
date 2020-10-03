part = MIMEBase('application', "octet-stream")
with open("articles.xlsx", 'rb') as file:
    part.set_payload(file.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment", filename="추석기사.xlsx")
msg.attach(part)

# 이 부분을 send email부분 앞에 적으면됨
