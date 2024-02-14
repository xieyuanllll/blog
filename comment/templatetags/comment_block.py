from django import template

from comment.forms import CommentForm
from comment.models import Comment

register = template.Library()


@register.inclusion_tag('comment/block.html')
def comment_block(target):
    return {
        'target': target,
        'comment_form': CommentForm(),
        'comment_list': Comment.get_by_target(target),
    }

# 这段代码定义了一个自定义模板标签（inclusion tag），名为 comment_block。
#自定义模板标签是 Django 中用于在模板中执行一些特定功能或生成特定内容的工具。

# 具体来说，这个自定义模板标签用于渲染评论区块。
#它接收一个 target 参数，这个参数通常是当前页面的目标地址，用于确定评论所属的对象。

# 在模板中使用这个自定义标签时，它会渲染指定模板 comment/block.html，并将以下数据传递给模板：


# target: 评论区块的目标地址。
# comment_form: 一个 CommentForm 实例，用于在模板中渲染评论表单。
# comment_list: 一个包含了目标地址对应的所有评论的列表，通过调用 Comment 模型的 get_by_target 方法获取。
# 这样，当在模板中使用 {% comment_block target %} 标签时，会将上述数据传递给 comment/block.html 模板，并在页面上渲染评论区块。





