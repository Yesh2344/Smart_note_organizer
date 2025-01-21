# Student Task Manager

## Overview

Student Task Manager is a web-based application built with Python and Flask. It provides a simple and intuitive interface for students to manage their tasks, helping them stay organized and productive.

## Features

- Add tasks with title, description, and due date
- View all tasks sorted by due date
- Mark tasks as completed or uncompleted
- Delete tasks
- Responsive design for both desktop and mobile browsers
- Data persistence using SQLite database

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/student-task-manager.git
   cd student-task-manager
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install flask flask-sqlalchemy
   ```

## Usage

1. Run the application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://127.0.0.1:5000/`

3. Use the interface to add, view, complete, and delete tasks.

## Project Structure

```
student-task-manager/
│
├── app.py              # Main application file
├── tasks.db            # SQLite database (created automatically)
├── README.md           # This file
└── templates/
    └── index.html      # HTML template for the web interface
```

## Customization

You can customize the application by:

- Modifying the HTML and CSS in `templates/index.html` to change the look and feel
- Adding new routes and functionality in `app.py`
- Extending the `Task` model in `app.py` to include more fields

## Contributing

Contributions to the Student Task Manager are welcome. Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

If you have any questions or feedback, please contact:

Your Name - email@example.com

Project Link: [https://github.com/yourusername/student-task-manager](https://github.com/yourusername/student-task-manager)
```

This README provides a comprehensive guide for anyone who wants to use or contribute to the Student Task Manager project. Remember to replace "yourusername" with your actual GitHub username and update the contact information before publishing the project.
