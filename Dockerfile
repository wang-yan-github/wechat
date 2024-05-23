FROM python:3.9-slim

WORKDIR /app

# 使用清华镜像源安装依赖
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD ["python", "login_and_send_message_999.py"]
