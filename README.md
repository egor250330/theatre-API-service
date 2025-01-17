# theatre-API-service

Theatre-API-service is a Django-based API service for managing theatres, plays, actors, and genres. This application provides endpoints to create, update, and retrieve data about theatres, plays, actors, and genres, allowing you to easily manage relationships between them.

## Functionality

This API service offers the following main features:
- **Theatre Management**: Manage theatres, including adding new theatres and linking them with plays.
- **Play Management**: Create, update, and delete plays, with the ability to associate them with specific actors and genres.
- **Actor Management**: Add actors and link them with multiple plays.
- **Genre Management**: Define genres and link them with plays to categorize them.
- **User Authentication**: Allows user registration and login with JWT for secure access to the API.
- **Admin Panel Access**: Admins can manage all entities through the Django admin panel.

## How to Run the Application

1. **Clone the Repository**:
    `git clone https://github.com/egor250330/theatre-API-service.git`
2. **Create a Virtual Environment**:
    `python -m venv venv`
3. **Activate the Virtual Environment**:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
4. **Install Dependencies**:
    `pip install -r requirements.txt`
5. **Set Up Environment Variables**: Create a `.env` file in the root of the project based on `env.sample` and specify the following variables:
   - `SECRET_KEY`: Django secret key for production
   - `DEBUG`: Set to `False` for production
   - `DATABASE_URL`: Database connection URL
6. **Apply Migrations**:
    `python manage.py migrate`
7. **Create a Superuser Account**:
    `python manage.py createsuperuser`
8. **Run the Server**:
    `python manage.py runserver`
9. **Loading Initial Data**:
    'python manage.py loaddata theatre/fixtures/initial_data.json'
10. **Make sure that Doker is running**
11. ## Setup Instructions

1. Copy the `env.sample` file to `.env`.
2. Update the variables in the `.env` file with your actual configuration values.

