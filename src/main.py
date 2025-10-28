from paths import DIR_OUT
from record import record_pc_audio
from transcribe import transcribe_from_audio
from save import save_with_timestamp


def main() -> None:
    # 1. 音声を録音
    path_audio = DIR_OUT / "record_audio.wav"
    print("音声録音を開始します（10秒間）...")
    record_pc_audio(duration_s=10, output_file=path_audio)
    print(f"録音が完了しました: {path_audio}")
    
    # 2. 音声ファイルを文字起こし
    print("文字起こしを実行中...")
    transcribed_text = transcribe_from_audio(path_audio)
    
    if transcribed_text:
        # 3. 文字起こし結果をタイムスタンプ付きファイルに保存
        print("文字起こし結果をファイルに保存しています...")
        save_with_timestamp(transcribed_text, DIR_OUT)
        print("すべての処理が完了しました。")
        print(f"文字起こし結果: {transcribed_text}")
    else:
        print("文字起こしに失敗しました。処理を終了します。")


if __name__ == "__main__":
    main()
