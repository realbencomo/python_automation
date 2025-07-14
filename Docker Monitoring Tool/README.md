# Log Monitor Application

A simple Python-based log monitoring tool that watches specified log files for defined keywords and sends alerts via email and Telegram when matches are found.

## Features

- Monitors one or multiple log files in real time
- Sends alerts via:
  - Email
  - Telegram
- Configurable scan interval and keywords
- Dockerized for easy deployment

## Requirements

- Python 3.8+
- `requests` library
- Docker (optional for container deployment)

## Installation

### Running Locally

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/log-monitor-app.git
    cd log-monitor-app
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure `config.py` with your log files, keywords, scan interval, and alert credentials.

4. Run the application:
    ```bash
    python main.py
    ```

### Running with Docker

1. Build the Docker image:
    ```bash
    docker build -t log-monitor-app .
    ```

2. Run the container:
    ```bash
    docker run -v /path/to/your/logs:/app/logs -e CONFIG_ENV=production log-monitor-app
    ```

## Configuration

Edit `config.py` to set:

- `LOG_FILES`: List of log file paths.
- `KEYWORDS`: List of keywords to monitor.
- `SCAN_INTERVAL`: Time interval in seconds between scans.
- Email and Telegram credentials.

## License

MIT License

## Author

Jorge Bencomo - github.com/realbencomo
