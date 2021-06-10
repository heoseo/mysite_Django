from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question


@login_required(login_url='common:login')
def question_create(request):
    """
    pybo 질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        # 화면에서 전달받은 데이터로 폼값이 채워지도록 객체 생성
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            # 바로 저장하지 않고 임시저장
            question.create_date = timezone.now()
            # create_date 값 설정하고 save()로 실제 저장
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
        # 입력값 없이 객체 생성

    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
    """
    pybo 질문수정
    """
    question = get_object_or_404(Question, pk=question_id)

    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)

        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:detail', question_id=question.id)

    else:
        form = QuestionForm(instance=question)

    context = {'form': form}

    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:Login')
def question_delete(request, question_id):
    """
    pybo 질문삭제
    """
    question = get_object_or_404(Question, pk=question_id)

    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)

    question.delete()

    return redirect('pybo:index')