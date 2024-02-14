from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    nickname = forms.CharField(
        label = '昵称',
        max_length=50,
        widget=forms.widgets.Input(
            attrs={'class':'form-control','style':'width:60%;'}
        )
    )
    email = forms.CharField(
        label='Email',
        max_length=50,
        widget=forms.widgets.EmailInput(
            attrs={'class':'form-control','style':'width:60%;'}
        )
    )
    
    content = forms.CharField(
        label='内容',
        max_length=500,
        widget=forms.widgets.Textarea(
            attrs={'rows':6,'cols':60,'class':'form-control'}
        )
    )
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('内容长度过短')
        return content
    
    class Meta:
        model = Comment
        fields = ('nickname',
                  'email',
                  'content',
                  )
        #如果你的表单字段在模型中是必需的（例如，模型中定义了 blank=False 或 null=False），
        #即使你在 fields 或 exclude 中排除了它们，它们也会出现在表单中。