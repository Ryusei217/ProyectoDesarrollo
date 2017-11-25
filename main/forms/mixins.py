from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset
from django import forms


class FieldSetModelFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FieldSetModelFormMixin, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 col-form-label'
        self.helper.field_class = 'col-sm-10'
        self.helper.wrapper_class = 'form-group row'
        self.field_names = self.fields.keys()

    def set_legend(self, text):
        self.helper.layout = Fieldset(text, *self.field_names)

    def set_action(self, action):
        self.helper.form_action = action
