from paths import DIR_OUT
from record import record_pc_audio


def main() -> None:
    path_audio = DIR_OUT / "record_audio.wav"
    record_pc_audio(duration_s=10, output_file=path_audio)


if __name__ == "__main__":
    main()
