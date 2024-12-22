# **Doctor Appointment System (DAS)**

**"Doctors Within Reach, Your Path to Wellness Starts Here."**

---

### **Project Overview**
The **Doctor Appointment System** is a web-based application designed to simplify and enhance the operational processes of a healthcare clinic. It offers core functionalities such as patient online reservation, user role-based access control, and appointment scheduling. This project is developed using Agile methodology to ensure iterative development and efficient delivery.

---

### **Features at a Glance**
| Feature                       | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| Patient Online Reservation    | Book appointments easily via a user-friendly interface.                     |
| Role-Based Access Control     | Restricted access based on user roles (Patient, Doctor, Admin).              |
| Appointment Scheduling        | View available slots and book/manage appointments.                          |
| User Authentication           | Secure login, logout, and registration functionality.                        |
| Profile Management            | Update user details and upload profile pictures.                            |
| Appointment Management        | Create, approve, cancel, and complete appointments.                          |
| Admin Management              | Admins can add, view, and manage doctor details.                             |
| Reports                       | Generate appointment or doctor reports with specific filters.                |
| Responsive Design             | Optimized for all devices using Bootstrap.                                   |
| Security                      | Implements CSRF protection and secure access decorators.                     |

---

### **Detailed Features**
1. **Patient Online Reservation**
   - Allows patients to book appointments through an intuitive interface.

2. **Role-Based Access Control (RBAC)**
   - Different user roles (e.g., Patient, Doctor, Admin) with restricted access levels.

3. **Appointment Scheduling**
   - Enables patients to view available slots and book appointments.
   - Doctors and nurses can manage schedules effectively.

4. **User Authentication**
   - User login and logout functionality.
   - User registration for doctors.

5. **User Profile Management**
   - Users can view and update their profile details.
   - Profile picture upload functionality.

6. **Appointment Management**
   - Users can create appointments with doctors.
   - Doctors can view, approve, cancel, and complete appointments.
   - Doctors can add remarks, prescribe medicines, and recommend tests for appointments.

7. **Admin Management**
   - Admin can add, view, and manage doctors.
   - Admin can search for doctors by name or mobile number.
   - Admin can view detailed information about doctors, including their specialization and contact details.

8. **Specialization Management**
   - Admin can add and manage specializations for doctors.

9. **Reports**
   - Admin can generate reports of doctors registered between specific dates.
   - Doctors can view appointments filtered by status (new, approved, cancelled, completed).

10. **Pagination**
   - Pagination is implemented for viewing lists of appointments to enhance user experience.

11. **Messaging and Notifications**
   - Success and error messages are displayed to users for various actions like profile updates, appointment creation, etc.

12. **Static Content Management**
   - Admin can update website details such as page title, address, about us, email, and mobile number.

13. **Responsive Design**
   - The application uses Bootstrap for responsive design, ensuring it works well on different devices.

14. **Security**
   - CSRF protection is implemented for forms.
   - Login required decorators are used to protect certain views.

---

### **Agile Workflow**
This project follows **Agile methodology** with:
- **Sprint Planning**: Tasks are divided into sprints with detailed breakdowns.  
- **Product Backlog**: Maintains prioritized user stories and tasks.  
- **Scrum Meetings**: Regular meetings for planning, feedback, and retrospectives.  
- **GitHub Integration**: Issues, branches, and pull requests are aligned with sprint tasks.  

---

### **Repository Structure**
```
doctorappointment/
├── .gitignore
├── docs/
|   ├──
|   ├──
├── README.md
├── requirements.txt
├── manage.py
├── doctorappointment/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── dasapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── ...
├── static/
│   ├── css/
│   │   ├── style.css
│   │   └── ...
│   ├── js/
│   │   ├── main.js
│   │   └── ...
│   ├── img/
│   │   ├── image-1.jpg
│   │   └── ...
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── admin/
│   │   ├── adminhome.html
│   │   └── ...
│   ├── user/
│   │   ├── userhome.html
│   │   └── ...
└── venv/
```

---

### **Technology Stack**
- **Project Name**: Doctor Appointments System Project in Python Django
- **Language Used**: Python
- **Framework Used**: Django
- **Database**: MySQL
- **User Interface Design**: HTML, AJAX, JQUERY, JavaScript
- **Web Browser**: Mozilla, Google Chrome, IE8, Opera
- **IDE**: VS Code

---

### **Setup Instructions**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ziadelshazly22/SWE-Project-Doctor-Appointment-System-DAS.git
   cd SWE-Project-Doctor-Appointment-System-DAS
   ```

2. **Database Setup**:
   - Open MySQL and create a database `docaspythondb`.
   - Import the SQL file available in the `MySQL File` folder.

3. **Install Dependencies**:
   - Create and activate a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

4. **Apply Migrations and Create Superuser**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Run the Application**:
   - Open your terminal and navigate to the project directory:
     ```bash
     cd project_path/doctorappointment/dasapp
     python manage.py runserver
     ```
   - Access the application at: [http://127.0.0.1:8000](http://127.0.0.1:8000).

6. **Run Tests**:
   ```bash
   python manage.py test
   ```

---

### **Documentation**
All project-related documents are available in the `docs/` folder, including:
- **Requirements**: Detailed user and system requirements.
- **Design**: Architecture diagrams, class diagrams, and wireframes.
- **User Manual**: Step-by-step usage guide for the system.
- **Agile Reports**: Sprint plans, retrospectives, and burndown charts.

---

### **Contributing**
We welcome contributions! Follow these steps:

1. Fork the repository.  
2. Create a feature branch:
   ```bash
   git checkout -b feature-[feature-name]
   ```
3. Commit your changes and push the branch:
   ```bash
   git push origin feature-[feature-name]
   ```
4. Submit a pull request to the `dev` branch for review.

- Please adhere to **PEP 8** coding standards.
- Ensure all changes pass the existing test suite.

---

### **Project Team**
| Name                 |
|----------------------|
| [Ziad ElShazly]      | 
| [Mohamed Magdy]      | 
| [Katreen William]    | 
| [Merna Wesa]         |

---

**"Together, simplifying healthcare one click at a time."**
