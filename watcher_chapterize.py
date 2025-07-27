import time
from pathlib import Path
from batch_chapterize import run_chapterize

INPUT_DIR = Path("input")
PROCESSED_DIR = Path("processed")
PROCESSED_DIR.mkdir(exist_ok=True)

def main():
    print("👀 Watching for new MP3 files in 'input/'...")
    while True:
        mp3_files = list(INPUT_DIR.glob("*.mp3"))
        for mp3 in mp3_files:
            try:
                run_chapterize(mp3)
                mp3.rename(PROCESSED_DIR / mp3.name)
                print(f"✅ Processed and moved: {mp3.name}")
            except Exception as e:
                print(f"❌ Error processing {mp3.name}: {e}")
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    main()
