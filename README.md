# Secure DevSecOps Pipeline

## Project Overview

This project demonstrates the implementation of a Secure DevSecOps Pipeline using GitHub Actions to automate security testing during software development. The pipeline integrates static code analysis, container vulnerability scanning, dependency monitoring, and continuous integration to improve software security.

The project follows DevSecOps principles by shifting security testing earlier in the software development lifecycle, ensuring vulnerabilities are detected before deployment.

---

## Objectives

- Build an automated CI/CD security pipeline.
- Detect insecure Python code using Bandit.
- Scan Docker images using Trivy.
- Automate workflow execution using GitHub Actions.
- Demonstrate vulnerability detection and remediation.
- Improve secure software development practices.

---

## Technologies Used

- Python 3.13
- Git
- GitHub
- GitHub Actions
- Docker
- Bandit
- Trivy
- Dependabot
- Kali Linux

---

## Project Structure

```
secure-devsecops-pipeline
│
├── .github/
│   └── workflows/
│       └── security.yml
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Workflow

Developer Pushes Code

↓

GitHub Actions Triggered

↓

Bandit Static Code Analysis

↓

Docker Image Build

↓

Trivy Vulnerability Scan

↓

Pipeline Status Generated

↓

Secure Code Ready for Deployment

---

## Features

- Automated security scanning
- Continuous Integration (CI)
- Static Application Security Testing (SAST)
- Docker image scanning
- Dependency monitoring
- Automated workflow execution
- Secure coding validation

---

## Security Tools

### Bandit

Bandit performs static security analysis on Python source code and detects insecure programming practices such as shell injection vulnerabilities.

### Trivy

Trivy scans Docker images for known vulnerabilities, insecure packages, and misconfigurations.

### Dependabot

Dependabot automatically monitors project dependencies and suggests security updates.

---

## Project Results

The pipeline successfully:

- Detected shell injection vulnerability.
- Identified insecure Python code.
- Demonstrated secure code remediation.
- Executed automated security scans.
- Built Docker container successfully.
- Completed Trivy vulnerability scanning.
- Generated successful GitHub Actions workflow.

---

## Future Enhancements

- Integrate CodeQL analysis.
- Add OWASP Dependency Check.
- Deploy using Kubernetes.
- Integrate SonarQube.
- Add automated security notifications.

---

## Conclusion

This project demonstrates how DevSecOps practices can automate security testing during software development. The integration of GitHub Actions, Bandit, Trivy, and Dependabot provides an effective security pipeline capable of identifying vulnerabilities early in the development lifecycle.

---

## Author

**Mohammad Rinshan**

MCA Cybersecurity

Jain University
