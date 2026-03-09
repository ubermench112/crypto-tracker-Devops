# Crypto Price Tracker (Serverless DevOps Project)

This project is a serverless cryptocurrency price tracker built on AWS.

It periodically collects crypto price data using a scheduled Lambda function, stores it in DynamoDB, and exposes an API endpoint to retrieve the latest price. The infrastructure is defined using CloudFormation and deployed through a CI/CD pipeline with CodePipeline and CodeBuild.

A fully serverless cryptocurrency price tracking system built on AWS using Infrastructure as Code and CI/CD automation.

This project collects cryptocurrency price data at scheduled intervals, stores it in DynamoDB, and exposes an API endpoint to retrieve the latest price.

The infrastructure is provisioned using CloudFormation and the deployment pipeline is automated using AWS CodePipeline and CodeBuild.

---

# Architecture Overview

The system follows an event-driven serverless architecture.

1. EventBridge triggers a scheduled Lambda function.
2. The Lambda collector fetches cryptocurrency prices from a public API.
3. The data is stored in DynamoDB.
4. Another Lambda function acts as an API handler.
5. API Gateway exposes an endpoint for users to query crypto prices.
6. CloudFormation provisions the infrastructure.
7. CodePipeline and CodeBuild automate CI/CD deployment.

---

# Architecture Diagram

![Architecture Diagram](screenshots/architecture.png)

---

# AWS Services Used

- AWS Lambda
- Amazon DynamoDB
- Amazon API Gateway
- Amazon EventBridge
- AWS CloudFormation
- AWS CodePipeline
- AWS CodeBuild

---

# Project Structure


crypto-price-tracker
│
├── infrastructure
│ └── template.yaml
│
├── lambda
│ ├── api
│ │ ├── handler.py
│ │ └── requirements.txt
│ │
│ └── collector
│ └── handler.py
│
├── screenshots
│
├── README.md
└── .gitignore


---

# Application Workflow

### 1. Scheduled Data Collection

Amazon EventBridge triggers the Collector Lambda function at scheduled intervals.

The collector Lambda:
- Fetches cryptocurrency prices from a public API
- Processes the data
- Stores the data in DynamoDB

### 2. Data Storage

The crypto price data is stored in an Amazon DynamoDB table called:


CryptoPriceTracker


Each record contains:

- crypto_name
- price_usd
- timestamp

---

### 3. API Access

An API Gateway endpoint exposes the stored crypto prices.

Route:


GET /prices


Example Request:


/prices?crypto=bitcoin


Example Response:

```json
{
 "crypto_name": "bitcoin",
 "price_usd": "66877",
 "timestamp": "2026-03-08T18:40"
}
Infrastructure as Code

All AWS resources are provisioned using AWS CloudFormation.

Resources defined in the template include:

Lambda functions

DynamoDB table

EventBridge rule

API Gateway

IAM roles and permissions

Infrastructure file:


infrastructure/template.yaml

CI/CD Pipeline

The project uses AWS CodePipeline and CodeBuild to automate deployments.

Pipeline Workflow:


GitHub
↓
CodePipeline
↓
CodeBuild
↓
CloudFormation Deployment
↓
Lambda + API Gateway Updated


Whenever code changes are pushed to GitHub:

CodePipeline is triggered

CodeBuild builds and packages Lambda functions

CloudFormation updates the infrastructure stack

Updated Lambda functions are deployed automatically

Deployment Steps

Clone the repository


git clone <repository-url>


Deploy infrastructure using CloudFormation


aws cloudformation deploy --template-file infrastructure/template.yaml --stack-name crypto-tracker


Verify deployment in AWS Console.

Screenshots
DynamoDB Table

API Gateway Route

CloudFormation Stack

API Response

Future Improvements

Add Terraform version of infrastructure

Implement monitoring with CloudWatch dashboards

Add unit tests for Lambda functions

Add multi-environment deployments (dev/staging/prod)

Implement authentication for API endpoints

Learning Outcomes

This project demonstrates:

Serverless architecture design

Infrastructure as Code with CloudFormation

Event-driven architecture

API design with API Gateway

CI/CD automation with CodePipeline and CodeBuild

DynamoDB data modeling

Lambda-based microservices

Author

DevOps Engineer Portfolio Project