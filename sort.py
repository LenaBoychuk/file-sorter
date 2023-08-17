import sys
from pathlib import Path
import main
if __name__ == '__main__':
    path = sys.argv[1]
    print(f"Start in {path}")

    arg = Path(path)
    main.main(arg)
