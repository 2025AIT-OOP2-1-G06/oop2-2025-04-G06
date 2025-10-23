from pathlib import Path

import ffmpeg


def record_pc_audio(duration_s: int, output_file: Path) -> None:
    """N 秒間, PC のマイクの音声を録音して保存する

    Note: macOS のみ動作する

    Args:
        duration_s (int): 秒数
        output_file (Path): 出力ファイルパス

    """
    (
        ffmpeg.input(":0", f="avfoundation", t=duration_s)
        .output(filename=output_file, acodec="pcm_s16le", ar="44100", ac=1)
        .run(overwrite_output=True)
    )
