from datetime import datetime
from pathlib import Path

def save_with_timestamp(text: str, output_dir: Path = Path("out")) -> None:
    """
    現在のタイムスタンプを用いたファイル名で、指定された文字列を.txtファイルに保存します。
    ファイルは上書きされず、毎回新しいファイルが作成されます。

    Parameters:
    - text (str): 保存する文字列
    - output_dir (Path): 出力先ディレクトリ（デフォルトは 'out'）
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = output_dir / f"transcription_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)