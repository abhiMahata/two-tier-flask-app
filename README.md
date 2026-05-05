# Two-Tier Flask Application — CI/CD on AWS EC2

This isa demo on a fully automated CI/CD pipeline that deploys a containerized two-tier web application (Flask + MySQL) on AWS EC2 using Jenkins, Docker, and Docker Compose.

Architecture

Developer -> GitHub -> Jenkins Pipeline -> Docker Compose -> EC2

- Flask app runs in a Docker container (port 5000)
- MySQL database runs in a separate Docker container
- Jenkins automates build and deployment on every git push
- All services managed via Docker Compose on AWS EC2 (t2.micro)

Tech Stack

 AWS EC2 - Cloud hosting (Ubuntu 24.04) 
  Docker - Containerization 
  Docker Compose - Multi-container orchestration 
  Jenkins - CI/CD automation 
  Flask - Python web framework 
  MySQL - Relational database 
  GitHub - Source code management 

Pipeline Stages

1. Clone Code - Jenkins pulls latest code from GitHub
2. Build Docker Image - builds Flask app image
3. Deploy - runs docker-compose to start/update containers

How to Run

1. Launch an Ubuntu EC2 instance (t2.micro)
2. Install Docker and run Jenkins as a container
3. Configure Jenkins pipeline pointing to this repo
4. Push any change to main branch — Jenkins auto-deploys

Screenshots

<img width="1920" height="1043" alt="Screenshot_2026-05-03_15-09-41" src="https://github.com/user-attachments/assets/1d13e426-ccec-48d5-bc26-5084f00555d1" />
<img width="1920" height="1043" alt="Screenshot_2026-05-03_15-15-32" src="https://github.com/user-attachments/assets/b73d705a-9f80-43a8-89be-7594c3520dc0" />
<img width="1920" height="1043" alt="Screenshot_2026-05-03_15-35-19" src="https://github.com/user-attachments/assets/76864e57-359d-4e5f-b0dc-88f7069f152b" />
<img width="1920" height="1043" alt="Screenshot_2026-05-03_15-35-57" src="https://github.com/user-attachments/assets/dc70643e-f7c6-41e7-b98d-b3dacd5d8aab" />
<img width="1920" height="1043" alt="Screenshot_2026-05-03_15-37-28" src="https://github.com/user-attachments/assets/c2e472da-6556-4e58-aabc-9644403c2a78" />
<img width="1920" height="1043" alt="Screenshot_2026-05-03_15-37-44" src="https://github.com/user-attachments/assets/3129145a-7323-42da-af76-93e17202c790" />
<img width="1920" height="1043" alt="Screenshot_2026-05-03_15-39-39" src="https://github.com/user-attachments/assets/83904f7b-8d4a-4878-82d6-a4ca63e85063" />
<img width="1920" height="1043" alt="Screenshot_2026-05-03_16-19-33" src="https://github.com/user-attachments/assets/a67bb3ca-7a4a-4ad2-abd7-6f0a57c99824" />
<img width="1920" height="1043" alt="Screenshot_2026-05-04_22-02-49" src="https://github.com/user-attachments/assets/3437129c-b857-4c92-8943-d4d8182ddac9" />
<img width="1920" height="1043" alt="Screenshot_2026-05-04_22-06-22" src="https://github.com/user-attachments/assets/2edf7199-f758-40fc-8fe9-da2e90a9eeec" />
<img width="1920" height="1043" alt="Screenshot_2026-05-04_22-27-39" src="https://github.com/user-attachments/assets/ea4e1d10-90d2-4eee-aa40-adbf9d17708a" />



What I Learned ffrom this?

- Setting up a CI/CD pipeline from scratch
- Containerizing a multi-service application with Docker Compose
- Deploying and managing applications on AWS EC2
- Debugging real-world Docker networking and permissions issues
- Infrastructure setup with zero cost using AWS Free Tier
