# Indian Constitution Web App

A comprehensive, educational web application exploring the Indian Constitution, built with Django.

## Features
-   **Historical Background**: From 1773 to 1947 and beyond.
-   **Structure**: Detailed view of Parts, Articles, and Schedules.
-   **Amendments**: Chronological list of amendments up to 2025.
-   **Judgments**: Landmark Supreme Court cases.
-   **Dr. B. R. Ambedkar**: Dedicated acknowledgment.

## Setup
1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Migrate Database**:
    ```bash
    python manage.py migrate
    ```
3.  **Run Server**:
    ```bash
    python manage.py runserver
    ```

## Content Updates
-   To add new amendments, use the Django Admin interface or update the `seed_data.py` script.
-   Content is current as of 2025.
