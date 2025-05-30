# Text Summarizer App

A Streamlit-based web application that provides text summarization using the BART-large-CNN model from Hugging Face. This application allows users to input long text and receive concise, meaningful summaries.

## Features

- Clean and intuitive user interface
- Powered by state-of-the-art BART-large-CNN model
- Handles long texts through automatic chunking
- Shows summary statistics (compression ratio, text lengths)
- Error handling and input validation
- CI pipeline with automated testing and linting

## Prerequisites

- Python 3.9 or higher
- pip (Python package installer)
- Git (for version control)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment (recommended):
```bash
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Enter or paste your text in the input area

4. Click "Generate Summary" to get the summarized version

## Project Structure

```
├── app.py              # Main Streamlit application
├── test_app.py         # Unit tests
├── requirements.txt    # Project dependencies
├── .github/
│   └── workflows/      # CI pipeline configuration
│       └── deploy.yml
└── README.md          # This file
```

## Development

### Running Tests

Run the test suite using:
```bash
python -m unittest test_app.py
```

### Code Quality

The project uses:
- flake8 for code linting
- black for code formatting

Run the linters:
```bash
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
black . --check
```

## CI Pipeline

The project includes a GitHub Actions CI pipeline that:
- Runs on every push and pull request
- Executes unit tests
- Performs code linting
- Checks code formatting

## Deployment

### Local Deployment
1. Ensure all dependencies are installed
2. Run `streamlit run app.py`
3. Access the app at http://localhost:8501

### Streamlit Cloud Deployment
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy the app

## Dependencies

- streamlit==1.32.0
- transformers==4.38.2
- torch==2.2.1
- sentencepiece==0.2.0
- protobuf==4.25.3
- accelerate==0.27.2

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

