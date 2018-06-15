# -*- coding:utf-8 -*-
__author__ = 'hzj'



from django import forms
from operation.models import UserAsk


#做普通的form表单
#可以对form表单进行一定的限制，比如required=TRUE 表示该内容必须不为空，否则会报错(相当于blank=true,null=true)，
# min_length = 2表示最小长度为2,max_length =20表示最大长度为20
#缺点:代码的重复性过高
# class UseAskForm(forms.Form):
#     name = forms.CharField(required=True, min_length=2, max_length=20)
#     phone = forms.CharField(required=True, max_length=11, min_length=11)
#     course_name = forms.CharField(required=True, min_length=5, max_length=50)



#进阶版form 继承ModelForm

class UserAskForm(forms.ModelForm):
    # my_friend = forms.CharField()#继承之后还能自己再创建新的字段，你说牛不牛比
    class Meta:
        model = UserAsk  #定义该表单继承自某一个模板
        fields = ['name','mobile','course_name'] #定义表单索要对模型操作的部分字段，有时候没有必要全部继承，继承字段