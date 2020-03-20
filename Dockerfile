FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN python init-database.py
EXPOSE 8080
CMD ["python", "run-production.py"]