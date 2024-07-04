# Instagram Subscriptions and Followers Comparison Script

## Overview

This script compares the followers and followees of an Instagram profile. It uses the `instaloader` library to fetch the data and `pandas` for data manipulation. The script requires user login credentials and the target profile's username.

## Prerequisites

Before running the script, ensure you have the following installed:
- Python 3.x
- Pandas
- NumPy
- Instaloader

## Installation

1. **Install Python and required libraries:**

    If you haven't installed Python, download and install it from [python.org](https://www.python.org/).

    Install the required libraries using pip:

    ```bash
    pip install pandas numpy instaloader
    ```
## Notes

- Ensure your Instagram credentials are correct and that you have permission to access the target profile's data.
- Handle your Instagram credentials securely and avoid sharing them.

## Troubleshooting

- **Login Issues:** Ensure your username and password are correct.
- **Element Not Found:** Ensure the profile exists and is accessible.
- **Data Mismatch:** Verify the data by checking the generated CSV file.
