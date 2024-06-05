FROM python:3.12-slim

WORKDIR /app

# Required by weasyprint
RUN apt-get update && apt-get install -y \
    libpango1.0-0 \
    libcairo2 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info \
    && rm -rf /var/lib/apt/lists/*

# Install pip dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app
COPY template.html /app
COPY make_pdf.py /app
COPY web.py /app

# Open flask port
EXPOSE 5000

# Tells flask what 'run' should run
ENV FLASK_APP=web.py

# host=0.0.0.0 allows access outside the container
CMD ["flask", "run", "--host=0.0.0.0"]

