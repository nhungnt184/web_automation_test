# Automation Test với Python + Playwright

## Yêu cầu
- Python 3.9+ (Windows / Linux / macOS)
- pip (Python package manager)

## Cài đặt nhanh (không dùng môi trường ảo)
```bash
pip install -r requirements.txt
playwright install
pytest -v
```

## Cài đặt chuyên nghiệp (dùng môi trường ảo)

### Windows (CMD)
```bat
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install
pytest -v
```

### Windows (PowerShell)
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install
pytest -v
```

### Linux / macOS (bash/zsh)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install
pytest -v
```

## Chạy test
Chạy toàn bộ test:
```bash
pytest -v
```

Chạy một test cụ thể:
```bash
pytest tests/test_example.py::test_example -v
```
