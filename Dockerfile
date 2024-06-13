FROM apache/airflow:2.9.1
USER airflow
COPY requirements.txt .
# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
