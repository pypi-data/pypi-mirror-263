import argparse
import json
import os
import sys
from spotify_dl.scaffold import console
from spotify_dl.utils import sanitize
from spotify_translator.constants import VERSION
from spotify_translator.utils import get_spotify_auth, download_urls, translate_song


def spotify_translator():
    parser = argparse.ArgumentParser(
        prog="spotify_translator", description="Translate Spotify songs."
    )
    parser.add_argument(
        "-l",
        "--url",
        action="store",
        help="Spotify Playlist link URL",
        type=str,
        nargs="+",
        required=False,  # this has to be set to false to prevent useless prompt for url when all user wants is the script version
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        action="store",
        help="Specify download directory for transcriptions, translations, and mp3.",
        required=False,
        default=".",
    )
    parser.add_argument(
        "-d",
        "--download",
        action="store_true",
        help="Download mp3 and transcriptions using youtube-dl",
        required=False,
        default=False,
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="Shows current version of the program",
    )
    parser.add_argument(
        "-mc",
        "--multi-core",
        action="store",
        type=str,
        default=0,
        help="Use multiprocessing [-m [int:numcores]",
    )
    parser.add_argument(
        "-fl",
        "--from-lang",
        action="store",
        type=str,
        help="Specify the base language[-fl [str:lang]",
        required=False,
    )

    parser.add_argument(
        "-tl",
        "--to-lang",
        action="store",
        type=str,
        help="Specify the desired translated language [-tl [str:lang]",
        required=False,
    )

    args = parser.parse_args()
    num_cores = os.cpu_count()
    args.multi_core = int(args.multi_core)

    if args.multi_core > (num_cores - 1):
        args.multi_core = num_cores - 1

    if args.version:
        console.print(f"spotify_dl [bold green]v{VERSION}[/bold green]")
        sys.exit(0)

    if os.path.isfile(os.path.expanduser("~/.spotify_translator_settings")):
        with open(os.path.expanduser("~/.spotify_translator_settings")) as file:
            config = json.load(file)
            print(config)

        for key, value in config.items():
            if (isinstance(value, bool) and value) or (
                isinstance(value, str) and value and value.lower() in ["true", "t"]
            ):
                setattr(args, key, True)
            else:
                setattr(args, key, value)

    if not args.url:
        raise (Exception("No playlist url provided:"))

    sp = get_spotify_auth()
    download_data = download_urls(
        sp, args.url, args.output, args.download, args.multi_core
    )

    for tracks in download_data:
        for song in tracks["songs"]:
            file_name = sanitize(f"{song['artist']} - {song['name']}", "#")

            print(f"\nProcessing {file_name}\n")

            transcription, translation = translate_song(
                tracks["save_path"],
                file_name,
                args.from_lang,
                args.to_lang,
                args.download,
            )

            print(f"\n\nTranscription: {transcription}\n")
            print(f"Translation: {translation}\n\n")


if __name__ == "__main__":
    spotify_translator()
