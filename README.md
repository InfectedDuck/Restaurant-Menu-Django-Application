# Little Lemon Restaurant

Welcome to the Little Lemon Restaurant project! This Django-based application provides a menu management system where users can view menu items, see details about each item, and explore additional information about the restaurant.

## Features

- **Home Page**: A landing page for the restaurant.
- **Menu Page**: Displays a list of all menu items.
- **Menu Item Detail Page**: Provides detailed information about a specific menu item.
- **About Page**: Offers information about the restaurant.
- **Booking Page**: (Optional) Allows users to make reservations or bookings.

## Tech Stack

- **Django**: A high-level Python web framework that simplifies the development of dynamic web applications.
- **HTML/CSS**: Used for front-end design and styling.
- **Python**: The programming language used for the backend.

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/your-username/little-lemon.git
    cd little-lemon
    ```

2. **Create and Activate a Virtual Environment**:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```


3. **Apply Migrations**:

    ```bash
    python manage.py migrate
    ```

4. **Run the Development Server**:

    ```bash
    python manage.py runserver
    ```

5. **Access the Application**: Open your browser and go to `http://127.0.0.1:8000/`.

## File Structure

- **`admin.py`**: Registers the `MenuItem` model with the Django admin interface.
- **`apps.py`**: Configures the application settings.
- **`models.py`**: Defines the `MenuItem` model with fields for name, price, description, and image.
- **`urls.py`**: Configures URL routing for different views.
- **`views.py`**: Contains the view functions for handling requests and rendering templates.
- **`settings.py`**: Contains project settings (not shown here but typically includes configurations such as database settings, installed apps, etc.).
- **`manage.py`**: A command-line utility that lets you interact with this Django project.

## CSS Styling

The project includes the following CSS styles for general layout and menu page styling:

- **General Styles**: Defines the look and feel of the header, footer, and body.
- **Menu Page Styles**: Styles for the menu items, including hover effects and image formatting.

## Contributing

If you wish to contribute to this project, please follow these steps:


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.
