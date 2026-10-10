# DevOps Demo App

Small Flask app used to practice Docker, security scanning, and CI/CD.

## Run locally
    python3 -m venv venv && source venv/bin/activate
    pip install -r requirements-dev.txt
    python app.py            # http://localhost:5000
    pytest                   # run tests

## Run with Docker
    docker build -t devops-demo-app:1.0 .
    docker run -d -p 5000:5000 --name demo devops-demo-app:1.0
    curl localhost:5000
    curl localhost:5000/health

## Security checks
    gitleaks detect -s .
    trufflehog git file://. --only-verified
    trivy image --scanners vuln devops-demo-app:1.0
