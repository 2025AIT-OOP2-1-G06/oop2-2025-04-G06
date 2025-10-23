from pathlib import Path
from typing import Union

# mlx-whisperをインストールしていることを前提とします
# 既存のファイル (onsei.py, transcribe.py) から mlx_whisper の使用を確認
try:
    import mlx_whisper
except ImportError:
    print("Error: mlx-whisper is not installed. Please install it with 'pip install mlx-whisper'.")
    # 実行時にエラーを避けるため、ダミー関数やexitなどは避け、ここでは単にpass
    # 実際の運用では環境設定が必要です
    pass


def transcribe_from_audio(audio_path: Union[str, Path]) -> str:
    """
    指定された音声ファイルパスから音声ファイルを読み込み、文字起こしを実行します。

    Args:
        audio_path (Union[str, Path]): 
            文字起こしする音声ファイル（例: .wav, .mp3など）のパス。
            strまたはPathオブジェクトを受け入れます。

    Returns:
        str: 文字起こしされたテキスト。文字起こしに失敗した場合は空文字列を返します。
    
    Notes:
        - 文字起こしには 'whisper-base-mlx' モデルを使用します。
        - mlx-whisperライブラリがインストールされている必要があります。
        - 音声データ（numpy arrayなど）を直接受け取る仕様も考えられますが、
          ここでは「音声ファイルを受け取り」の要件に絞り、ファイルパスを受け取ります。
    """
    
    path_obj = Path(audio_path)
    
    if not path_obj.exists():
        print(f"エラー: 指定された音声ファイルが見つかりません: {audio_path}")
        return ""

    if path_obj.is_dir():
        print(f"エラー: 指定されたパスはファイルではなくディレクトリです: {audio_path}")
        return ""
        
    try:
        # mlx_whisper.transcribeを使用して音声ファイルを文字起こし
        # path_or_hf_repo="whisper-base-mlx" は onsei.py や transcribe.py の初期ファイルから踏襲
        result = mlx_whisper.transcribe(
            str(path_obj), 
            path_or_hf_repo="whisper-base-mlx"
        )
        
        # result は辞書型 ({'text': '...' ...}) のため、テキスト部分を抽出
        transcribed_text = result.get('text', '').strip()
        
        # デバッグ/確認用に出力（本番利用時は必要に応じて削除/ログ出力に変更）
        print(f"文字起こしに成功しました。ファイル: {path_obj.name}")
        
        return transcribed_text
        
    except NameError:
        # mlx_whisperのインポート失敗時のエラーハンドリング
        print("エラー: mlx_whisperがインポートされていません。環境を確認してください。")
        return ""
    except Exception as e:
        # その他の文字起こし中のエラーをキャッチ
        print(f"文字起こし中に予期せぬエラーが発生しました: {e}")
        return ""

# 実行例（main.pyから利用されることを想定しているため、ここではコメントアウト）
# if __name__ == '__main__':
#     # 実際には main.py の処理で生成されたパスを指定します
#     # 例:
#     # from paths import DIR_OUT
#     # path_audio = DIR_OUT / "record_audio.wav"
#     # text = transcribe_from_audio(path_audio)
#     # print(f"最終的な文字起こし結果:\n{text}")
#     pass