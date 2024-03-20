from spotify_dl.spotify import (
    fetch_tracks,
    parse_spotify_url,
    get_item_name,
    validate_spotify_urls,
)
from spotify_dl.youtube import (
    download_songs,
    default_filename,
)
from spotify_dl.scaffold import get_tokens
from spotipy.oauth2 import SpotifyClientCredentials
from pathlib import Path, PurePath
import sys
import whisper
import spotipy

LANGUAGES = {
    "en": "english",
    "zh": "chinese",
    "de": "german",
    "es": "spanish",
    "ru": "russian",
    "ko": "korean",
    "fr": "french",
    "ja": "japanese",
    "pt": "portuguese",
    "tr": "turkish",
    "pl": "polish",
    "ca": "catalan",
    "nl": "dutch",
    "ar": "arabic",
    "sv": "swedish",
    "it": "italian",
    "id": "indonesian",
    "hi": "hindi",
    "fi": "finnish",
    "vi": "vietnamese",
    "he": "hebrew",
    "uk": "ukrainian",
    "el": "greek",
    "ms": "malay",
    "cs": "czech",
    "ro": "romanian",
    "da": "danish",
    "hu": "hungarian",
    "ta": "tamil",
    "no": "norwegian",
    "th": "thai",
    "ur": "urdu",
    "hr": "croatian",
    "bg": "bulgarian",
    "lt": "lithuanian",
    "la": "latin",
    "mi": "maori",
    "ml": "malayalam",
    "cy": "welsh",
    "sk": "slovak",
    "te": "telugu",
    "fa": "persian",
    "lv": "latvian",
    "bn": "bengali",
    "sr": "serbian",
    "az": "azerbaijani",
    "sl": "slovenian",
    "kn": "kannada",
    "et": "estonian",
    "mk": "macedonian",
    "br": "breton",
    "eu": "basque",
    "is": "icelandic",
    "hy": "armenian",
    "ne": "nepali",
    "mn": "mongolian",
    "bs": "bosnian",
    "kk": "kazakh",
    "sq": "albanian",
    "sw": "swahili",
    "gl": "galician",
    "mr": "marathi",
    "pa": "punjabi",
    "si": "sinhala",
    "km": "khmer",
    "sn": "shona",
    "yo": "yoruba",
    "so": "somali",
    "af": "afrikaans",
    "oc": "occitan",
    "ka": "georgian",
    "be": "belarusian",
    "tg": "tajik",
    "sd": "sindhi",
    "gu": "gujarati",
    "am": "amharic",
    "yi": "yiddish",
    "lo": "lao",
    "uz": "uzbek",
    "fo": "faroese",
    "ht": "haitian creole",
    "ps": "pashto",
    "tk": "turkmen",
    "nn": "nynorsk",
    "mt": "maltese",
    "sa": "sanskrit",
    "lb": "luxembourgish",
    "my": "myanmar",
    "bo": "tibetan",
    "tl": "tagalog",
    "mg": "malagasy",
    "as": "assamese",
    "tt": "tatar",
    "haw": "hawaiian",
    "ln": "lingala",
    "ha": "hausa",
    "ba": "bashkir",
    "jw": "javanese",
    "su": "sundanese",
    "yue": "cantonese",
}

# language code lookup by name, with a few language aliases
TO_LANGUAGE_CODE = {
    **{language: code for code, language in LANGUAGES.items()},
    "burmese": "my",
    "valencian": "ca",
    "flemish": "nl",
    "haitian": "ht",
    "letzeburgesch": "lb",
    "pushto": "ps",
    "panjabi": "pa",
    "moldavian": "ro",
    "moldovan": "ro",
    "sinhalese": "si",
    "castilian": "es",
    "mandarin": "zh",
}


def translate_song(path, file_name, from_lang, to_lang, download):
    model = whisper.load_model("small")

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(f"{path}/{file_name}.mp3")
    # audio = whisper.pad_or_trim(audio)

    # Process audio
    transcription = model.transcribe(
        audio, language=from_lang, task="transcribe", fp16=False
    )["text"]
    translation = model.transcribe(
        audio, language=from_lang, task="translate", fp16=False
    )["text"]

    if download is True:
        with open(f"{path}/{file_name}_transcription.txt", "w") as f:
            f.write(transcription)
        with open(f"{path}/{file_name}_translation.txt", "w") as f:
            f.write(translation)

    return (transcription, translation)


def get_spotify_auth():
    tokens = get_tokens()
    if tokens is None:
        sys.exit(1)
    client_id, client_secret = tokens

    sp = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=client_id, client_secret=client_secret
        )
    )
    return sp


def download_urls(
    sp, urls: list[str], output_path: str, download: bool, multi_core: int
) -> list:
    valid_urls = validate_spotify_urls(urls)
    if not valid_urls:
        sys.exit(1)

    url_data = {"urls": []}
    for url in valid_urls:
        url_dict = {}
        item_type, item_id = parse_spotify_url(url)
        directory_name = get_item_name(sp, item_type, item_id)
        url_dict["save_path"] = Path(
            PurePath.joinpath(Path(output_path), Path(directory_name))
        )
        url_dict["save_path"].mkdir(parents=True, exist_ok=True)
        # log.info("Saving songs to %s directory", directory_name)
        url_dict["songs"] = fetch_tracks(sp, item_type, item_id)
        url_data["urls"].append(url_dict.copy())

    if download is True:
        file_name_f = default_filename
        download_songs(
            songs=url_data,
            output_dir=output_path,
            format_str="bestaudio/best",
            skip_mp3=False,
            keep_playlist_order=False,
            no_overwrites=False,
            remove_trailing_tracks="no",
            use_sponsorblock="yes",
            file_name_f=file_name_f,
            multi_core=multi_core,
            proxy="",
        )

    return url_data["urls"]
