FROM python:3.11

WORKDIR /Bewise_test
COPY requirements.txt /Bewise_test/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /Bewise_test/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
