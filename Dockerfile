FROM python:3.8-slim


# Set work directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt /app/

# Install Requirements
RUN pip install -r requirements.txt

# Copy code
COPY . /app/

CMD uvicorn main:app --host 0.0.0.0 --port 5000 --log-level debug