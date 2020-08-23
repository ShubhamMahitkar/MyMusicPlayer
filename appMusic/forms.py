from django import forms
from appMusic.models import *

class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieModel
        fields = "__all__"

class MusicForm(forms.ModelForm):
    class Meta:
        model = MusicModel
        fields = "__all__"

        # def clean_song(self):
        #     s = self.cleaned_data["song"]
        #
        #     if s.endwith(".mp3"):
        #         return s
        #     else:
        #         raise forms.ValidationError("We accept .mp3 files only")
