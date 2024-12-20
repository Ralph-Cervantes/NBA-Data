# NBA ETL Pipeline 🚀

## About the Project

This project is an **ETL (Extract, Transform, Load) pipeline** designed to collect, clean, and store NBA data for analysis and reporting. It combines web scraping, data transformation, and database management to build a robust and scalable application.

---

### Features
- **Extract**: Scrapes NBA data from the internet using the Scrapy framework.
- **Transform**: Cleans and processes raw data into a structured and usable format using Pandas.
- **Load**: Stores the processed data into a PostgreSQL database.
- **Orchestration**: Automates the ETL process using Apache Airflow.
- **Containerization**: Deploys the entire application in Docker containers for easy management.
- **Cloud Computing**: Uses Terraform to manage and deploy cloud resources.

---

### Tech Stack

- 🕷️ **Scrapy**: Web scraping framework for collecting NBA data.
- ☁️ **Terraform**: Infrastructure as code for managing cloud resources.
- 🐳 **Docker**: Containerization for consistent and portable deployments.
- 📊 **Pandas**: Python library for data cleaning and transformation.
- ⏱️ **Apache Airflow**: Workflow orchestration and scheduling.
- 🛢️ **PostgreSQL**: Relational database for storing processed data.

---

### Getting Started

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/nba-etl-pipeline.git
   cd nba-etl-pipeline
   ```

2. **Set Up Environment**:
   - Install Docker and Docker Compose.
   - Configure your cloud infrastructure using Terraform.

3. **Build and Run Docker Containers**:
   ```bash
   docker-compose up --build
   ```

4. **Access Airflow**:
   - Navigate to `http://localhost:8080` to monitor and manage the ETL workflows.

---

### Project Structure

```
.
├── dags/                 # Airflow DAGs for ETL orchestration
├── scraper/             # Scrapy project for web scraping
├── transform/           # Scripts for data cleaning and transformation
├── docker-compose.yml   # Docker Compose file for containerization
├── terraform/           # Terraform scripts for cloud setup
└── README.md            # Project documentation
```

---

### Future Enhancements

- Add real-time data ingestion capabilities.
- Build dashboards for data visualization using tools like Tableau or Power BI.
- Incorporate advanced analytics and machine learning for player and team insights.

---

### Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to fork the repository and submit a pull request.

---

### Contact

Feel free to reach out with any questions or suggestions:
- **Email**: [rafael.g.cervantes@gmail.com](mailto:rafael.g.cervantes@gmail.com)

Let’s build something amazing together! 🏀

