# SkinRave Hi-Lo Statistics

Simple Python project that collects statistics from the SkinRave Hi-Lo game using OCR (Tesseract).

## Files

- **main.py** – Starts Chrome, reads cards, and records statistics.
- **hledani_souradnic.py** – Selects the OCR capture region.
- **position.py** – Prints current mouse coordinates.
- **null_stats.py** – Resets all collected statistics.
- **stt.py** – Displays statistics in a formatted table.
- **stats.json** – Stores collected data.

## Requirements

- Python 3
- Tesseract OCR
- Google Chrome
- Required Python libraries:
  - pyautogui
  - keyboard
  - pytesseract
  - opencv-python
  - numpy
  - mss
  - rich

Install dependencies:


pip install pyautogui keyboard pytesseract opencv-python numpy mss rich


## Usage

1. Install Tesseract OCR.
2. Set the correct capture region using `hledani_souradnic.py`.
3. Update the `region` values in `main.py`.
4. Run `main.py` to start collecting statistics.
5. Press **Right Shift** to stop.
6. Run `stt.py` to view the results.