from pathlib import Path
from datetime import datetime
from typing import Union

def save_with_timestamp(text: str, out_dir: Union[Path, str] = Path("out"), date_filename_format: str = "%Y-%m-%d.txt") -> Path:
    """
    文字列を日時付きで上書きせずに保存する。

    保存ルール:
    - デフォルトの出力ディレクトリはプロジェクトルートの 'out'。
    - ファイル名は実行日のフォーマット (デフォルト: YYYY-MM-DD.txt)。
    - ファイルが存在しなければ作成し、存在すれば追記する。
    - 各エントリは [ISOタイムスタンプ] の行と本文、空行で区切られる。

    引数:
        text: 保存する文字列（末尾改行は自動で処理される）。
        out_dir: 出力ディレクトリ（Path または文字列）。デフォルト "out"。
        date_filename_format: ファイル名の日時フォーマット（datetime.strftime 用）。

    戻り値:
        保存先の Path オブジェクト。

    例:
        >>> save_with_timestamp("これはテストです。")
        PosixPath('out/2025-10-23.txt')
    """
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    filename = datetime.now().strftime(date_filename_format)
    file_path = out_path / filename

    timestamp = datetime.now().isoformat(sep=" ", timespec="seconds")
    entry = f"[{timestamp}]\n{text.rstrip()}\n\n"

    # テキストを追記モードで書き込む（上書きしない）
    with file_path.open("a", encoding="utf-8") as f:
        f.write(entry)

    return file_path