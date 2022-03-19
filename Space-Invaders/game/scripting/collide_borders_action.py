from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        explosion_sound = Sound(EXPLOSION_SOUND)
        over_sound = Sound(OVER_SOUND)
                
        if x < FIELD_LEFT:
            ball.explosion_x()
            self._audio_service.play_sound(explosion_sound)

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            ball.explosion_x()
            self._audio_service.play_sound(explosion_sound)

        if y < FIELD_TOP:
            ball.explosion_y()
            self._audio_service.play_sound(explosion_sound)

        elif y >= (FIELD_BOTTOM - BALL_WIDTH):
            stats = cast.get_first_actor(STATS_GROUP)
            stats.lose_life()
            
            if stats.get_lives() > 0:
                callback.on_next(TRY_AGAIN) 
            else:
                callback.on_next(GAME_OVER)
                self._audio_service.play_sound(over_sound)