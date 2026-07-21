# Student Stress Tracker

This project is a web-based Student Stress Tracking and Management system built using Django for the backend, HTML and Bootstrap for the frontend, and Chart.js for data visualization. The application allows students to log their daily stress levels, view analytics, and access resources for managing stress.

## Features

- User-friendly interface for logging daily stress inputs.
- Dashboard displaying recent entries and insights.
- Analytics page with visualizations of stress trends using Chart.js.
- Resources page offering tips and suggestions for student wellbeing.

## Technologies Used

- Python
- Django
- HTML
- Bootstrap
- Chart.js
- CSS

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd student-stress-tracker
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

6. Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

- Navigate to the stress log page to submit your daily stress levels.
- View the dashboard for insights into your stress patterns.
- Check the analytics page for visual representations of your stress data.
- Explore the resources page for helpful tips on managing stress.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.