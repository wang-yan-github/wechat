FROM python:3.9-slim

WORKDIR /app

#COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --index-url https://pypi.tuna.tsinghua.edu.cn/simple itchat requests schedule itchat-uos==1.5.0.dev0
#RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD ["python", "login_and_send_message_999.py"]
