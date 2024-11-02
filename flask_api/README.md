# PYTHON PROJECT 

### Setting Up and Using a Virtual Environment

1. **Create a Virtual Environment**:
   To isolate project dependencies, create a virtual environment in your project directory. Replace `venv` with any name you like for your environment.

   ```bash
   python -m venv venv
   ```

   This creates a `venv` directory with a self-contained Python environment, including its own `pip`.

2. **Activate the Virtual Environment**:
   Activation ensures that any packages you install only apply to this project environment. The command varies by OS:

   - **On Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - **On macOS/Linux**:

     ```bash
     source venv/bin/activate
     ```

   After activation, you should see `(venv)` at the beginning of your terminal prompt, indicating the environment is active.

3. **Install Packages from `requirements.txt`**:
   Use this command to install all dependencies listed in the `requirements.txt` file for your project.

   ```bash
   pip install -r requirements.txt
   ```

   This is particularly useful for setting up an existing project with a known list of dependencies.

4. **Deactivate the Virtual Environment**:
   To exit the virtual environment and return to the global Python environment, run:

   ```bash
   deactivate
   ```

---

### Running a Flask Application

1. **Run the Flask Application**:
   Assuming your Flask app file is `app.py`, start the server using:

   ```bash
   python app.py
   ```

   By default, this starts the Flask app on `http://127.0.0.1:5000`.

2. **Run Flask on a Different Port**:
   If port 5000 is unavailable, specify an alternative port (e.g., 5001) in the code:

   ```python
   if __name__ == '__main__':
       app.run(debug=True, port=5001)
   ```

   Then run the app again:

   ```bash
   python app.py
   ```

3. **Check Port Usage on Windows**:
   If a port is in use, check for the process ID (PID) and stop it if necessary.

   ```bash
   netstat -aon | findstr :5000
   ```

   After identifying the PID, stop the process with:

   ```bash
   taskkill /PID <PID> /F
   ```

   Replace `<PID>` with the actual process ID.

---

### Updating `pip` (Optional)

If you receive a message about a `pip` update, upgrade `pip` using:

```bash
python -m pip install --upgrade pip
```

This command ensures you have the latest version of `pip`, which can help avoid compatibility issues.