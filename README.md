# DevOps CI/CD Pipeline Project

## Overview
Automated CI/CD pipeline that builds, pushes and deploys 
a containerized Flask application to AWS EC2 automatically 
on every GitHub push.

## Architecture
Developer pushes code to GitHub
↓
GitHub Actions triggers automatically
↓
Docker image built & pushed to AWS ECR
↓
EC2 pulls latest image & deploys container
↓
App live on internet! 🌐

## Tech Stack
- **Application**                   — Python Flask
- **Containerization**              — Docker
- **Infrastructure as Code**        — Terraform
- **Container Registry**            — AWS ECR
- **Compute**                       — AWS EC2 (t3.micro)
- **Networking**                    — AWS VPC, Subnet, IGW, Security Groups
- **CI/CD**                         — GitHub Actions
- **OS**                            — Ubuntu 26.04 LTS

## AWS Infrastructure
- VPC with CIDR 10.0.0.0/16
- Public Subnet — 10.0.1.0/24
- Internet Gateway
- Route Table
- Security Group (Port 22, 5000)
- EC2 t3.micro instance

## CI/CD Pipeline Flow
1. Code pushed to main branch
2. GitHub Actions workflow triggers
3. AWS credentials configured
4. Docker image built
5. Image pushed to AWS ECR
6. EC2 pulls latest image
7. Old container stopped & removed
8. New container deployed on port 5000

## Live Demo
App URL: http://<EC2-PUBLIC-IP>:5000

Note: EC2 instance stopped to avoid AWS charges.
      Run locally using Docker steps below.

## How To Run Locally
```bash
# Clone repo
git clone https://github.com/shivam-gupta-14/devops-cicd-project

# Build Docker image
docker build -t devops-project-app .

# Run container
docker run -p 5000:5000 devops-project-app

# Open browser
http://localhost:5000
```

## Infrastructure Setup
```bash
# Initialize Terraform
cd terraform
terraform init

# Preview changes
terraform plan

# Apply infrastructure
terraform apply

# Destroy when done
terraform destroy
```

## Author
**Shivam Kumar Gupta**  
DevOps Engineer | Cloud Engineer  
[LinkedIn](https://www.linkedin.com/in/shivam-gupta14) | 
[GitHub](https://github.com/shivam-gupta-14)
