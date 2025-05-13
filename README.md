# SocialMedia-REST

## Overview  
**SocialMedia-REST** is a RESTful API application built with Python, designed to support the functionality of a social media platform. It provides endpoints for managing user accounts, posts, comments, likes, and other essential features of a modern social media application.

This project is ideal for learning and implementing RESTful API design principles, authentication mechanisms, and efficient backend development.

---

## Features  
- **User Management**:  
  - Sign up, log in, and manage user profiles.  
  - Secure authentication using tokens or session-based mechanisms.  

- **Post and Comment Management**:  
  - Create, edit, and delete posts.  
  - Add comments to posts and manage comment threads.  

- **Interaction Features**:  
  - Like and unlike posts or comments.  
  - Follow and unfollow users.  

- **RESTful Design**:  
  - Adheres to RESTful principles for clean, predictable, and scalable API design.  
  - Proper use of HTTP methods (GET, POST, PUT, DELETE) and status codes.  

- **Scalable Architecture**:  
  - Built with scalability and maintainability in mind, making it suitable for real-world applications.  

---

## Technology Stack  
This project is developed using:  
- **Python**: Backend logic, API implementation, and core functionalities.  
- **Framework**: Django REST Framework (DRF) for API development.  
- **HTML** *(if applicable)*: For minimal frontend components or admin panel customization.  

---

## Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/BehradShirkavand/SocialMedia-REST.git
   cd SocialMedia-REST
   ```

2. Create and activate a virtual environment:  
   ```bash
   python -m virtualenv venv
   .\venv\Scripts\activate
   ```

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations to set up the database:  
   ```bash
   python manage.py migrate
   ```

5. Start the development server:  
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints  

### User Authentication
- **POST /api/register**: Create a new user.  
- **POST /api/login**: Authenticate and log in a user.  

### Post Management  
- **GET /api/posts/**: Retrieve all posts.  
- **POST /api/posts/**: Create a new post.  
- **PUT /api/posts/{id}/**: Update a post.  
- **DELETE /api/posts/{id}/**: Delete a post.  

### Comment Management  
- **GET /api/posts/{id}/comments/**: Retrieve comments for a post.  
- **POST /api/posts/{id}/comments/**: Add a comment to a post.  

### Like Management  
- **POST /api/posts/{id}/like/**: Like a post.  
- **DELETE /api/posts/{id}/like/**: Unlike a post.  

### Follow Management  
- **POST /api/users/{id}/follow/**: Follow a user.  
- **DELETE /api/users/{id}/follow/**: Unfollow a user.  

---

## Contribution  

We welcome contributions to improve this project!  

1. Fork the repository.  
2. Create a feature branch:  
   ```bash
   git checkout -b feature-name
   ```  
3. Commit your changes:  
   ```bash
   git commit -m "Description of changes"
   ```  
4. Push to your branch:  
   ```bash
   git push origin feature-name
   ```  
5. Open a pull request.  

---

## License  
This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it as needed.
