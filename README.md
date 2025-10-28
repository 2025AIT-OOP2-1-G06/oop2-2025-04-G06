# 音声録音・文字起こしアプリケーション

## 概要

このアプリケーションは、音声を録音して文字起こしを行い、結果をファイルに保存する機能を提供します。

## 機能

1. **音声録音**: 10秒間のPC音声を録音
2. **文字起こし**: 音声ファイルから文字起こしを実行
3. **結果保存**: 文字起こし結果をタイムスタンプ付きファイルに保存

## ファイル構成

```
src/
├── main.py          # メインの実行ファイル
├── record.py        # 音声録音用のファイル
├── transcribe.py    # 音声ファイル・データを文字起こしするファイル
├── save.py          # 文字列保存用のファイル
└── paths.py         # ディレクトリ管理

out/
├── record_audio.wav                    # 録音した音声ファイル
└── transcription_<タイムスタンプ>.txt  # 文字起こし結果の保存ファイル
```

## 使用方法

### 基本実行

```bash
python src/main.py
```

### 個別機能の使用

#### 1. 音声録音 (`record.py`)

```python
from pathlib import Path
from src.record import record_pc_audio

# 10秒間の音声を録音
output_path = Path("out/my_audio.wav")
record_pc_audio(duration_s=10, output_file=output_path)
```

#### 2. 文字起こし (`transcribe.py`)

```python
from pathlib import Path
from src.transcribe import transcribe_from_audio

# 音声ファイルから文字起こし
audio_path = Path("out/record_audio.wav")
text = transcribe_from_audio(audio_path)
print(f"文字起こし結果: {text}")
```

#### 3. 結果保存 (`save.py`)

```python
from pathlib import Path
from src.save import save_with_timestamp

# 文字列をタイムスタンプ付きファイルに保存
text = "これは文字起こしされたテキストです。"
save_with_timestamp(text, Path("out"))
```

## 出力例

### 音声ファイル
- ファイル名: `record_audio.wav`
- 形式: WAV (PCM 16bit, 44.1kHz, モノラル)
- 場所: `out/record_audio.wav`

### 文字起こし結果ファイル
- ファイル名形式: `transcription_YYYYMMDD_HHMMSS.txt`
- 内容例:
```
オブジェクト指向プログラミングの演習に、これから始めたいと思います。
```

### 具体的な出力ファイル例

```
out/
├── record_audio.wav
├── transcription_20251028_143045.txt
├── transcription_20251028_143512.txt
└── transcription_20251028_144201.txt
```

#### `transcription_20251028_143045.txt` の内容例:
```
オブジェクト指向プログラミングの演習に、これから始めたいと思います。プログラムの設計について学習していきましょう。
```

## 動作環境

- macOS (FFmpegのavfoundationを使用)
- Python 3.11+
- 必要なライブラリ: `requirements.txt`を参照

## インストール

```bash
# 依存関係のインストール
pip install -r requirements.txt

# 出力ディレクトリの作成（自動的に作成されますが、手動でも可能）
mkdir -p out
```

## 注意事項

- 音声録音はmacOSのマイクを使用します
- 文字起こしにはMLX Whisperを使用します
- ファイルは上書きされず、タイムスタンプにより区別されます
- 初回実行時は、文字起こしモデルのダウンロードに時間がかかる場合があります

## トラブルシューティング

### よくあるエラー

1. **mlx-whisper関連のエラー**
   ```
   pip install mlx-whisper
   ```

2. **FFmpeg関連のエラー**
   ```bash
   brew install ffmpeg
   ```

3. **マイクアクセス権限エラー**
   - システム環境設定 > セキュリティとプライバシー > マイクでアプリケーションを許可

## API仕様

### record_pc_audio(duration_s: int, output_file: Path) -> None
- **概要**: 指定秒数の音声を録音
- **引数**: 
  - `duration_s`: 録音秒数
  - `output_file`: 出力ファイルパス
- **戻り値**: なし

### transcribe_from_audio(audio_path: Union[str, Path]) -> str
- **概要**: 音声ファイルから文字起こしを実行
- **引数**: 
  - `audio_path`: 音声ファイルのパス
- **戻り値**: 文字起こしされたテキスト（失敗時は空文字列）

### save_with_timestamp(text: str, output_dir: Path = Path("out")) -> None
- **概要**: テキストをタイムスタンプ付きファイルに保存
- **引数**: 
  - `text`: 保存するテキスト
  - `output_dir`: 出力ディレクトリ（デフォルト: "out"）
- **戻り値**: なし
