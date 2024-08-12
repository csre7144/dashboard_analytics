from .models import category
from django import forms

class category_items(forms.ModelForm):
      class Meta:
            model = category
            fields = ['image', 'title', 'description', 'status']

      def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["image"].widget.attrs.update({"class": "form-control"})
            self.fields["title"].widget.attrs.update({"class": "form-control"})
            self.fields["description"].widget.attrs.update({"class": "form-control"})
            self.fields["status"].widget.attrs.update({"class": "form-control", "type": "checkbox"})
