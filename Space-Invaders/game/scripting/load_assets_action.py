from pathlib import Path
from game.scripting.action import Action
import os, sys

class LoadAssetsAction(Action):

    def __init__(self, audio_service, video_service):
        self._audio_service = audio_service
        self._video_service = video_service

    def execute(self, cast, script, callback):
        self._audio_service.load_sounds(os.path.dirname(sys.modules['__main__'].__file__) + "/assets/sounds")
        self._video_service.load_fonts(os.path.dirname(sys.modules['__main__'].__file__) + "/assets/fonts")
        self._video_service.load_images(os.path.dirname(sys.modules['__main__'].__file__) + "/assets/images")
        