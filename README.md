# Data Science Learning Platform

## Overview

A data science learning and interactive web app designed to help users learn and practice data science concepts. Built with Django and React, it allows users to engage with coding challenges and track their progress in improving their skills.

## Tech Stack

- **Backend**: Django 4.2, Django Rest Framework
- **Frontend**: React 18
- **Database**: PostgreSQL 13
- **Authentication**: JWT (JSON Web Tokens)
- **Code Execution**: Docker (for sandboxed environments)

## Prerequisites

- Python 3.8+
- Node.js 14+
- PostgreSQL 13+
- Docker (for code execution feature)

## Installation

### Backend Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/data-science-platform.git
   cd data-science-platform
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the project root
   - Add the following variables:
     ```
     SECRET_KEY=your_secret_key
     DB_NAME=your_db_name
     DB_USER=your_db_user
     DB_PASSWORD=your_db_password
     DB_HOST=localhost
     DB_PORT=5432
     ```

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

7. Start the Django server:
   ```
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Start the React development server:
   ```
   npm start
   ```

## Usage

- Access the Django admin interface at `http://localhost:8000/admin/`
- The API will be available at `http://localhost:8000/api/`
- The React frontend will be served at `http://localhost:3000`

## API Endpoints

- User Registration: `POST /api/users/register/`
- User Login: `POST /api/users/login/`
- Questions List: `GET /api/questions/`
- Submit Answer: `POST /api/questions/{id}/submit/`

For detailed API documentation, run the server and visit `http://localhost:8000/api/docs/`

## Development

To contribute to this project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## Testing

Run backend tests:
```
python manage.py test
```

Run frontend tests:
```
cd frontend
npm test
```

## Deployment

Deployment instructions will be added in future updates.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

