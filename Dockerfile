# Use official Python base image
FROM python:3.10

# Set working directory inside container
WORKDIR /app

# Copy everything into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on (change if needed)
EXPOSE 5000

# Run your app (update if not app.py)
CMD ["python", "app.py"]
