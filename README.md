# DevOps CI/CD Pipeline Project

## Overview
Automated CI/CD pipeline that deploys a 
containerized Flask app to AWS EC2 using 
GitHub Actions and Terraform.

## Architecture
GitHub → GitHub Actions → Docker Build → 
AWS ECR → Terraform → AWS EC2 → Live App

## Tech Stack
- Python Flask (Application)
- Docker (Containerization)
- Terraform (Infrastructure as Code)
- AWS ECR (Container Registry)
- AWS EC2 (Compute)
- AWS VPC (Networking)
- GitHub Actions (CI/CD)

## How It Works
1. Developer pushes code to main branch
2. GitHub Actions pipeline triggers automatically
3. Docker image is built and pushed to ECR
4. Terraform provisions/updates AWS infrastructure
5. Application is deployed and accessible publicly

## Live Demo
App URL: http://<EC2-PUBLIC-IP>:5000
