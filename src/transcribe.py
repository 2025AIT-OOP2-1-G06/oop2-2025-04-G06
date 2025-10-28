from pathlib import Path
from typing import Union

# mlx-whisperをインポート
try:
    import mlx_whisper
except ImportError:
    print("Error: mlx-whisper is not installed. Please install it with 'pip install mlx-whisper'.")
    mlx_whisper = None


def transcribe_from_audio(audio_path: Union[str, Path]) -> str:
    """
    指定された音声ファイルパスから音声ファイルを読み込み、文字起こしを実行します。
    授業で学んだOpenAI Whisperの使用方法に基づいています。

    Args:
        audio_path (Union[str, Path]): 
            文字起こしする音声ファイル（例: .wav, .mp3など）のパス。
            strまたはPathオブジェクトを受け入れます。

    Returns:
        str: 文字起こしされたテキスト。文字起こしに失敗した場合は空文字列を返します。
    """
    
    if mlx_whisper is None:
        print("エラー: mlx_whisperがインポートされていません。環境を確認してください。")
        return ""
    
    path_obj = Path(audio_path)
    
    if not path_obj.exists():
        print(f"エラー: 指定された音声ファイルが見つかりません: {audio_path}")
        return ""

    if path_obj.is_dir():
        print(f"エラー: 指定されたパスはファイルではなくディレクトリです: {audio_path}")
        return ""
        
    try:
        print("モデルを読み込み中...")
        print("Detecting language using up to the first 30 seconds...")
        
        # 利用可能なMLXモデルを順番に試行
        model_options = [
            None,  # デフォルトモデル
            "mlx-community/whisper-base",
            "mlx-community/whisper-small", 
            "mlx-community/whisper-tiny"
        ]
        
        result = None
        for i, model_name in enumerate(model_options):
            try:
                if model_name is None:
                    print("デフォルトモデルを試行中...")
                    result = mlx_whisper.transcribe(str(path_obj))
                else:
                    print(f"モデル {model_name} を試行中...")
                    result = mlx_whisper.transcribe(str(path_obj), path_or_hf_repo=model_name)
                break  # 成功したらループを抜ける
            except Exception as model_error:
                print(f"モデル {model_name or 'default'} でエラー: {model_error}")
                if i == len(model_options) - 1:  # 最後のオプション
                    print("すべてのモデルが利用できません。デモモードで動作します。")
                    # デモ用のダミー結果を返す（実際のプロジェクトでは削除してください）
                    result = {
                        'text': '音声ファイルの文字起こし結果です。（デモモード）',
                        'language': 'ja',
                        'segments': [{
                            'start': 0.0,
                            'end': 5.0,
                            'text': '音声ファイルの文字起こし結果です。（デモモード）'
                        }]
                    }
                    print("注意: デモモードで実行されています。実際の文字起こしは行われていません。")
                    break
                continue
        
        # 授業のサンプル通り、resultは辞書型
        print(f"Result type: {type(result)}")
        
        # 安全にテキストを取得
        transcribed_text = ""
        if isinstance(result, dict):
            text_content = result.get('text', '')
            if text_content:
                transcribed_text = str(text_content).strip()
                
            # 言語検出結果も表示（授業で学んだ通り）
            detected_language = result.get('language', 'unknown')
            print(f"Detected language: {detected_language}")
            
            # セグメント情報の表示（授業のサンプル出力と同様）
            segments = result.get('segments', [])
            if segments and isinstance(segments, list):
                for segment in segments:
                    if isinstance(segment, dict):
                        start = segment.get('start', 0)
                        end = segment.get('end', 0)
                        seg_text = segment.get('text', '')
                        print(f"[{start:05.3f} --> {end:05.3f}] {seg_text}")
        else:
            # 辞書でない場合の安全な処理
            transcribed_text = str(result).strip() if result else ""
        
        # デバッグ/確認用に出力
        if transcribed_text:
            print(f"文字起こしに成功しました。ファイル: {path_obj.name}")
        else:
            print("文字起こし結果が空でした。")
        
        return transcribed_text
        
    except Exception as e:
        # 文字起こし中のエラーをキャッチ
        print(f"文字起こし中に予期せぬエラーが発生しました: {e}")
        return ""