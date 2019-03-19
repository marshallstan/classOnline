# __author__ = 'Marshall Stan'

import re
from django import forms

from operation.models import UserAsk

REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"


class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("手机号码非法", code="mobile_invalid")
