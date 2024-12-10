# Listify - Todo Manager 📋✨

Listify is a simple and efficient todo manager built with Flask for the backend and Bootstrap for the frontend. It helps you keep track of your tasks and stay organized. 🕒🗓️

## Features 🚀

- **Task Management**: Add, edit, and delete tasks. ➕🖋️❌
- **Task Prioritization**: Mark tasks as high, medium, or low priority. 🔥🔄💧
- **Task Completion**: Mark tasks as completed. ✅
- **Responsive Design**: Built with Bootstrap for a mobile-friendly experience. 📱💻

## Screenshots 📸

![image](https://github.com/user-attachments/assets/e48affb5-6c97-4333-b2e1-0a5548611c05)

## Installation 🛠️

### Prerequisites 📦

- Python 3.x
- pip (Python package installer)

### Steps 🚶

1. **Clone the repository**:
    ```bash
    git clone https://github.com/udaygiri/Listify.git
    cd Listify
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up the environment variables**:
    Create a `.env` file in the root directory and add the following:
    ```env
    SECRET_KEY=your_secret_key
    DATABASE_URL=sqlite:///listify.db
    ```

6. **Initialize the database**:
    ```bash
    flask db upgrade
    ```

7. **Run the application**:
    ```bash
    flask run
    ```

8. **Access the application**:
    Open your browser and go to `http://127.0.0.1:5000/`. 🌐

## Usage 📝

1. **Add a Task**:
    - Click on the "Add Task" button.
    - Fill in the task details and click "Save". 📝

2. **Edit a Task**:
    - Click on the "Edit" button next to the task you want to modify.
    - Make the necessary changes and click "Save". 🖋️

3. **Delete a Task**:
    - Click on the "Delete" button next to the task you want to remove. ❌

4. **Mark a Task as Completed**:
    - Click on the checkbox next to the task to mark it as completed. ✅

## Live Demo 🌍

Check out the live demo of Listify [here](https://listify-bswb.onrender.com/).

## Contributing 🤝

Contributions are welcome! Please follow these steps:

1. Fork the repository. 🍴
2. Create a new branch (`git checkout -b feature-branch`). 🌿
3. Make your changes and commit them (`git commit -am 'Add new feature'`). 📦
4. Push to the branch (`git push origin feature-branch`). 📤
5. Create a new Pull Request. 🔃

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- Thanks to the Flask and Bootstrap communities for their excellent documentation and support. 📚
- Inspired by various to-do list applications. 💡

## Contact 📧

For any questions or suggestions, feel free to open an issue or contact me directly at [My Email](udaygiri.aparnathi5@gmail.com). 📬
