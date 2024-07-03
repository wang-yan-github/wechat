FROM python:3.9-slim

WORKDIR /app

# 如果需要卸载所有依赖项，可以使用以下命令。不建议除非确实需要清理所有依赖项。
# RUN pip uninstall -y '*'

# 安装依赖项
RUN pip install --no-cache-dir --index-url https://pypi.tuna.tsinghua.edu.cn/simple requests schedule itchat-uos itchat-uos==1.5.0.dev0

# 如果有使用 requirements.txt 的需要，可以取消注释以下行，并确保在项目中包含了 requirements.txt 文件。
# COPY requirements.txt requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 将当前目录下的所有文件复制到 Docker 镜像的 /app 目录中
COPY . .

# 定义容器启动时运行的命令
CMD ["python", "login_and_send_message_999.py"]
