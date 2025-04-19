FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create a non-root user
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpango1.0-0 \
    libcairo2 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy dependency list and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY template.html .
COPY make_pdf.py .
COPY web.py .

# Use non-root user from now on
USER appuser

# Use a production server
EXPOSE 5000
CMD ["waitress-serve", "--host=0.0.0.0", "--port=5000", "web:app"]
