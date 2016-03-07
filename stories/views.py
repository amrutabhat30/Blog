from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import Story, Comment
from forms import CreateStoryForm, CreateCommentForm
from django.db.models import F
from django.core.urlresolvers import reverse
from datetime import datetime, timedelta
from utilities import get_comment,get_story
import logging
logger = logging.getLogger(__name__)


def home(request):
    """
    returns top 5 stories that are not flagged
    :param request:
    :return:
    """
    stories = Story.objects.filter(flag=False).order_by('-created_on')[:5]
    message = ''
    if not stories:
        message = "No stories to show"
    return render(request, 'stories/home.html', {'stories': stories, 'param': 'home', 'message': message})


def admin_story(request):
    """
    flag / unflag stories
    :param request:
    :return:
    """
    try:
        if request.method == 'POST':
            flag_list = request.POST.getlist('flags')
            Story.objects.filter(id__in=flag_list).update(flag=True)
            Story.objects.exclude(id__in=flag_list).update(flag=False)
            return HttpResponseRedirect(reverse('home'))
        else:
            stories = Story.objects.all().order_by('-created_on')
            return render(request, 'stories/home.html', {'stories': stories, 'param': 'admin', 'form': CreateStoryForm()})
    except Exception, e:
        logger.error(e)
        return render(request, 'stories/error.html')


def filter_stories(request):
    """
    filter stories on time / duration in hours
    :param request:
    :return:
    """
    try:
        duration = request.GET['duration']
        time_threshold = datetime.now() - timedelta(hours=int(duration))
        stories = Story.objects.filter(flag=False,created_on__gt=time_threshold)[:5]
        message = ''
        if not stories:
            message = "No stories to show"
        return render(request, 'stories/home.html', {'stories': stories, 'param': 'home', 'message': message})
    except Exception, e:
        logger.error(e)
        return render(request, 'stories/error.html')


def create_story(request):
    """
    create and save a story with title and link
    :param request:
    :return:
    """
    try:
        if request.method == 'POST':
            story_form = CreateStoryForm(request.POST)

            if story_form.is_valid():
                story_form.save()
                return HttpResponseRedirect(reverse('home'))
        else:
            story_form = CreateStoryForm()
        return render(request, 'stories/create_story.html', {'form': story_form, 'param': 'create'})
    except Exception, e:
        logger.error(e)
        return render(request, 'stories/error.html')


def view_story(request,story_id):
    """
    detailed view of a story
    :param request:
    :param story_id:
    :return:
    """
    try:
        story = get_story(request, story_id)
        comment_form = CreateCommentForm()
        return render(request, 'stories/display_story.html', {'story': story, 'form': comment_form})
    except Exception, e:
        logger.error(e)
        return render(request, 'stories/error.html')


def edit_story(request,story_id):
    """
    edit and update a story
    :param request:
    :param story_id:
    :return:
    """
    try:
        story = get_story(request, story_id)
        if request.method == 'POST':
            story_form = CreateStoryForm(request.POST, instance=story)
            if story_form.is_valid():
                story_form.save()
                return HttpResponseRedirect(reverse('home'))
        else:
            story_form = CreateStoryForm(instance=story)
        return render(request, 'stories/create_story.html', {'form': story_form,'param': 'edit'})
    except Exception, e:
        logger.error(e)
        return render(request, 'stories/error.html')


def delete_story(request,story_id):
    """
    delete a story
    :param request:
    :param story_id:
    :return:
    """
    try:
        story = get_story(request, story_id)
        story.delete()
        return HttpResponseRedirect(reverse('home'))
    except Exception, e:
        logger.error(e)
        return render(request, 'stories/error.html')


def up_vote(request,story_id):
    """
    Up vote a story
    :param request:
    :param story_id:
    :return:
    """
    try:
        story = get_story(request, story_id)
        story.up_vote = F('up_vote') + 1
        story.save()
        return HttpResponseRedirect(reverse('home'))
    except Exception, e:
        logger.error(e)
        return render(request, 'stories/error.html')


def down_vote(request,story_id):
    """
    Down vote a story
    :param request:
    :param story_id:
    :return:
    """
    try:
        story = get_story(request, story_id)
        story.down_vote = F('down_vote') + 1
        story.save()
        return HttpResponseRedirect(reverse('home'))
    except Exception, e:
        logger.error(e)
        return render(request, 'stories/error.html')


def create_comment(request, story_id):
    """
    create a comment for a story
    """
    try:
        if request.method == 'POST':
            story = get_story(request, story_id)
            comment_form = CreateCommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.story = story
                comment.save()
                return HttpResponseRedirect(reverse('view_story', args=[story_id]))
            return render(request, 'stories/display_story.html', {'form': comment_form, 'param': 'create', 'story': story})
        else:
            return HttpResponseRedirect(reverse('home'))
    except Exception, e:
        logger.error(e)
        return render(request, 'stories/error.html')


def view_comments(request,story_id):
    """
    return top 25 comments on a story
    :param request:
    :param story_id:
    :return:
    """
    try:
        story = get_story(request,story_id)
        comments = Comment.objects.filter(story=story_id).order_by('-posted_on')[:25]
        message = ''
        if not comments:
            message = "No comments to show"
        return render(request, 'stories/display_comments.html', {'comments': comments,'story': story, 'message': message})
    except Exception, e:
        logger.error(e)
        return render(request, 'stories/error.html')


def edit_comment(request,story_id,comment_id):
    """
    edit a comment on a story
    :param request:
    :param story_id:
    :param comment_id:
    :return:
    """
    try:
        comment = get_comment(request,comment_id)
        if request.method == 'POST':
            comment_form = CreateCommentForm(request.POST, instance=comment)
            if comment_form.is_valid():
                comment_form.save()
                return HttpResponseRedirect(reverse('view_story', args=[story_id]))
        else:
            comment_form = CreateCommentForm(instance=comment)
        return render(request, 'stories/edit_comment.html', {'form': comment_form, 'param': 'edit'})
    except Exception, e:
        logger.error(e)
        return render(request, 'stories/error.html')


def delete_comment(request,story_id,comment_id):
    """
    delete a comment on a story
    :param request:
    :param story_id:
    :param comment_id:
    :return:
    """
    try:
        comment = get_comment(request,comment_id)
        comment.delete()
        return HttpResponseRedirect(reverse('view_story', args=[story_id]))
    except Exception, e:
        logger.error(e)
        return render(request, 'stories/error.html')






