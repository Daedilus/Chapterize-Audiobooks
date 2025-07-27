import time
from pathlib import Path
from batch_chapterize import run_chapterize

# Directory paths
INPUT_DIR = Path("input")
PROCESSED_DIR = Path("processed")

# Supported file types
SUPPORTED_FORMATS = [".mp3", ".m4b"]

# Make sure processed dir exists
PROCESSED_DIR.mkdir(exist_ok=True)

def main():
    print("👀 Watching for new audiobook files (.mp3, .m4b) in 'input/'...")

    while True:
        # Find new supported files that haven't been processed
        files_to_process = [
            f for f in INPUT_DIR.iterdir()
            if f.suffix.lower() in SUPPORTED_FORMATS
            and f.is_file()
            and not (PROCESSED_DIR / f.name).exists()
        ]

        for file in files_to_process:
            try:
                run_chapterize(file)
                file.rename(PROCESSED_DIR / file.name)
                print(f"✅ Finished and moved: {file.name}")
            except Exception as e:
                print(f"❌ Error processing {file.name}: {e}")

        time.sleep(10)  # Wait 10 seconds before next scan

if __name__ == "__main__":
    main()
