import os
import subprocess
from pathlib import Path

INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")
SCRIPT = "chapterize_ab.py"  # The main script to call

# Allowed audiobook formats
SUPPORTED_FORMATS = [".mp3", ".m4b"]

def run_chapterize(audiobook_path: Path):
    print(f"🎧 Processing {audiobook_path.name}")

    # Create output subfolder named after file stem
    output_subdir = OUTPUT_DIR / audiobook_path.stem
    output_subdir.mkdir(parents=True, exist_ok=True)

    # Copy audiobook into the working output dir
    working_file = output_subdir / audiobook_path.name
    working_file.write_bytes(audiobook_path.read_bytes())

    # Build command to invoke chapterize script
    cmd = [
        "python", SCRIPT,
        str(working_file),
        "--title", audiobook_path.stem,
        "--language", "en-us"
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"✅ Done: {audiobook_path.name}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to process {audiobook_path.name}: {e}")

def main():
    if not INPUT_DIR.exists():
        print(f"❌ Input directory '{INPUT_DIR}' does not exist.")
        return

    input_files = [
        f for f in INPUT_DIR.iterdir()
        if f.suffix.lower() in SUPPORTED_FORMATS and f.is_file()
    ]

    if not input_files:
        print("📭 No supported audiobook files found in input/")
        return

    for file in input_files:
        run_chapterize(file)

if __name__ == "__main__":
    main()
