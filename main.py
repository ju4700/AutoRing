from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.logger import Logger
from jnius import autoclass
from plyer import notification

MediaRecorder = autoclass('android.media.MediaRecorder')
Context = autoclass('android.content.Context')
AudioManager = autoclass('android.media.AudioManager')

class NoiseMeter:
    def __init__(self):
        self.recorder = MediaRecorder()
        self.recorder.setAudioSource(MediaRecorder.AudioSource.MIC)
        self.recorder.setOutputFormat(MediaRecorder.OutputFormat.THREE_GPP)
        self.recorder.setAudioEncoder(MediaRecorder.AudioEncoder.AMR_NB)
        self.recorder.setOutputFile('/dev/null')
        self.recorder.prepare()
        self.recorder.start()

    def get_noise_level(self):
        try:
            return self.recorder.getMaxAmplitude()
        except Exception as e:
            Logger.error(f"Error getting noise level: {e}")
            return 0

    def stop(self):
        self.recorder.stop()
        self.recorder.release()

def set_ringtone_mode(noise_level):
    # Get the current activity context
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    activity = PythonActivity.mActivity
    audio_manager = activity.getSystemService(Context.AUDIO_SERVICE)

    THRESHOLD = 2000  # Example threshold, adjust as needed
    MAX_VOLUME = audio_manager.getStreamMaxVolume(AudioManager.STREAM_RING)

    if noise_level > THRESHOLD:
        audio_manager.setRingerMode(AudioManager.RINGER_MODE_NORMAL)
        audio_manager.setStreamVolume(AudioManager.STREAM_RING, MAX_VOLUME, 0)
    else:
        audio_manager.setRingerMode(AudioManager.RINGER_MODE_VIBRATE)

class AutoRingtoneApp(App):
    def build(self):
        self.label = Label(text="Auto Ringtone App")
        self.noise_meter = NoiseMeter()
        Clock.schedule_interval(self.update_ringtone, 1)  # Check every 1 second
        self.start_background_service()
        return self.label

    def update_ringtone(self, dt):
        noise_level = self.noise_meter.get_noise_level()
        set_ringtone_mode(noise_level)

        # Check noise level and show/hide notification based on threshold
        if noise_level > 2000:
            self.show_notification("AutoRing is now active")
        else:
            notification.dismiss("auto_ringtone_notification")

    def show_notification(self, message):
        notification.notify(
            title="AutoRing",
            message=message,
            app_name='AutoRingtone App',
            ticker='AutoRing is running',
            app_icon=None,  # You can provide an icon path here
            tag="auto_ringtone_notification"
        )

    def start_background_service(self):
        PythonService = autoclass('org.kivy.android.PythonService')
        self.service = PythonService.mService

        from android import mActivity
        mActivity.startService(self.service)

    def on_stop(self):
        self.noise_meter.stop()

if __name__ == '__main__':
    AutoRingtoneApp().run()
