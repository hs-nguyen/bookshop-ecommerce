# Dockerfile Review and Fixes

## 🔴 Critical Issues Fixed

### 1. Missing Base Image Name
**Issue:** `FROM 3.10.19-slim` - Missing "python:" prefix
**Fix:** `FROM python:3.10.19-slim`
**Impact:** Docker build would fail immediately

### 2. Incorrect ENTRYPOINT Syntax
**Issue:** `ENTRYPOINT [ "gunicorn --workers 4..." ]` - String instead of array
**Fix:** `CMD ["gunicorn", "--workers", "4", ...]`
**Impact:** Container would fail to start

### 3. Missing System Dependencies
**Issue:** No PostgreSQL client or build tools
**Fix:** Added `gcc` and `postgresql-client`
**Impact:** psycopg2 installation would fail

### 4. Security: Running as Root
**Issue:** Container runs as root user
**Fix:** Created non-root user `appuser`
**Impact:** Security vulnerability fixed

### 5. Inefficient Layer Caching
**Issue:** Copying all files before pip install
**Fix:** Copy requirements.txt first, then install
**Impact:** Faster builds with better caching

### 6. Missing Python Packages in Final Stage
**Issue:** Only copying /app, not installed packages
**Fix:** Copy site-packages from build stage
**Impact:** Application would fail to run

## ✅ Improvements Made

### 1. Multi-Stage Build Optimization
```dockerfile
# Build stage - includes build tools
FROM python:3.10.19-slim as build

# Runtime stage - minimal dependencies
FROM python:3.10.19-slim
```

### 2. Layer Caching
```dockerfile
# Copy requirements first (changes less often)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code later (changes more often)
COPY . .
```

### 3. Security Hardening
```dockerfile
# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser
```

### 4. Proper Command Syntax
```dockerfile
# Use CMD with array syntax (not ENTRYPOINT with string)
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8000", "bookshop.wsgi:application"]
```

### 5. Clean APT Cache
```dockerfile
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*
```

## 📋 Additional Files Created

### 1. .dockerignore
Excludes unnecessary files from Docker context:
- Python cache files
- Virtual environments
- Git files
- Environment files
- Log files

**Benefits:**
- Faster builds
- Smaller context
- No sensitive data in image

### 2. docker-compose.yml
Complete development environment:
- PostgreSQL database
- Django backend
- Health checks
- Volume persistence
- Environment variables

## 🚀 Usage

### Build Image
```bash
cd backend
docker build -t bookshop-backend .
```

### Run Container
```bash
docker run -p 8000:8000 \
  -e DEBUG=True \
  -e SECRET_KEY=your-secret-key \
  -e DB_HOST=host.docker.internal \
  bookshop-backend
```

### Using Docker Compose (Recommended)
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Run migrations
docker-compose exec backend python manage.py migrate

# Create superuser
docker-compose exec backend python manage.py createsuperuser

# Seed data
docker-compose exec backend python manage.py shell < seed_data.py

# Stop services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

## 🔍 Dockerfile Best Practices Applied

### ✅ Security
- [x] Non-root user
- [x] Minimal base image (slim)
- [x] No secrets in Dockerfile
- [x] Clean package cache

### ✅ Performance
- [x] Multi-stage build
- [x] Layer caching optimization
- [x] Minimal dependencies
- [x] .dockerignore file

### ✅ Maintainability
- [x] Clear stage names
- [x] Comments for clarity
- [x] Proper command syntax
- [x] Explicit WORKDIR

### ✅ Production Ready
- [x] Gunicorn WSGI server
- [x] Multiple workers (4)
- [x] Proper port binding
- [x] Health check support

## 📊 Image Size Comparison

### Before Optimization
- Base image issues would prevent build
- If it worked: ~500-600MB

### After Optimization
- Build stage: ~400MB (discarded)
- Final image: ~200-250MB
- Efficient layer caching

## 🔧 Production Deployment

### Environment Variables Required
```bash
DEBUG=False
SECRET_KEY=<strong-random-key>
ALLOWED_HOSTS=yourdomain.com
DB_NAME=bookshop_prod
DB_USER=bookshop_user
DB_PASSWORD=<strong-password>
DB_HOST=db.yourdomain.com
DB_PORT=5432
CORS_ALLOWED_ORIGINS=https://yourdomain.com
```

### Production docker-compose.yml
```yaml
version: '3.8'

services:
  backend:
    image: bookshop-backend:latest
    restart: always
    environment:
      - DEBUG=False
      - SECRET_KEY=${SECRET_KEY}
      - DB_HOST=${DB_HOST}
      # ... other env vars
    ports:
      - "8000:8000"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/admin/"]
      interval: 30s
      timeout: 10s
      retries: 3
```

### Kubernetes Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: bookshop-backend
spec:
  replicas: 3
  selector:
    matchLabels:
      app: bookshop-backend
  template:
    metadata:
      labels:
        app: bookshop-backend
    spec:
      containers:
      - name: backend
        image: bookshop-backend:latest
        ports:
        - containerPort: 8000
        env:
        - name: DEBUG
          value: "False"
        - name: SECRET_KEY
          valueFrom:
            secretKeyRef:
              name: bookshop-secrets
              key: secret-key
```

## 🧪 Testing the Dockerfile

### 1. Build Test
```bash
docker build -t bookshop-backend:test .
```

### 2. Run Test
```bash
docker run --rm bookshop-backend:test python manage.py check
```

### 3. Security Scan
```bash
docker scan bookshop-backend:test
```

### 4. Size Check
```bash
docker images bookshop-backend:test
```

## 🐛 Troubleshooting

### Build Fails at pip install
**Issue:** Missing system dependencies
**Solution:** Check gcc and postgresql-client are installed

### Container Exits Immediately
**Issue:** Command syntax error
**Solution:** Use CMD with array syntax, not string

### Permission Denied Errors
**Issue:** Files owned by root
**Solution:** Ensure chown command runs before USER switch

### Database Connection Fails
**Issue:** Wrong DB_HOST
**Solution:** Use service name in docker-compose or host.docker.internal

## 📈 Performance Tuning

### Gunicorn Workers
```dockerfile
# CPU-bound: workers = (2 x CPU cores) + 1
CMD ["gunicorn", "--workers", "4", "--threads", "2", ...]
```

### Memory Limits
```yaml
services:
  backend:
    deploy:
      resources:
        limits:
          memory: 512M
        reservations:
          memory: 256M
```

## 🎯 Summary

### Issues Fixed (6)
1. ✅ Missing python: in base image
2. ✅ Incorrect ENTRYPOINT syntax
3. ✅ Missing system dependencies
4. ✅ Running as root user
5. ✅ Poor layer caching
6. ✅ Missing Python packages in final stage

### Files Created (3)
1. ✅ Dockerfile (fixed)
2. ✅ .dockerignore
3. ✅ docker-compose.yml

### Ready For
- ✅ Development (docker-compose)
- ✅ Testing (docker build)
- ✅ Production (with env vars)
- ✅ CI/CD pipelines
- ✅ Kubernetes deployment
