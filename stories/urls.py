from django.conf.urls import patterns, url


urlpatterns = patterns('stories',
    url(r'^$', 'views.home', name='home'),                                                          #Home Page
    url(r'^submit/$', 'views.create_story', name='create_story'),                                   #Create a story
    url(r'^stories/$', 'views.filter_stories', name='filter_stories'),                                #Filter Story
    url(r'^story/(?P<story_id>[\d]+)/$', 'views.view_story', name='view_story'),               #View Story
    url(r'^story/(?P<story_id>[\d]+)/edit/$', 'views.edit_story', name='edit_story'),               #Edit Story
    url(r'^story/(?P<story_id>[\d]+)/delete/$', 'views.delete_story', name='delete_story'),         #Delete Story
    url(r'^story/(?P<story_id>[\d]+)/up_vote/$', 'views.up_vote', name='up_vote'),                  #UpVote Story
    url(r'^story/(?P<story_id>[\d]+)/down_vote/$', 'views.down_vote', name='down_vote'),            #DownVote Story

    url(r'^story/(?P<story_id>[\d]+)/comment/$', 'views.create_comment', name='create_comment'),    #Create Comment
    url(r'^story/(?P<story_id>[\d]+)/comments/$', 'views.view_comments', name='view_comments'),   #View Comment
    url(r'^story/(?P<story_id>[\d]+)/comment/(?P<comment_id>[\d]+)/edit/$', 'views.edit_comment',   #Edit Comment
        name='edit_comment'),
    url(r'^story/(?P<story_id>[\d]+)/comment/(?P<comment_id>[\d]+)/delete/$',                      #Delete Comment
        'views.delete_comment',name='delete_comment'),

    url(r'^admin/$', 'views.admin_story', name='admin_story'),                                      #Admin Page


)
