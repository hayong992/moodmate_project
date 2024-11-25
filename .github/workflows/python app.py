name: Python application

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run Python script
      run: python app.py  # 'your_script.py' 대신 'app.py' 사용

        echo "Running Python script"
        python app.py  # 실제 파일 이름으로 변경
      env:
        OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}  # GitHub Secrets에서 API 키 불러오기

