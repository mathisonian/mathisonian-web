from django import forms

from mathisonian.labs.models import Sketch


class Create(forms.Form):
    content = forms.CharField()

    def save(self):
        return Sketch.objects.create(content=self.cleaned_data['content'])


class NewVersion(forms.Form):
    content = forms.CharField()
    sketch_id = forms.CharField()

    def save(self):
        sketch = Sketch.get_from_encoded_id(self.cleaned_data['sketch_id'])
        version = sketch.create_version(content=self.cleaned_data['content'])

        return version
