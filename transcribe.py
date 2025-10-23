import openai
from pathlib import Path

def transcribe_from_audio(audio_path: Path) -> str:
    """
    wavファイルを読み取り、OpenAI APIで文字起こしを行う
    """
    with open(audio_path, "rb") as audio_file:
        transcript = openai.Audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=audio_file
        )
    text = transcript.text
    print("[INFO] 文字起こし完了")
    return text